# main.py
from dataset import dataset, update_dataset
from markov import build_markov_chain, predict_next

def main():
    global dataset
    while True:
        outcomes = [entry[1] for entry in dataset]
        markov_chain = build_markov_chain(outcomes)

        current_state = outcomes[0]  # The most recent outcome
        predicted_next_state = predict_next(current_state, markov_chain)

        print(f"Current state: '{current_state}'")
        print(f"Predicted next state: '{predicted_next_state}'")

        # Input the actual outcome
        new_outcome = input("Enter the actual outcome (A, B, or C): ").strip().upper()
        if new_outcome not in ['A', 'B', 'C']:
            print("Invalid outcome. Please enter 'A', 'B', or 'C'.")
            continue

        # Update dataset
        dataset = update_dataset(dataset, new_outcome)
        print("Dataset updated successfully!")
        print(f"New data: {dataset[0]}")  # Show the latest entry
        print("-" * 50)

if __name__ == "__main__":
    main()
