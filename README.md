<img width="890" height="541" alt="image" src="https://github.com/user-attachments/assets/b80e7bc5-b31f-4f8b-8996-dc159004c2ed" />

  # 🪨 📄 ✂️ THE GAUNTLET: RPS EDITION

  **Can you outsmart the machine, or will you succumb to its random logic?**

  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    <img src="https://img.shields.io/badge/Category-Game_Theory-red?style=for-the-badge" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  </p>

  <h4>
    <a href="#-the-logic">The Logic</a>
    <span> · </span>
    <a href="#-installation">Install</a>
    <span> · </span>
    <a href="#-how-to-play">How to Play</a>
  </h4>
</div>

---

## 📖 Description

**The Gauntlet** is a robust Command Line Interface (CLI) version of the timeless "Rock Paper Scissors" game. Built with Python, it focuses on clean input handling, randomized computer strategy, and a persistent "Round" system that lets you continue your battle until you decide to walk away.

## 🧠 The Logic

The game operates on a triangular win-state logic. If the choices are identical, a **Draw** is declared. Otherwise, the winner is determined by the following cycle:



* **Rock** crushes **Scissors**
* **Scissors** cuts **Paper**
* **Paper** covers **Rock**

## ✨ Features

* **🔢 Multi-Round System:** Define exactly how many rounds you want to play at the start.
* **🤖 Smart Randomization:** Uses the `random.randint` algorithm for unpredictable computer moves.
* **🛡️ Error Handling:** Includes `try-except` blocks to prevent the game from crashing if you enter invalid text.
* **🔄 Continuation Loop:** Option to extend your "misery" or quit while you're ahead after each round.

## 🕹️ How to Play

1.  **Launch the game:** Enter the number of rounds you wish to play.
2.  **Make your move:** Enter the number corresponding to your choice:
    * `1` for **ROCK**
    * `2` for **PAPER**
    * `3` for **SCISSORS**
3.  **Face the outcome:** The computer reveals its move instantly, and the winner of the round is displayed.

## 🛠️ Installation

```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/rock-paper-scissors.git](https://github.com/YOUR_USERNAME/rock-paper-scissors.git)

# Navigate to the folder
cd rock-paper-scissors

# Run the game
python main.py 
```

## 🤝 Contributing
Feel free to fork this project and submit a Pull Request. 

## 📄 License
Distributed under the MIT License. 

<div align="center"> <p><i>"Thou human wish to repeat thy misery again?"</i></p> <sub>Built with ❤️ for the Python Community</sub> </div>
