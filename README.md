# Sustainability Game

## Overview
The **Sustainability Game** is an interactive web-based game designed to promote eco-friendly habits and raise awareness about sustainability. Players make decisions to balance their energy, eco-points, and sustainability levels over the course of 7 days.

The game logic is implemented in Python using Flask, and it is hosted online for easy access.

---

## Hosted Game
- **Game URL**: [https://cool3163.pythonanywhere.com/](https://cool3163.pythonanywhere.com/)
  - This is the main URL where the game is hosted and can be played.
  
- **Redirect URL**: [https://cool3163.github.io/](https://cool3163.github.io/)
  - Visiting this URL will automatically redirect you to the game hosted on PythonAnywhere.

---


## How It Works
1. **Game Logic**:
   - The game logic is implemented in `sustainability_game.py` and is used by the Flask app in `app.py`.
   - Players can perform actions, change locations, and progress through the game by interacting with the web interface.

2. **Hosting**:
   - The game is hosted on PythonAnywhere at [https://cool3163.pythonanywhere.com/](https://cool3163.pythonanywhere.com/).
   - A redirect page (`index.html`) is set up on GitHub Pages at [https://cool3163.github.io/](https://cool3163.github.io/) to forward users to the PythonAnywhere-hosted game.

---

## How to Run Locally
If you'd like to run the game locally on your machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/COOL3163/COOL3163.github.io.git
   cd COOL3163.github.io
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App**:
   ```bash
   python app.py
   ```

5. **Access the Game**:
   - Open your browser and go to `http://127.0.0.1:5000/`.
   - You can now play the game locally.
