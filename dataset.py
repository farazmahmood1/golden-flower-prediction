from typing import List, Tuple

# File to store dataset
DATA_FILE = "dataset.txt"

# Parse dataset from a file
def parse_dataset_from_file(file_path: str) -> List[Tuple[int, str]]:
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        return [(int(line.split()[0]), line.split()[1].strip()) for line in lines]
    except FileNotFoundError:
        # Initialize an empty dataset if file does not exist
        return []

# Write dataset to a file
def write_dataset_to_file(file_path: str, dataset: List[Tuple[int, str]]):
    with open(file_path, "w") as file:
        for entry in dataset:
            file.write(f"{entry[0]} {entry[1]}\n")

# Update dataset in memory and persist it to a file
def update_dataset(dataset: List[Tuple[int, str]], new_outcome: str) -> List[Tuple[int, str]]:
    last_id = dataset[0][0] if dataset else 1321015  # Starting ID if the dataset is empty
    new_id = last_id + 1
    dataset.insert(0, (new_id, new_outcome))  # Add new outcome at the beginning
    write_dataset_to_file(DATA_FILE, dataset)
    return dataset

# Initialize dataset
dataset = parse_dataset_from_file(DATA_FILE)
