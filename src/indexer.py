import bm25s
import os
import tqdm
from tokenize import tokenize
from chunking import chunk_file
from pathlib import Path
class Indexer:
    def __init__(self, raw_dir: str, processed_dir: str, max_chunks_size: int) -> None:
        self.chunks = []
        self.bm25 = None
        self.max_chunks_size = max_chunks_size
        self.processed_dir = processed_dir
        self.raw_dir = raw_dir

    def collect_filse(self) -> list[str]:
        file_to_ignore = '__pycache__'
        root_dir = 'data/raw'
        work_filse = []
        indexed_ext = {'.py', '.md'}
        for root, dirs, files in os.walk(self.raw_dir):
            for name in files:
                extention = name.split('.')[1]
                if extention in indexed_ext:
                    work_filse.append(name)
        return sorted(work_filse)

    def build(self) -> None:
        files = self.collect_filse()
        for path in tqdm.tqdm(files):
            try:
                self.chunks.append(chunk_file(path, self.max_chunks_size)) #############################
            except ValueError:   #############3
                print("ERROR in chunk_file")
                continue
        tokens_per_chunk = [bm25s.tokenize(c) for c in self.chunks]
        self.bm25 = bm25s.BM25()
        self.bm25.index(tokens_per_chunk)


    def save(self) -> None:
        path = Path(self.processed_dir)
        path.mkdir(parents=True, exist_ok=True)
        self.bm25.save(self.processed_dir / "bm25")

        

