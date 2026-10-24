"""import argparse"""


class RagCLI:

    def index(self, max_chunk_size: int = 2000) -> None:
        try:
            if max_chunk_size <= 0 or max_chunk_size > 2000:
                print("ERROR in max chunk size")
                return
            
        except:
    # def search(self, query: str, k: int = 10) -> None: ...
    # def search_dataset(self, dataset_path: str, k: int,
    # save_directory: str) -> None: ...
    # def answer(self, query: str, k: int = 10) -> None: ...
    # def answer_dataset(self, student_search_results_path: str,
    # save_directory: str) -> None: ...
    # def evaluate(self, student_search_results_path: str,
    # dataset_path: str) -> None: ...
    pass
