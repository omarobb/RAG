import bm25s
import os
import tqdm
from tokenize import tokenize
class Indexer:
    def __init__(self, raw_dir: str, processed_dir: str, max_chunks_size: int) -> None:
        chunks = []
        bm25 = None

    def collect_filse(self) -> list[str]:
        file_to_ignore = '__pycache__'
        root_dir = 'data/raw'
        work_filse = []
        for root, dirs, files in os.walk(root_dir):
            work_filse = dirs[:] = [d for d in dirs if not d == file_to_ignore]
        return work_filse
    
    def build(self) -> None:
        files = self.collect_filse()
        for path in tqdm(files):
            try:
                self.chunks += chunk_file(path, self.max_chunks_size) #############################
            except ValueError:   #############3
                print("ERROR in chunk_file")
                continue
        tokens_per_chunk = [tokenize(c) for c in self.chunks]
        self.bm25 = bm25s.BM25()

    def save(self) -> None:
        self.bm25.save()
        

