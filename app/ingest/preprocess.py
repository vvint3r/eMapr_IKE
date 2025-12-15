from __future__ import annotations

import mimetypes
from pathlib import Path
from typing import Optional

import fitz  # PyMuPDF


class DocumentPreprocessor:
    """Convert heterogeneous inputs (txt/md/pdf) into clean text."""

    TEXT_EXTENSIONS = {".txt", ".md", ".markdown", ".json"}

    def __init__(self, min_length: int = 400) -> None:
        self.min_length = min_length

    def load(self, path: Path) -> Optional[str]:
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(path)

        ext = path.suffix.lower()
        if ext in self.TEXT_EXTENSIONS:
            text = path.read_text(encoding="utf-8", errors="ignore")
        elif ext == ".pdf":
            text = self._extract_from_pdf(path)
        else:
            # attempt to guess MIME
            mime, _ = mimetypes.guess_type(str(path))
            if mime and mime.startswith("text/"):
                text = path.read_text(encoding="utf-8", errors="ignore")
            else:
                return None

        cleaned = self._normalize(text)
        if len(cleaned) < self.min_length:
            return None
        return cleaned

    def _extract_from_pdf(self, path: Path) -> str:
        doc = fitz.open(path)
        chunks = []
        for page in doc:
            chunks.append(page.get_text("text"))
        return "\n".join(chunks)

    @staticmethod
    def _normalize(text: str) -> str:
        lines = [line.strip() for line in text.splitlines()]
        return "\n".join(line for line in lines if line)
