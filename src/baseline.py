"""
Baseline Pricing Strategies
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing

Author: Darpana Khaspa
"""

from environment import HotelPricingEnv


class BaselinePricing:
    """
    Implements simple baseline pricing strategies.
    """

    def __init__(self):
        self.env = HotelPricingEnv()
        self.base_price = self.env.base_price

    def fixed_pricing(self):
        """
        Always returns the base price.
        """
        return self.base_price

    def rule_based_pricing(self, demand):
        """
        Adjust price based on demand level.

        High Demand   -> +20%
        Medium Demand -> Base Price
        Low Demand    -> -20%
        """

        if demand >= 0.75:
            return self.base_price * 1.20

        elif demand >= 0.50:
            return self.base_price

        else:
            return self.base_price * 0.80


def demo():

    baseline = BaselinePricing()

    env = HotelPricingEnv()

    state, _ = env.reset()

    print("\n========== Baseline Pricing Demo ==========\n")

    for day in range(10):

        demand = state[2]

        fixed_price = baseline.fixed_pricing()

        rule_price = baseline.rule_based_pricing(demand)

        print(f"Day {day + 1}")

        print(f"Demand Level : {demand:.2f}")

        print(f"Fixed Price  : ₹{fixed_price:.2f}")

        print(f"Rule Price   : ₹{rule_price:.2f}")

        print("-" * 40)

        _, _, terminated, truncated, _ = env.step(2)

        state = env.state

        if terminated or truncated:
            break


if __name__ == "__main__":
    demo()