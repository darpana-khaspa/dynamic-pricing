"""
Q-Learning Training
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing
"""

from environment import HotelPricingEnv
from qlearning import QLearningAgent


def train_agent(episodes=5):

    env = HotelPricingEnv()

    agent = QLearningAgent()

    for episode in range(episodes):

        state, _ = env.reset()

        total_reward = 0

        done = False

        while not done:

            action = agent.choose_action(state)

            next_state, reward, terminated, truncated, _ = env.step(action)

            agent.update_q_table(
                state,
                action,
                reward,
                next_state
            )

            state = next_state

            total_reward += reward

            done = terminated or truncated

        print(f"Episode {episode + 1} | Total Reward = {total_reward:.2f}")

    print("\nTraining Completed!")

    print(f"Total States Learned : {len(agent.q_table)}")


if __name__ == "__main__":

    train_agent()