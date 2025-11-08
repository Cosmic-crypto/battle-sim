import random
import time

class Player:
    def __init__(self, name: str, health: int = 100, damage: int = 20):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, other: "Player", amount: int):
        other.health -= amount
        print(f"{self.name} attacks {other.name} for {amount} damage!")
        return f"{self.name} attacks {other.name} for {amount} damage!"

    def heal(self, amount: int):
        self.health += amount
        print(f"{self.name} heals for {amount} health!")
        return f"{self.name} heals for {amount} health!"


print("\n⚔️ Welcome to the Python Battle Arena!")
print("Create your warriors (press Ctrl+C when done)\n")

num = 1
warriors = []

# Create warriors
while True:
    try:
        name = input(f"Enter name for Warrior {num}: ").strip()
        health = 100
        damage = 20
        print()
        warriors.append(Player(name, health, damage))
        num += 1

    except KeyboardInterrupt:
        if len(warriors) >= 2:
            print("\n✅ Warriors have been created:")
            for warrior in warriors:
                print(f"- {warrior.name} (Health: {warrior.health}, Damage: {warrior.damage})")
            break
        else:
            print("\n⚠️ Battle was stopped before enough warriors were created.")
            exit()

# Game loop
round_num = 1
filename = "battle_log.txt"

try:
    with open(filename, "w") as log_file:
        log_file.write("⚔️  Battle Start!\n\n")

        while sum(w.health > 0 for w in warriors) > 1:
            try:
                print(f"\n⚔️  Round {round_num}")
                log_file.write(f"\n⚔️  Round {round_num}\n")
                round_num += 1

                alive_warriors = [w for w in warriors if w.health > 0]
                if len(alive_warriors) < 2:
                    break

                for _ in range(len(warriors)//2):  # allows half the alive people to act per round
                    attacker, defender = random.sample(alive_warriors, 2)

                    actions = [
                        (lambda: attacker.attack(defender, random.randint(1, attacker.damage)), f"{attacker.name} attacks {defender.name}"),
                        (lambda: attacker.heal(random.randint(1, 10)), f"{attacker.name} heals"),
                        (lambda: defender.heal(random.randint(1, 10)), f"{defender.name} heals"),
                    ]

                    action_func, description = random.choice(actions)
                    print(f"➡️  {description}")
                    log_file.write(f"➡️  {description}\n")

                    result = action_func()
                    if result:
                        log_file.write(result + "\n")

                # Cap health
                for w in warriors:
                    w.health = min(max(w.health, 0), 100)

                for w in warriors:
                    print(f"❤️  {w.name} Health: {w.health}")
                    log_file.write(f"❤️  {w.name} Health: {w.health}\n")

                # Show fallen warriors
                for w in warriors:
                    if w.health <= 0:
                        print(f"💀 {w.name} has fallen!")
                        log_file.write(f"💀 {w.name} has fallen!\n")

                log_file.write("-" * 40 + "\n")
                time.sleep(1)

            except KeyboardInterrupt:
                print("\n✝️ Divine intervention!")
                players = {str(i): w for i, w in enumerate(warriors, start=1)}

                for idx, w in players.items():
                    print(f"{idx}: {w.name} (Health: {w.health})")

                choice = input("Do you want to 'end', 'heal', or 'attack'?: ").lower().strip()

                if choice in ("end", "break", "quit", "exit", "stop"):
                    print("Divine intervention! The battle ends prematurely.")
                    break

                elif choice in ("heal", "attack"):
                    while True:
                        target = input(f"Enter target number (1–{len(warriors)}) and amount separated by a comma (e.g. '3,20'): ").strip().split(",")
                        if target[0] in players and len(target) == 2:
                            player = players[target[0]]
                            amount = int(target[1])

                            if choice == "heal":
                                if player.health <= 0:
                                    print(f"{player.name} has come back to life!")
                                player.heal(amount)
                                print(f"Divine intervention executed! {player.name} healed for {amount} health.")
                            else:
                                other = random.choice([w for w in warriors if w != player and w.health > 0])
                                other.attack(player, amount)
                            player.health = min(max(player.health, 0), 100)
                            break
                        else:
                            print("Invalid input. Try again.")

        alive = [w for w in warriors if w.health > 0]
        if len(alive) == 0:
            result_text = "\n🤝 It's a draw!"
        elif len(alive) == 1:
            result_text = f"\n🏆 {alive[0].name} wins!"
        else:
            survivors = ", ".join(w.name for w in alive)
            result_text = f"\n⚔️ The battle ends in chaos — multiple survivors remain: {survivors}"

        print(result_text)
        log_file.write(result_text + "\n")

except FileNotFoundError:
    print("The paper to write the battle log could not be found!")

except Exception as e:
    print("\nAn unexpected interruption occurred. The battle ends abruptly.")
    print(f"Interruption details: {e}")
