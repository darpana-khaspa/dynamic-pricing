"""
Model Evaluation
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing
"""

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

    print("\nEvaluation Completed!")
    print(f"Average Reward: {sum(rewards)/len(rewards):.2f}")


if __name__ == "__main__":

    evaluate_agent()