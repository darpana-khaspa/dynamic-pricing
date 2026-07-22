"""
Q-Learning Training
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing
"""

from environment import HotelPricingEnv
from qlearning import QLearningAgent


def train_agent(episodes=5):

    env = HotelPricingEnv()

    agent = QLearningAgent()

    reward_history = []
    training_results = []

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

        reward_history.append(total_reward)

        training_results.append(
            f"Episode {episode + 1}: Reward = {total_reward:.2f}"
        )

        print(f"Episode {episode + 1} | Total Reward = {total_reward:.2f}")

        # Epsilon Decay
        agent.decay_epsilon()

    print("\nTraining Completed!")

    stats = agent.get_training_statistics()

    print(f"Total States Learned : {stats['states_learned']}")
    print(f"Training Steps : {stats['training_steps']}")
    print(f"Final Epsilon : {agent.epsilon:.3f}")
    print(f"Average Reward : {sum(reward_history) / len(reward_history):.2f}")

    with open("results/training_results.txt", "w") as file:

        file.write("Q-Learning Training Results\n")
        file.write("=" * 35 + "\n\n")

        for line in training_results:
            file.write(line + "\n")

        file.write("\n")
        file.write(f"Average Reward : {sum(reward_history) / len(reward_history):.2f}\n")
        file.write(f"Final Epsilon : {agent.epsilon:.3f}\n")

    print("Training results saved to results/training_results.txt")


if __name__ == "__main__":

    train_agent()