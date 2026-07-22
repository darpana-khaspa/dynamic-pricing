"""
Q-Learning Agent
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing
"""

import numpy as np


class QLearningAgent:
    """
    Basic Q-Learning Agent
    """

    def __init__(
        self,
        state_size=3,
        action_size=5,
        learning_rate=0.1,
        discount_factor=0.95,
        epsilon=1.0,
        epsilon_decay=0.95,
        min_epsilon=0.1,
    ):

        self.state_size = state_size
        self.action_size = action_size

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon

        self.training_steps = 0

        # Q-table
        self.q_table = {}

    def get_q_values(self, state):
        """
        Return Q-values for a given state.
        """

        state = tuple(state.astype(int))

        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.action_size)

        return self.q_table[state]

    def choose_action(self, state):
        """
        Epsilon-Greedy Action Selection
        """

        if np.random.random() < self.epsilon:
            return np.random.randint(self.action_size)

        return np.argmax(self.get_q_values(state))

    def update_q_table(self, state, action, reward, next_state):
        """
        Update the Q-table using the Q-Learning equation.
        """

        state = tuple(state.astype(int))
        next_state = tuple(next_state.astype(int))

        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.action_size)

        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(self.action_size)

        current_q = self.q_table[state][action]

        max_future_q = np.max(self.q_table[next_state])

        updated_q = current_q + self.learning_rate * (
            reward
            + self.discount_factor * max_future_q
            - current_q
        )

        self.q_table[state][action] = updated_q
        self.training_steps += 1

    def decay_epsilon(self):
        """
        Reduce exploration after every episode.
        """

        self.epsilon = max(
            self.min_epsilon,
            self.epsilon * self.epsilon_decay
        )

    def get_training_statistics(self):
        """
        Return current learning statistics.
        """

        return {
            "epsilon": self.epsilon,
            "training_steps": self.training_steps,
            "states_learned": len(self.q_table)
        }


if __name__ == "__main__":

    agent = QLearningAgent()

    state = np.array([100, 30, 1])
    next_state = np.array([95, 29, 1])

    action = agent.choose_action(state)

    reward = 5000

    agent.update_q_table(
        state,
        action,
        reward,
        next_state
    )

    print("Current State :", state)
    print("Next State    :", next_state)
    print("Action        :", action)
    print("Reward        :", reward)
    print("\nUpdated Q-values:")
    print(agent.get_q_values(state))

    print("\nTraining Statistics:")
    print(agent.get_training_statistics())