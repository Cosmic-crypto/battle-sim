import random
import time

# main player class
class Player:
    def __init__(self, name: str, team: str, health: int = 100, damage: int = 20):
        self.name = name
        self.team = team
        self.health = health
        self.damage = damage

    def attack(self, other: "Player", amount: int):
        other.health -= amount
        print(f"{self.name} ({self.team}) attacks {other.name} ({other.team}) for {amount} damage!")
        return f"{self.name} ({self.team}) attacks {other.name} ({other.team}) for {amount} damage!"

    def heal(self, amount: int):
        self.health += amount
        print(f"{self.name} ({self.team}) heals for {amount} health!")
        return f"{self.name} ({self.team}) heals for {amount} health!"


# --- Subclasses ---
class Warrior(Player):
    def __init__(self, name: str, team: str, health: int = 100, damage: int = 20):
        super().__init__(name, team, health, damage)
        self.heal_modifier = 0.8

    def heal(self, amount: int):
        actual = amount * self.heal_modifier
        self.health += actual
        print(f"{self.name} ({self.team}) heals for {int(actual)} health (reduced healing).")
        return f"{self.name} ({self.team}) heals for {int(actual)} health (reduced healing)."


class Archer(Player):
    def __init__(self, name: str, team: str, health: int = 100, damage: int = 20):
        super().__init__(name, team, health, damage)
        self.attack_modifier = 1.5

    def attack(self, other: "Player", amount: int):
        modified = int(amount * self.attack_modifier)
        other.health -= modified
        print(f"{self.name} ({self.team}) fires an arrow at {other.name} ({other.team}) for {modified} damage!")
        return f"{self.name} ({self.team}) fires an arrow at {other.name} ({other.team}) for {modified} damage!"


class Mage(Player):
    def __init__(self, name: str, team: str, health: int = 100, damage: int = 20):
        super().__init__(name, team, health, damage)
        self.attack_modifier = 1.2
        self.heal_modifier = 1.2

    def attack(self, other: "Player", amount: int):
        modified = int(amount * self.attack_modifier)
        other.health -= modified
        print(f"{self.name} ({self.team}) casts a spell at {other.name} ({other.team}) for {modified} damage!")
        return f"{self.name} ({self.team}) casts a spell at {other.name} ({other.team}) for {modified} damage!"

    def heal(self, amount: int):
        actual = int(amount * self.heal_modifier)
        self.health += actual
        print(f"{self.name} ({self.team}) restores {actual} health with magic.")
        return f"{self.name} ({self.team}) restores {actual} health with magic."


# --- Setup ---
print("\n⚔️ Welcome to the Python Battle Arena!")
print("Create your warriors (press Ctrl+C when done)\n")

num = 1
warriors = []

while True:
    try:
        name = input(f"Enter name for Warrior {num}: ").strip()
        team = random.choice(["Team 1", "Team 2"])
        typ = random.choice(["warrior", "archer", "mage"])
        print()

        if typ == "warrior":
            warriors.append(Warrior(name, team))
        elif typ == "archer":
            warriors.append(Archer(name, team))
        elif typ == "mage":
            warriors.append(Mage(name, team))

        num += 1

    except KeyboardInterrupt:
        if len(warriors) >= 2:
            print("\n✅ Warriors created:")
            for w in warriors:
                print(f"- {w.name} ({w.team}) | ❤️ {w.health} | ⚔️ {w.damage}")
            break
        else:
            print("\n⚠️ Not enough warriors to start a battle.")
            exit()

# --- Battle Loop ---
round_num = 1
filename = "battle_log.txt"

with open(filename, "w") as log_file:
    log_file.write("⚔️ Battle Start!\n\n")

    while True:
        alive = [w for w in warriors if w.health > 0]
        alive_teams = set(w.team for w in alive)

        if len(alive_teams) <= 1:
            break

        print(f"\n⚔️ Round {round_num}")
        log_file.write(f"\n⚔️ Round {round_num}\n")
        round_num += 1

        for _ in range(len(alive)//2):
            attacker = random.choice(alive)
            # only attack enemies
            enemies = [w for w in alive if w.team != attacker.team and w.health > 0]
            if not enemies:
                continue
            defender = random.choice(enemies)

            action = random.choice(["attack", "heal"])
            if action == "attack":
                result = attacker.attack(defender, random.randint(5, attacker.damage))
            else:
                result = attacker.heal(random.randint(5, 15))

            log_file.write(result + "\n")

        # Update and print health
        for w in warriors:
            w.health = min(max(w.health, 0), 100)
            print(f"❤️ {w.name} ({w.team}) — {w.health} HP")
            log_file.write(f"❤️ {w.name} ({w.team}) — {w.health} HP\n")

        # Fallen warriors
        for w in warriors:
            if w.health <= 0:
                print(f"💀 {w.name} ({w.team}) has fallen!")
                log_file.write(f"💀 {w.name} ({w.team}) has fallen!\n")

        log_file.write("-" * 40 + "\n")
        time.sleep(1)

    # --- Result ---
    alive = [w for w in warriors if w.health > 0]
    if len(alive) == 0:
        result_text = "\n🤝 It's a draw!"
    else:
        winning_team = alive[0].team
        result_text = f"\n🏆 Team {winning_team} wins the battle!"

    print(result_text)
    log_file.write(result_text + "\n")
