# 01 - Turtle Graphics Sandbox

A simple experimentation script created to explore the basic capabilities of the **Python Turtle** library.

## 📌 Overview
This script serves as a learning playground to test various graphic commands, including:
*   **Coordinate Movement:** Using `goto()`, `home()`, `setx()`, and `sety()`.
*   **Shapes & Fills:** Drawing triangles, squares, and circles using `begin_fill()` and `end_fill()`.
*   **Drawing Logic:** Implementing `for` loops and `while` loops to generate geometric patterns and expanding circles.
*   **Styling:** Adjusting `shapesize`, `pensize`, and manipulating colors.


# 02 - Turtle Race: The Dice Challenge

**Turtle Race** is a local multiplayer board-game style racing simulator built with **Python's Turtle Graphics**. Instead of a continuous race, this project implements a **turn-based mechanic** using a virtual 6-sided dice to determine movement.

## Game Mechanics
*   **Turn-Based Racing:** Two players (Green vs. Blue) take turns rolling a die.
*   **Dynamic HUD:** Each racer has an independent "writer" turtle that displays the last dice roll and the exact units remaining to reach the goal.
*   **Visual Feedback:** The game draws a physical goal line (circular target) and leaves a trail (pen down) to track the progress of each racer.
*   **Class-Based Design:** Every racer is an instance of a `Racer` class, managing its own graphics, stats, and text updates.

---

## How it Works
The game follows a simple yet effective logic loop:
1.  **Input Trigger:** The game waits for a user to press `Enter` in the console to roll the die for the current player.
2.  **Dice Logic:** A random value between 1 and 6 is chosen.
3.  **Distance Calculation:** The turtle moves forward by `dice_roll * 20` units.
4.  **Win Condition:** The first turtle to have an X-coordinate greater than or equal to the `GOAL_LINE` (200 units) is declared the winner.

---

## Technical Implementation
*   **Object-Oriented Programming (OOP):** Encapsulation of turtle properties and movement methods within the `Racer` class.
*   **Type Hinting:** Use of Python type hints (`color: str`, `-> bool`) for cleaner and more professional code.
*   **Real-time Calculations:** Mathematical subtraction of coordinates to provide live "Missing units" feedback.
*   **Turtle Composition:** Using one turtle for the sprite and another hidden turtle (`self.writer`) to handle text rendering without interfering with the movement trail.

---

## Installation & Play

### Prerequisites
*   Python 3.x
*   A GUI-enabled environment (standard desktop OS).

### Running the Race
```bash
python main.py
```

# 03 - Multi-Flavor Snake: A POO Turtle Adventure

**Multi-Flavor Snake** is an advanced take on the classic arcade game, built with **Python's Turtle graphics**. This version implements a robust Object-Oriented Programming (OOP) structure, featuring different types of food that affect the game's physics and speed in real-time.


##  Key Features
*   **Dynamic Speed System:** The game's difficulty doesn't just increase; it fluctuates based on what you eat.
*   **OOP Architecture:** Clean implementation of classes for the Snake, Food (with inheritance), and Score management.
*   **Power-Up Mechanics:** Strategic spawning of special food types that can either help you recover or challenge your reflexes.
*   **Audio Feedback:** Integrated sound effects for eating and game-over events using `winsound`.

---

## The Menu: Food Variants
Each food type has a unique impact on your score and the game's `delay` (speed):

| Food Type | Appearance | Points | Effect |
| :--- | :--- | :--- | :--- |
| **Normal** | Orange Square | +10 | Slightly increases speed. |
| **Slow Down** | Blue Triangle | +5 | **Power-Up:** Significantly slows down the snake (Easy mode). |
| **Fast Forward** | Red Circle | +20 | **Challenge:** Greatly increases speed for high-risk rewards. |



---

## 🛠️ Technical Insights
This project demonstrates advanced usage of the `turtle` module and Python logic:
*   **Inheritance:** A base `Food` class is extended by `NormalFood`, `SlowFood`, and `FastFood` to reuse code efficiently.
*   **Tracer Control:** Uses `screen.tracer(0)` and `screen.update()` to eliminate flickering and provide smooth 60fps-like movement.
*   **Collision Engine:** Custom logic for boundary detection, self-collision, and distance-based consumption.

---

## 🚀 Installation & Gameplay

### Requirements
*   Python 3.x
*   Windows OS (for `winsound` support)

### How to Play - Controls
* Up Arrow: Move Up
* Down Arrow: Move Down
* Left Arrow: Move Left
* Right Arrow: Move Right

Note: The snake cannot turn 180 degrees directly (e.g., if moving Up, Down is disabled) to prevent self-collision.

```bash
python main.py
```

# 04 - Space Ship: Score Survival

**Space Ship** is a fast-paced arcade shooter developed in **Python** using the **Pygame** library. In this mission, you must eliminate waves of UFO invaders where your performance is your only lifeline.

## 🕹️ Unique Mechanic: "Score as HP"
Unlike traditional games with health bars, here **your Score acts as your Hit Points (HP)**.
*   **Destroy Enemies:** Increases your energy (points).
*   **Taking Damage:** Drastically drains your energy.
*   **The Stakes:** If your score reaches zero, it's Game Over! You must play aggressively to survive while protecting your accumulated record.

---

## Enemy Variety
The space sector is infested with different types of UFOs, each with unique behaviors powered by a **Dynamic Tinting System**:

| Enemy Type | Color | Behavior |
| :--- | :--- | :--- |
| **Scout** | Blue | Erratic movement. Does not shoot, but physical collision drains points. |
| **Gunner X** | Green | Fires high-speed horizontal lasers (X-axis). |
| **Destroyer Y** | Red | Dual vertical fire (Y-axis), shooting both up and down. |

---

## Controls
*   **Arrows:** Move the ship.
*   **Spacebar:** Fire lasers.
*   **R:** Retry (during Game Over).
*   **Q:** Quit game.

---

## Tech Stack & Optimization
*   **Language:** Python 3.x
*   **Library:** [Pygame](https://www.pygame.org/)
*   **OOP Architecture:** Efficient use of Classes and Sprite Groups for collision handling and memory management.
*   **Real-time Post-processing:** 
    *   **Dynamic Colorizing:** Using `BLEND_RGBA_MULT` to generate multiple enemy types from a single base asset.
    *   **Blur Effect:** Implementation of a real-time Gaussian-style blur for the Game Over screen using surface scaling.
    *   **Resource Caching:** Optimized font and sound loading to prevent frame drops.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python and Pygame installed:
```bash
pip install pygame
python index.py
