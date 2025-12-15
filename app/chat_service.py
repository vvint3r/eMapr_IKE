from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import chromadb
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from neo4j import GraphDatabase


@dataclass
class RAGConfig:
    chroma_path: Path
    chroma_collection: str
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str
    neo4j_db: Optional[str] = None
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.1
    max_tokens: int = 900


class MarketingRAG:
    def __init__(self, config: RAGConfig) -> None:
        self.config = config
        self._vectorstore = self._build_vectorstore()
        self._driver = GraphDatabase.driver(
            config.neo4j_uri, auth=(config.neo4j_user, config.neo4j_password)
        )
        self._llm = ChatOpenAI(
            model=config.model_name,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
        )
        prompt = PromptTemplate(
            template="""You are a marketing analytics expert. Use the provided context and KG facts to answer.
            Cite specific capabilities or nodes when relevant.

            Context:
            {context}

            KG Facts:
            {kg_facts}

            Question: {question}
            Answer:""",
            input_variables=["context", "kg_facts", "question"],
        )
        self._chain = ConversationalRetrievalChain.from_llm(
            llm=self._llm,
            retriever=self._vectorstore.as_retriever(search_kwargs={"k": 5}),
            combine_docs_chain_kwargs={"prompt": prompt},
            return_source_documents=True,
        )

    def _build_vectorstore(self) -> Chroma:
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma(
            collection_name=self.config.chroma_collection,
            embedding_function=embeddings,
            persist_directory=str(self.config.chroma_path),
        )
        return vectorstore

    def _fetch_kg_context(self, node_ids: List[str]) -> str:
        if not node_ids:
            return ""
        query = (
            "MATCH (n:MA_Node) WHERE n.id IN $ids "
            "OPTIONAL MATCH (n)-[r]->(m:MA_Node) "
            "RETURN n.id AS id, n.name AS name, n.topic_path AS topic, collect(distinct r.relation) AS relations"
        )
        with self._driver.session(database=self.config.neo4j_db) as session:
            records = session.run(query, {"ids": node_ids})
            parts = []
            for record in records:
                rels = record["relations"]
                rel_text = ", ".join(rel for rel in rels if rel)
                parts.append(
                    f"{record['name']} ({record['topic']}): relationships -> {rel_text or 'none'}"
                )
        return "\n".join(parts)

    def ask(self, question: str, history: Optional[List[tuple[str, str]]] = None) -> dict:
        history = history or []
        response = self._chain(
            {
                "question": question,
                "chat_history": history,
                "kg_facts": "",
            }
        )
        docs: List[Document] = response.get("source_documents", [])
        node_ids: List[str] = []
        for doc in docs:
            meta = doc.metadata or {}
            node_id = meta.get("node_id")
            if node_id:
                node_ids.append(node_id)
        kg_context = self._fetch_kg_context(list({nid for nid in node_ids}))

        answer = response["answer"]
        return {
            "answer": answer,
            "sources": [doc.metadata for doc in docs],
            "kg_context": kg_context,
        }
