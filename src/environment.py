"""
Custom Gymnasium Environment
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing

Author: Darpana Khaspa
Ch Srimani Deepika Krishna
"""

import gymnasium as gym
from gymnasium import spaces
import numpy as np


class HotelPricingEnv(gym.Env):
    """
    Hotel Dynamic Pricing Environment
    """

    metadata = {"render_modes": ["human"]}

    def __init__(self):

        super().__init__()

        # -----------------------------
        # Hotel Configuration
        # -----------------------------

        self.total_rooms = 100
        self.base_price = 5000
        self.booking_window = 30

        # Current State Variables

        self.remaining_rooms = self.total_rooms
        self.days_remaining = self.booking_window
        self.demand = 0.5

        # -----------------------------
        # Action Space
        # -----------------------------
        #
        # 0 -> -20%
        # 1 -> -10%
        # 2 -> No Change
        # 3 -> +10%
        # 4 -> +20%
        #

        self.action_space = spaces.Discrete(5)

        # -----------------------------
        # Observation Space
        # -----------------------------
        #
        # Remaining Rooms
        # Days Remaining
        # Demand Level
        #

        self.observation_space = spaces.Box(
            low=np.array([0, 0, 0.0], dtype=np.float32),
            high=np.array(
                [
                    self.total_rooms,
                    self.booking_window,
                    1.0
                ],
                dtype=np.float32
            ),
            dtype=np.float32
        )

        self.state = np.array(
            [
                self.remaining_rooms,
                self.days_remaining,
                self.demand
            ],
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):
        """
        Reset the environment to its initial state.
        """

        super().reset(seed=seed)

        self.remaining_rooms = self.total_rooms
        self.days_remaining = self.booking_window
        self.demand = np.random.uniform(0.3, 0.9)

        self.state = np.array(
            [
                self.remaining_rooms,
                self.days_remaining,
                self.demand
            ],
            dtype=np.float32
        )

        return self.state, {}

    def step(self, action):
        """
        Execute one pricing action.
        """

        # -----------------------------
        # Price Multiplier
        # -----------------------------

        price_changes = {
            0: 0.80,
            1: 0.90,
            2: 1.00,
            3: 1.10,
            4: 1.20
        }

        multiplier = price_changes[action]
        current_price = self.base_price * multiplier
        # Ensure the recommended price remains within a safe range
        min_price = self.base_price * 0.80
        max_price = self.base_price * 1.20
        current_price = np.clip(current_price, min_price, max_price)

        # -----------------------------
        # Demand Simulation
        # -----------------------------

        base_probability = self.demand

        purchase_probability = np.clip(
            base_probability - (multiplier - 1.0) * 0.5,
            0.05,
            0.95
        )

        expected_customers = max(1, int(np.random.randint(5, 16) * self.demand))

        bookings = 0

        for _ in range(expected_customers):
            if np.random.random() < purchase_probability:
                bookings += 1

        bookings = min(bookings, self.remaining_rooms)

        revenue = bookings * current_price

        self.remaining_rooms -= bookings
        self.days_remaining -= 1

        # Random demand for next day
        self.demand = np.random.uniform(0.3, 0.9)

        # -----------------------------
        # Reward Function
        # -----------------------------

        reward = revenue

        if self.remaining_rooms > 0 and self.days_remaining == 0:
            reward -= self.remaining_rooms * 1000

        if multiplier > 1.15 and bookings == 0:
            reward -= 5000

        terminated = (
            self.remaining_rooms == 0
            or
            self.days_remaining == 0
        )

        truncated = False

        self.state = np.array(
            [
                self.remaining_rooms,
                self.days_remaining,
                self.demand
            ],
            dtype=np.float32
        )

        info = {
            "price": current_price,
            "bookings": bookings,
            "revenue": revenue,
            "remaining_rooms": self.remaining_rooms,
            "days_remaining": self.days_remaining
        }

        return (
            self.state,
            reward,
            terminated,
            truncated,
            info
        )
    
    def render(self):
        """
        Display the current environment state.
        """

        print("\n========== Hotel Pricing Environment ==========")
        print(f"Remaining Rooms : {self.remaining_rooms}")
        print(f"Days Remaining  : {self.days_remaining}")
        print(f"Demand Level    : {self.demand:.2f}")
        print("===============================================\n")

    def close(self):
        """
        Close the environment.
        """
        pass


if __name__ == "__main__":

    env = HotelPricingEnv()

    state, info = env.reset()

    print("Initial State:", state)

    done = False

    while not done:

        action = env.action_space.sample()

        state, reward, terminated, truncated, info = env.step(action)

        env.render()

        action_names = {
            0: "Decrease 20%",
            1: "Decrease 10%",
            2: "No Change",
            3: "Increase 10%",
            4: "Increase 20%"
        }

        print(f"Action Taken : {action}")
        print(f"Price        : ₹{info['price']:.2f}")
        print(f"Bookings     : {info['bookings']}")
        print(f"Revenue      : ₹{info['revenue']:.2f}")
        print(f"Reward       : {reward:.2f}")
        print("-" * 50)

        done = terminated or truncated

    print("\nSimulation Finished!")

    env.close()
