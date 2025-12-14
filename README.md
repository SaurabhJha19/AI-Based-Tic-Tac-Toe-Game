# 🎮 Tic-Tac-Toe with AI (Console & GUI Versions)

## 📌 Project Overview

This project is a **fully-featured Tic-Tac-Toe game** implemented in Python, available in **two variants**:

1. **Console-based version** (CLI)
2. **Graphical User Interface (GUI) version**

The game supports:
- **Player vs Player (PvP)**
- **Player vs AI (PvAI)**

The AI opponent is implemented using the **Minimax algorithm with Alpha–Beta pruning**, ensuring **optimal play**.

The project is structured following **clean software design principles**, with a clear separation between:
- **Game logic (engine)**
- **User interface (presentation layer)**

---

## 🧠 Key Features

- Optimal AI using Minimax + Alpha-Beta pruning  
- Two gameplay modes: PvP and PvAI  
- Choice of playing as **X or O**  
- Console and GUI implementations  
- Dark-themed, center-aligned GUI  
- Modular, reusable game logic  

---

## 🗂️ Project Structure

```
project/
│
├── game_logic.py        # Core game engine (logic only)
├── gui.py               # Tkinter GUI application
├── console_game.py      # Console-based version (CLI)
└── README.md
```

---

## 🧩 Technology Stack

| Category        | Technology |
|----------------|------------|
| Language        | Python 3 |
| GUI Framework   | Tkinter |
| Algorithms      | Minimax, Alpha–Beta Pruning |
| Architecture    | Modular / Separation of Concerns |
| UI Design       | Custom Tkinter widgets, Canvas |

---

## 📚 Libraries Used

### Standard Python Libraries
- `tkinter` – GUI framework
- `math` – Used in Minimax evaluation
- `tkinter.messagebox` – Game result dialogs

> No third-party libraries are required.  
> The project runs on a **standard Python installation**.

---

## 🎮 Game Variants

### 1️⃣ Console Version (CLI)

The console version is a **terminal-based implementation** that:
- Uses `input()` and `print()` for interaction
- Allows both PvP and PvAI gameplay
- Displays the board using text formatting
- Uses the same AI logic as the GUI version

**Purpose:**
- Algorithm demonstration
- Simplicity
- Debugging and testing logic independently of UI

---

### 2️⃣ GUI Version (Tkinter)

The GUI version is a **desktop application** built using Tkinter and includes:

- Welcome screen
- Mode selection screen
- Symbol selection screen
- Interactive 3×3 game board
- Dark theme UI
- Center-aligned layout
- AI integration with visual feedback

**Design Highlights:**
- Single window with multiple screens (`Frame`-based navigation)
- Event-driven architecture (no infinite loops)
- Custom-styled buttons and layout
- Game logic completely decoupled from UI

---

## 🧠 Algorithms Used

### 🔹 Minimax Algorithm

The **Minimax algorithm** is used to evaluate all possible game states and determine the optimal move for the AI player.

- The AI assumes the opponent plays optimally
- Each move is scored based on win, loss, or draw
- Guarantees best possible outcome for the AI

**Scoring Strategy:**
- AI win → `+1`
- Human win → `-1`
- Draw → `0`

---

### 🔹 Alpha–Beta Pruning

To improve performance, **Alpha–Beta pruning** is applied to the Minimax algorithm.

**Benefits:**
- Eliminates unnecessary branches
- Reduces time complexity
- Enables real-time AI response

---

## 🏗️ Software Design Principles

- **Separation of Concerns**
  - `game_logic.py` contains only logic
  - `gui.py` handles presentation and events

- **Reusability**
  - Same game engine powers both console and GUI versions

- **Scalability**
  - GUI can be replaced (e.g., PyQt, Web UI) without changing logic

- **Maintainability**
  - Clean, readable, modular code structure

---

## 🚀 How to Run

### Run Console Version
```bash
python console_game.py
```

### Run GUI Version
```bash
python gui.py
```

Ensure Python 3 is installed.

---

## 🎯 Future Enhancements

- Difficulty levels (depth-limited Minimax)
- Highlight winning line in GUI
- Restart button & score tracking
- Sound effects and animations
- PyQt or Web-based UI port
- Executable packaging (`.exe`)

---

## 👤 Author

**Saurabh Jha**  
Computer Science | AI & Software Development  

---

## 📄 License

This project is intended for **educational and learning purposes**.  
Feel free to modify, extend, or reuse the code.
