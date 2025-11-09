⚔️ Python Battle Arena

A turn-based battle simulator built in Python where players create custom warriors, assign them to teams, and watch them fight automatically — with random attacks, healing, and even divine intervention!

Supports:

Free-for-all battles

Team-based battles

Custom player names

Different classes (Warrior, Archer, Mage)

Dynamic logging to battle_log.txt

🧩 Features
🎮 Interactive Setup

Create as many warriors as you want.

Choose between Free-for-All or Team Battle.

Assign each warrior a name, team, and class type:

🛡️ Warrior – Slightly reduced healing but steady attacks.

🏹 Archer – Stronger attack power.

🔮 Mage – Stronger healing and magical attacks.

⚔️ Dynamic Battle Simulation

Each round, random warriors perform actions:

Attack enemies

Heal themselves or allies

Health automatically caps at 100.

Fallen warriors are announced in real time.

✝️ Divine Intervention

At any moment, press Ctrl + C to pause and:

end – Stop the battle early

heal – Heal a warrior manually

attack – Smite a warrior manually

📜 Automatic Battle Log

All events (rounds, actions, and results) are saved to:

battle_log.txt

🧠 Example Gameplay
```
Setup:

⚔️ Welcome to the Python Battle Arena!
Create your warriors (press Ctrl+C when done)

Enter name for Warrior 1: Luke
Enter team (Team 1, Team 2): Team A
Enter type (Warrior, Archer, Mage): Warrior

Enter name for Warrior 2: Zara
Enter team (Team 1, Team 2): Team B
Enter type (Warrior, Archer, Mage): Mage

✅ Warriors have been created:

- Luke (Health: 100, Damage: 20, Team: Team A)
- Zara (Health: 100, Damage: 20, Team: Team B)
```
Battle Sample:
```
⚔️ Round 1
➡️ Luke attacks Zara
Luke attacks Zara for 12 damage!
❤️ Luke Health: 100
❤️ Zara Health: 88
----------------------------------------
➡️ Zara heals
Zara heals for 7 health!
❤️ Luke Health: 100
❤️ Zara Health: 95
----------------------------------------
💀 None have fallen yet!
```
Divine Intervention:
```
✝️ Divine intervention!
1: Luke (Health: 100)
2: Zara (Health: 95)
Do you want to 'end', 'heal', or 'attack'?: heal
Enter target number (1–2) and amount separated by a comma (e.g. '2,20'): 1,15
Luke heals for 15 health!
Divine intervention executed!
```
⚙️ How It Works

Each warrior is an instance of a class derived from the Player base:

`attack()` reduces another player’s health.

`heal()` increases the player’s health.

`Mage`, `Archer`, and `Warrior` modify these effects with multipliers.

Example logic:
```py
enemies = [w for w in alive if w.team != attacker.team and w.health > 0]
```

Ensures a warrior only attacks alive enemies — not teammates or the dead.

🧱 Code Structure
```
battle_arena.py
├── class Player
│   ├── attack()
│   ├── heal()
├── class Warrior(Player)
├── class Archer(Player)
├── class Mage(Player)
├── Battle setup (interactive)
├── Main game loop
│   ├── Random actions
│   ├── Health checks
│   ├── Logging
│   ├── Divine intervention
└── Result output + file logging
```
🧰 Requirements
```
Python 3.8+
```
No external libraries required (uses only random and time)

🚀 How to Run

Clone or download the project.

Open a terminal in the project folder.

Run the script:
```
python battle_arena.py
```

Follow the on-screen prompts to create your warriors and start the battle!

🏆 Win Conditions

The battle continues until only one team (or one player) remains alive.

If everyone dies simultaneously, it’s declared a draw.

The winner is displayed and logged automatically.

📄 Log Example
```
⚔️  Battle Start!

⚔️  Round 1
➡️  Luke attacks Zara
Luke attacks Zara for 17 damage!
❤️  Luke Health: 100
❤️  Zara Health: 83
----------------------------------------
➡️  Zara heals
Zara heals for 5 health!
❤️  Luke Health: 100
❤️  Zara Health: 88
----------------------------------------
🏆 Team A wins!
```
