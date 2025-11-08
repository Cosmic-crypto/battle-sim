🥷 Battle Simulator
A simple Python text-based battle simulation between two warriors.
Each round, a random action occurs — either an attack or a heal — until one (or both) warriors fall.

⚔️ Features


Two warriors fight in turn-based style


Randomized actions each round (attack or heal)


Real-time updates with health tracking


Automatic victory/draw detection


Easy to extend with new actions (like critical hits or defense)



🧩 How It Works
Each round:


A random action (attack or heal) is chosen.


The chosen action prints a short description.


The corresponding function runs — adjusting health.


The current health of both warriors is displayed.


The loop repeats until one or both warriors reach 0 health.


Example output:
```
⚔️  Round 3
➡️  Warrior 2 attacks Warrior 1
Warrior 2 attacks Warrior 1 for 15 damage!
❤️  Warrior 1 Health: 70
❤️  Warrior 2 Health: 90
----------------------------------------
```

🧠 Code Overview
```
# Create warriors
warrior1 = Player("Warrior 1", 100, 15, 10)
warrior2 = Player("Warrior 2", 100, 15, 10)

# Define possible actions
actions = [
    (lambda: warrior1.attack(warrior2), "Warrior 1 attacks Warrior 2"),
    (lambda: warrior2.attack(warrior1), "Warrior 2 attacks Warrior 1"),
    (lambda: warrior1.heal(10), "Warrior 1 heals"),
    (lambda: warrior2.heal(10), "Warrior 2 heals")
]

# Pick a random tuple (function, description)
action_func, description = random.choice(actions)
print(description)
action_func()
```
Each lambda stores a callable action that doesn’t run until selected, so actions can be randomized without being pre-executed.

🏃 How to Run


Make sure you have Python 3.7+ installed.


Save the script as `battle_simulator.py`.


Open a terminal in the script’s directory.


Run:
```
python battle_simulator.py

```


🛠️ Future Ideas


Add random damage variation (random.randint)


Add critical hits or misses


Add defense or armor stats


Add more than two players


Turn it into a GUI or web game



👨‍💻 Author
Made by you — with help from ChatGPT 🤖
A fun little Python project to practice OOP, randomness, and game loops.
