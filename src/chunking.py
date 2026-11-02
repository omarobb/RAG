from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from .models import Chunk
import os

indexed_ex = {'.py', '.md'}


def build_splitter(extension: str,
                   max_size: int) -> RecursiveCharacterTextSplitter:

    if extension == '.py':
        lang = Language.PYTHON
    elif extension == '.md':
        lang = Language.MARKDOWN
    else:
        lang = None
    if lang:
        return RecursiveCharacterTextSplitter.from_language(
                                                        lang,
                                                        chunk_size=max_size,
                                                        chunk_overlap=0,
                                                        add_start_index=True
                                                        )
    else:
        return RecursiveCharacterTextSplitter(chunk_size=max_size,
                                              chunk_overlap=0,
                                              add_start_index=True)


def chunk_file(path: str, max_size: int) -> list[Chunk]:
    extension = os.path.splitext(path)[1]
    if extension not in indexed_ex:
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except (OSError, UnicodeDecodeError, FileNotFoundError) as e:
        print(f"ERROR in file: {e}")
        return []
    if not text:
        return []

    splitter = build_splitter(extension, max_size)
    docs = splitter.create_documents([text])

    chunks = []

    for doc in docs:
        start = doc.metadata["start_index"]
        end = start + len(doc.page_content)
        chunks.append(
            Chunk(file_path=path,
                  first_character_index=start,
                  last_character_index=end,
                  text=doc.page_content)
        )
    return chunks
