# Python Mini Projects 🐍

Short and sweet Python Mini Projects for beginners. This repository contains a collection of simple scripts and a Jupyter Notebook to practice core Python concepts.

## 📂 Projects

### 1. ⚡ Quick Automations (`Quick Automations in Python.ipynb`)
A Jupyter Notebook containing 5 useful automation scripts:
- **Date & Time**: Displays the current system timestamp.
- **Password Generator**: Creates random passwords.
- **Text-to-Speech**: Converts text input to an audio file using `gTTS`.
- **To-Do List Manager**: Creates a CSV file with your daily tasks.
- **RAM Checker**: Monitors system memory usage (Total, Available, Used).

### 2. ✂️ Rock Paper Scissors (`rock_paper_scissor.py`)
A classic implementation of the Rock, Paper, Scissors game.
- Play against the computer.
- Tracks wins for both the user and the computer.
- Handles invalid inputs and ties correctly.

### 3. 🔢 Number Guessing Game (`number_guessing.py`)
A simple game where the computer generates a random number, and you have to guess it.
- Provides feedback if your guess is too high or too low.
- Tracks how many guesses it took you to win.

### 4. 🔐 Password Generator (`password_generator.py`)
A utility to generate strong, random passwords.
- Specify how many passwords you need.
- Generates 8-character passwords using letters, numbers, and punctuation.

### 5. 🛡️ Password Manager (`password_manager.py`)
A secure tool to store and retrieve your passwords.
- **Security Check**: Generates an encryption key (`key.key`) if one doesn't exist.
- **Add Passwords**: Save site name, username, and password (encrypted).
- **View Passwords**: Decrypts and shows your saved credentials.
- *Note: Requires the `cryptography` library.*

## 🚀 How to Run
Make sure you have Python installed. Some scripts require additional libraries.

### Install Dependencies
```bash
pip install cryptography pandas psutil gTTS ipython
```

### Run a Script
```bash
python rock_paper_scissor.py
```

### Run the Notebook
To run the automations notebook, you need Jupyter:
```bash
pip install notebook
jupyter notebook "Quick Automations in Python.ipynb"
```
