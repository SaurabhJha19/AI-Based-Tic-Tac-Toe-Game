# 🎮 Tic-Tac-Toe with AI (Console & GUI Versions)

## Project Description (Paragraph Style)

This project is a Python-based implementation of the classic Tic-Tac-Toe game, developed in both console and graphical user interface (GUI) variants, with support for Player vs Player (PvP) and Player vs Artificial Intelligence (PvAI) gameplay. The core game logic is implemented as a standalone engine using the Minimax algorithm enhanced with Alpha–Beta pruning, enabling the AI to make optimal decisions while maintaining efficient performance. The application follows clean software design principles by separating the game logic from the presentation layer. The GUI is built using Tkinter and features a modern dark-themed, center-aligned interface with intuitive navigation screens for mode selection, symbol selection, and gameplay.

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
├── Game_Logic.py        # Core game engine (logic only)
├── GUI.py               # Tkinter GUI application
├── main.py              # Console-based version (CLI)
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
  - `Game_Logic.py` contains only logic
  - `GUI.py` handles presentation and events
  - `main.py ` contains CLI version

- **Scalability**
  - GUI can be replaced (e.g., PyQt, Web UI) without changing logic

- **Maintainability**
  - Clean, readable, modular code structure

---

## 🚀 How to Run

### Run Console Version
```bash
python main.py
```

### Run GUI Version
```bash
python GUI.py
```

Ensure Python 3 is installed.

---

## 👤 Author

**Saurabh Jha**  

---
