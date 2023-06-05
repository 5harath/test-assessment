import random

def simulate_event(outcomes):
    total_probability = sum(outcome[1] for outcome in outcomes)
    normalized_probabilities = [(outcome[0], outcome[1] / total_probability) for outcome in outcomes]

    event_results = []
    for _ in range(1000):  # Simulating 1000 occurrences of the event
        rand_num = random.uniform(0, 1)  # Generate a random number between 0 and 1
        cumulative_prob = 0
        for outcome in normalized_probabilities:
            cumulative_prob += outcome[1]
            if rand_num <= cumulative_prob:
                event_results.append(outcome[0])
                break

    result_distribution = {}
    for outcome in outcomes:
        result_distribution[outcome[0]] = event_results.count(outcome[0])

    return result_distribution

# Example usage
dice_outcomes = [(1, 10), (2, 30), (3, 15), (4, 15), (5, 30), (6, 0)]
coin_outcomes = [("Head", 35), ("Tail", 65)]

print(simulate_event(dice_outcomes))
print(simulate_event(coin_outcomes))
