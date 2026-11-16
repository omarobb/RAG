import argparse
import os
from .indexer import Indexer


class RagCLI:

    def index(self, max_chunk_size: int = 2000) -> None:
        if not isinstance(max_chunk_size, int):
            return
        try:
            if int(max_chunk_size) <= 0 or int(max_chunk_size) > 2000:
                print("ERROR in max chunk size")
                return
        except ValueError as e:
            print(f"ERROR in max chunk size: {e}")
        if not os.path.isdir("data/raw"):
            print("ERROR data/raw does not exists")
            return
        try:
            indexer = Indexer("data/raw", "data/processed", max_chunk_size)
            indexer.build()
            indexer.save()
        except (OSError, ValueError) as e:
            print(f"ERROR: {e}")
            return

        print("Ingestion complete! Indices saved under data/processed/")
    # def search(self, query: str, k: int = 10) -> None: ...
    # def search_dataset(self, dataset_path: str, k: int,
    # save_directory: str) -> None: ...
    # def answer(self, query: str, k: int = 10) -> None: ...
    # def answer_dataset(self, student_search_results_path: str,
    # save_directory: str) -> None: ...
    # def evaluate(self, student_search_results_path: str,
    # dataset_path: str) -> None: ...
