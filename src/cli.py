import argparse
import os
from .indexer import Indexer

# parser = argparse.ArgumentParser(description="Every command is invoked as "
#                                  "uv run python -m src <command> [options]")
# parser.add_argument("-index", "--max_chunk_size", type=int, default=2000,
#                     help="index –max_chunk_size <int>"
#                     "Ingest data/raw/ and build"
#                     " the index under data/processed/")
# parser.add_argument("-search", "--k", type=int,
#                     default=10,
#                     help="search <query> –k <int>"
#                     "Return the top-k sources for a single query.")
# parser.add_argument("-search_dataset", help="search_dataset –dataset_path "
#                     "<path> –k <int> –save_directory <dir>"
#                     "Run search over a whole dataset and write"
#                     " a StudentSearchResults JSON file")
# parser.add_argument("--dataset_path", type=str, required=True)
# parser.add_argument("--k", type=int, default=10, required=True)
# parser.add_argument("--save_directory", type=str, required=True)

# parser.add_argument("-answer", "--k", type=int, default=10,
#                     help="answer <query> –k <int>"
#                     "Answer a single query using the retrieved context.")
# parser.add_argument("-answer_dataset",
#                     help="answer_dataset –student_search_results_path "
#                     "<path> –save_directory <dir>"
#                     "Generate answers for a dataset, producing a "
#                     "StudentSearchResultsAndAnswer JSON file")
# parser.add_argument("--student_search_results_path", type=str, required=True)
# parser.add_argument("--save_directory", type=str, required=True)
# parser.add_argument("-evaluate", help="evaluate –student_search_results_path "
#                     "<path> –dataset_path <path>")
# parser.add_argument("--student_search_results_path", type=str, required=True)
# parser.add_argument("--dataset_path", type=str, required=True)

parser = argparse.ArgumentParser(
    description="Every command is invoked as "
                "uv run python -m src <command> [options]"
)

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

# INDEX
index_parser = subparsers.add_parser(
    "index",
    help="index –max_chunk_size <int>"
         "Ingest data/raw/ and build"
         " the index under data/processed/"
)

index_parser.add_argument(
    "--max_chunk_size",
    type=int,
    default=2000,
    help="Maximum chunk size"
)

# SEARCH
search_parser = subparsers.add_parser(
    "search",
    help="search <query> –k <int>"
         "Return the top-k sources for a single query."
)

search_parser.add_argument(
    "query",
    type=str,
    help="Search query"
)

search_parser.add_argument(
    "--k",
    type=int,
    default=10
)

# SEARCH DATASET
search_dataset_parser = subparsers.add_parser(
    "search_dataset", help="search_dataset –dataset_path "
    "<path> –k <int> –save_directory <dir>"
    "Run search over a whole dataset and write"
    " a StudentSearchResults JSON file")

search_dataset_parser.add_argument(
    "--dataset_path",
    type=str,
    required=True
)

search_dataset_parser.add_argument(
    "--k",
    type=int,
    default=10
)

search_dataset_parser.add_argument(
    "--save_directory",
    type=str,
    required=True
)

# ANSWER
answer_parser = subparsers.add_parser(
    "answer",
    help="answer <query> –k <int>"
    "Answer a single query using the retrieved context."
)

answer_parser.add_argument(
    "query",
    type=str
)

answer_parser.add_argument(
    "--k",
    type=int,
    default=10
)

# ANSWER DATASET
answer_dataset_parser = subparsers.add_parser(
    "answer_dataset",
    help="answer_dataset –student_search_results_path "
         "<path> –save_directory <dir>"
         "Generate answers for a dataset, producing a "
         "StudentSearchResultsAndAnswer JSON file")

answer_dataset_parser.add_argument(
    "--student_search_results_path",
    type=str,
    required=True
)

answer_dataset_parser.add_argument(
    "--save_directory",
    type=str,
    required=True
)

# EVALUATE
evaluate_parser = subparsers.add_parser(
    "evaluate",
    help="evaluate –student_search_results_path "
         "<path> –dataset_path <path>")

evaluate_parser.add_argument(
    "--student_search_results_path",
    type=str,
    required=True
)

evaluate_parser.add_argument(
    "--dataset_path",
    type=str,
    required=True
)

args = parser.parse_args()


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
