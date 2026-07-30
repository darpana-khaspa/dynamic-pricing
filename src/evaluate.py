"""
Model Evaluation
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing
"""

import os

from environment import HotelPricingEnv
from qlearning import QLearningAgent


def evaluate_agent(episodes=3):

    env = HotelPricingEnv()

    agent = QLearningAgent()

    # Use the learned policy (no exploration)
    agent.epsilon = 0

    rewards = []

    for episode in range(episodes):

        state, _ = env.reset()

        total_reward = 0

        done = False

        while not done:

            action = agent.choose_action(state)

            next_state, reward, terminated, truncated, _ = env.step(action)

            state = next_state

            total_reward += reward

            done = terminated or truncated

        rewards.append(total_reward)

        print(f"Evaluation Episode {episode + 1}: Reward = {total_reward:.2f}")

    average_reward = sum(rewards) / len(rewards)
    best_reward = max(rewards)
    worst_reward = min(rewards)

    print("\nEvaluation Completed!")
    print(f"Average Reward : {average_reward:.2f}")
    print(f"Best Reward    : {best_reward:.2f}")
    print(f"Worst Reward   : {worst_reward:.2f}")

    os.makedirs("results", exist_ok=True)

    with open("results/evaluation_report.txt", "w") as file:
        file.write("Q-Learning Evaluation Report\n")
        file.write("=" * 35 + "\n\n")
        file.write(f"Evaluation Episodes : {len(rewards)}\n")
        file.write(f"Average Reward      : {average_reward:.2f}\n")
        file.write(f"Best Reward         : {best_reward:.2f}\n")
        file.write(f"Worst Reward        : {worst_reward:.2f}\n")

    print("Evaluation report saved to results/evaluation_report.txt")


if __name__ == "__main__":
    evaluate_agent()