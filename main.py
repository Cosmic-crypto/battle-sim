import random
import time

class Player:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

    def attack(self, other):
        other.health -= self.damage
        print(f"{self.name} attacks {other.name} for {self.damage} damage!")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} health!")


# Create two warriors
warrior1 = Player("Warrior 1", 100, 15, 10)
warrior2 = Player("Warrior 2", 100, 15, 10)

# Game loop
round_num = 1
while warrior1.health > 0 and warrior2.health > 0:
    print(f"\n⚔️  Round {round_num}")
    round_num += 1

    # Define possible actions with both the function and the description
    actions = [
        (lambda: warrior1.attack(warrior2), "Warrior 1 attacks Warrior 2"),
        (lambda: warrior2.attack(warrior1), "Warrior 2 attacks Warrior 1"),
        (lambda: warrior1.heal(10), "Warrior 1 heals"),
        (lambda: warrior2.heal(10), "Warrior 2 heals")
    ]

    # Choose a random action
    action_func, description = random.choice(actions)

    # Print what’s happening
    print(f"➡️  {description}")

    # Execute the chosen action
    action_func()

    # Show health after action
    print(f"❤️  Warrior 1 Health: {warrior1.health}")
    print(f"❤️  Warrior 2 Health: {warrior2.health}")
    print("-" * 40)

    time.sleep(1)

# End result
if warrior1.health <= 0 and warrior2.health <= 0:
    print("\n🤝 It's a draw!")
elif warrior1.health <= 0:
    print("\n🏆 Warrior 2 wins!")
else:
    print("\n🏆 Warrior 1 wins!")
