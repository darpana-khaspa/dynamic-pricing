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
    ):

        self.state_size = state_size
        self.action_size = action_size

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon

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


if __name__ == "__main__":

    agent = QLearningAgent()

    sample_state = np.array([100, 30, 1])

    action = agent.choose_action(sample_state)

    print("Sample State :", sample_state)
    print("Selected Action :", action)