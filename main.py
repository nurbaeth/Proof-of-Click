import time
import random

class CryptoClicker:
    def __init__(self):
        self.coins = 0
        self.mining_power = 1
        self.auto_mining = 0

    def click(self):
        self.coins += self.mining_power
        print(f"You mined {self.mining_power} coins! Total: {self.coins}")

    def upgrade_mining(self):
        cost = 10 * self.mining_power
        if self.coins >= cost:
            self.coins -= cost
            self.mining_power += 1
            print(f"Mining power increased! Now: {self.mining_power} per click.")
        else:
            print(f"Not enough coins! Need {cost}.")

    def buy_auto_miner(self):
        cost = 50 * (self.auto_mining + 1)
        if self.coins >= cost:
            self.coins -= cost
            self.auto_mining += 1
            print(f"Auto-miner bought! Producing {self.auto_mining} coins per second.")
        else:
            print(f"Not enough coins! Need {cost}.")

    def auto_mine(self):
        while True:
            if self.auto_mining > 0:
                self.coins += self.auto_mining
                print(f"Auto-mined {self.auto_mining} coins! Total: {self.coins}")
            time.sleep(1)

    def run(self):
        print("Welcome to Crypto Clicker! Type 'click', 'upgrade', 'buy' or 'exit'")
        while True:
            command = input("Command: ").strip().lower()
            if command == "click":
                self.click()
            elif command == "upgrade":
                self.upgrade_mining()
            elif command == "buy":
                self.buy_auto_miner()
            elif command == "exit":
                print("Thanks for playing!")
                break
            else:
                print("Unknown command! Use 'click', 'upgrade', 'buy', or 'exit'.")

if __name__ == "__main__":
    game = CryptoClicker()
    game.run()
