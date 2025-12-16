#!/usr/bin/env python3
"""Generate learning blueprint scaffolds for each KG node."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

if str(SCRIPT_DIR) not in sys.path:
    sys.path.append(str(SCRIPT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from kg_loader import KGNode, MarketingAnalyticsKG  # type: ignore

BLOOM_PRIORITY: Sequence[tuple[str, Sequence[str]]] = (
    ("CREATE", ("STRATEGY",)),
    ("EVALUATE", ("THEORY", "STRATEGY")),
    ("ANALYZE", ("PROCESS", "ANALYTICAL")),
    ("APPLY", ("TACTICAL", "SKILL_APPLIED")),
    ("UNDERSTAND", ()),
)


@dataclass
class BlueprintContext:
    node: KGNode
    ancestors: List[KGNode]
    children: List[KGNode]


class LearningBlueprintBuilder:
    def __init__(self, kg: MarketingAnalyticsKG, min_level: int = 2, max_level: int | None = None) -> None:
        self.kg = kg
        self.min_level = min_level
        self.max_level = max_level

    def build(self) -> Dict[str, Any]:
        entries: List[Dict[str, Any]] = []
        for node in self.kg.nodes.values():
            if node.level < self.min_level:
                continue
            if self.max_level and node.level > self.max_level:
                continue
            context = BlueprintContext(
                node=node,
                ancestors=self.kg.ancestors(node.id),
                children=self._children(node.id),
            )
            entries.append(self._build_entry(context))

        entries.sort(key=lambda item: item["topic_path"])
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "framework_version": "1.0",
            "node_count": len(entries),
            "nodes": entries,
        }

    def _children(self, node_id: str) -> List[KGNode]:
        return [record for record in self.kg.nodes.values() if record.parent_id == node_id]

    def _build_entry(self, ctx: BlueprintContext) -> Dict[str, Any]:
        node = ctx.node
        payload = node.payload

        knowledge_types = payload.get("knowledge_types", [])
        skill_dimensions = payload.get("skill_dimensions", [])
        value_streams = payload.get("value_streams", [])
        description = payload.get("description") or node.name

        bloom_primary = self._infer_bloom(knowledge_types, skill_dimensions)
        solo_target = self._infer_solo(node.level)
        learning_modes = self._infer_learning_modes(node.level, knowledge_types)

        objectives = self._craft_objectives(node, description, value_streams, bloom_primary)
        activities = self._craft_activities(node, bloom_primary)
        assessments = self._craft_assessments(node)
        resources = self._craft_resources(payload)
        metacognition = self._craft_metacognition()

        prerequisites = [
            {"id": ancestor.id, "name": ancestor.name, "topic_path": ancestor.topic_path}
            for ancestor in reversed(ctx.ancestors)
        ]
        next_topics = [
            {"id": child.id, "name": child.name, "topic_path": child.topic_path}
            for child in ctx.children
        ]

        checklist = {
            "learning_outcomes": bool(objectives),
            "prerequisites": bool(prerequisites),
            "activities": bool(activities),
            "assessments": bool(assessments["formative"] or assessments["summative"]),
            "resources": bool(resources["primary_tools"] or resources["references"]),
            "metacognition": bool(metacognition["reflection_prompts"]),
        }
        coverage_index = sum(1 for ready in checklist.values() if ready) / len(checklist)
        missing_sections = [name for name, ready in checklist.items() if not ready]

        has_assets = bool(payload.get("micro_assets"))
        has_blueprints = bool(payload.get("content_blueprints"))

        if has_assets and has_blueprints:
            status = "ready"
            status_reason = "Has micro-assets and blueprint references."
        elif has_assets or has_blueprints:
            status = "in_progress"
            status_reason = "Partial assets present; fill remaining sections."
        else:
            status = "needs_content"
            status_reason = "No linked assets or blueprints yet."

        return {
            "node_id": node.id,
            "name": node.name,
            "topic_path": node.topic_path,
            "level": node.level,
            "status": status,
            "status_reason": status_reason,
            "learning_modes": learning_modes,
            "cognitive_profile": {
                "bloom_primary": bloom_primary,
                "solo_target": solo_target,
                "skill_dimensions": skill_dimensions,
                "complexity_notes": f"Level {node.level} node emphasizing {', '.join(knowledge_types) or 'mixed knowledge areas'}.",
            },
            "prerequisites": {
                "topics": prerequisites,
                "assumed_knowledge": [f"Familiarity with {ancestor.name}" for ancestor in ctx.ancestors] or [],
            },
            "enablement_path": {
                "next_topics": next_topics,
                "value_streams": value_streams,
            },
            "blueprint": {
                "learning_outcomes": {
                    "summary": f"Equip practitioners to operationalize {node.name} within marketing analytics programs.",
                    "objectives": objectives,
                    "bloom_primary": bloom_primary,
                    "solo_target": solo_target,
                },
                "activities": activities,
                "assessments": assessments,
                "resources": resources,
                "metacognition": metacognition,
            },
            "checklist": checklist,
            "gap_summary": {
                "coverage_index": round(coverage_index, 2),
                "missing_sections": missing_sections,
                "asset_counts": {
                    "micro_assets": len(payload.get("micro_assets", [])),
                    "content_blueprints": len(payload.get("content_blueprints", [])),
                    "notes_ref": len(payload.get("notes_ref", [])),
                },
            },
        }

    def _infer_bloom(self, knowledge_types: Sequence[str], skills: Sequence[str]) -> str:
        knowledge_set = {item.upper() for item in knowledge_types}
        skill_set = {item.upper() for item in skills}
        for level, triggers in BLOOM_PRIORITY:
            if not triggers:
                return level
            if knowledge_set.intersection({t.upper() for t in triggers}) or skill_set.intersection(
                {t.upper() for t in triggers}
            ):
                return level
        return "UNDERSTAND"

    def _infer_solo(self, level: int) -> str:
        if level <= 2:
            return "Extended Abstract"
        if level == 3:
            return "Relational"
        return "Multistructural"

    def _infer_learning_modes(self, level: int, knowledge_types: Sequence[str]) -> List[str]:
        modes = ["Learn", "Practice", "Reference"]
        if level <= 2:
            modes = ["Strategic Overview", "Review", "Facilitate"]
        elif "TACTICAL" in [kt.upper() for kt in knowledge_types]:
            modes = ["Hands-on Lab", "Practice", "Reference"]
        return modes

    def _craft_objectives(
        self,
        node: KGNode,
        description: str,
        value_streams: Sequence[str],
        bloom_level: str,
    ) -> List[str]:
        objectives = [
            f"Describe how {node.name} supports {', '.join(value_streams) or 'core marketing outcomes'} ({bloom_level}).",
            f"Apply the {node.name} playbook to a live marketing initiative and articulate expected KPIs.",
        ]
        if node.payload.get("tools"):
            objectives.append(
                f"Configure the primary tooling stack ({', '.join(node.payload['tools'][:3])}) to operationalize {node.name}."
            )
        if node.payload.get("kpis"):
            objectives.append(
                f"Map success indicators ({', '.join(node.payload['kpis'][:3])}) to stakeholder expectations."
            )
        return objectives[:4]

    def _craft_activities(self, node: KGNode, bloom_level: str) -> List[Dict[str, Any]]:
        return [
            {
                "name": "Concept Briefing",
                "type": "Whole-task",
                "focus": "Understand",
                "description": f"Facilitated walkthrough of {node.name} with stakeholder scenarios.",
            },
            {
                "name": "Scenario Lab",
                "type": "Practice",
                "focus": bloom_level,
                "description": f"Select a marketing program and design the {node.name} approach end-to-end.",
            },
            {
                "name": "Instrumentation Debrief",
                "type": "Part-task",
                "focus": "Apply",
                "description": f"Document required data inputs, owners, and automation for {node.name}.",
            },
        ]

    def _craft_assessments(self, node: KGNode) -> Dict[str, Any]:
        return {
            "formative": [
                {
                    "name": "Readiness pulse",
                    "type": "Concept map",
                    "criteria": "Learner can articulate components of the capability and prerequisite decisions.",
                },
                {
                    "name": "Playbook critique",
                    "type": "Peer review",
                    "criteria": f"Learner can evaluate an existing {node.name} artifact and suggest improvements.",
                },
            ],
            "summative": [
                {
                    "name": "Capability rollout plan",
                    "type": "Project",
                    "criteria": "Learner delivers a scoped rollout plan linking KPIs, owners, and tooling.",
                }
            ],
        }

    def _craft_resources(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "primary_tools": payload.get("tools", []),
            "references": payload.get("notes_ref", []),
            "content_blueprints": payload.get("content_blueprints", []),
            "micro_assets": payload.get("micro_assets", []),
        }

    def _craft_metacognition(self) -> Dict[str, Any]:
        prompts = [
            "What blockers could prevent this capability from landing in your org?",
            "Which stakeholders benefit most from this topic and how will you keep them engaged?",
            "Where can you repurpose existing assets to accelerate adoption?",
        ]
        return {
            "reflection_prompts": prompts,
            "self_checks": [
                "I can explain this capability to an exec sponsor.",
                "I can outline the first 30-day implementation plan.",
                "I know which metrics confirm adoption.",
            ],
        }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate learning blueprints for KG nodes.")
    parser.add_argument("--kg", type=Path, default=Path("artifacts/marketing_analytics_kg.json"))
    parser.add_argument("--out", type=Path, default=Path("artifacts/learning_blueprints.json"))
    parser.add_argument("--min-level", type=int, default=2, help="Minimum node level to include.")
    parser.add_argument("--max-level", type=int, default=None, help="Maximum node level to include.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    kg = MarketingAnalyticsKG(args.kg)
    builder = LearningBlueprintBuilder(kg, min_level=args.min_level, max_level=args.max_level)
    payload = builder.build()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"Wrote {payload['node_count']} learning blueprints to {args.out}")


if __name__ == "__main__":
    main()

