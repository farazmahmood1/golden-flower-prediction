# markov.py
from collections import defaultdict
from typing import List, Dict

# Build Markov Chain
def build_markov_chain(outcomes: List[str]) -> Dict[str, Dict[str, float]]:
    markov_chain = defaultdict(lambda: defaultdict(int))
    for i in range(len(outcomes) - 1):
        current_state = outcomes[i]
        next_state = outcomes[i + 1]
        markov_chain[current_state][next_state] += 1
    # Normalize probabilities
    for state, transitions in markov_chain.items():
        total = sum(transitions.values())
        for next_state in transitions:
            markov_chain[state][next_state] /= total
    return markov_chain

# Predict next state
def predict_next(current_state: str, markov_chain: Dict[str, Dict[str, float]]) -> str:
    if current_state in markov_chain:
        next_states = markov_chain[current_state]
        return max(next_states, key=next_states.get)  # Most probable next state
    return None  # No prediction possible
