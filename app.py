from flask import Flask, render_template, request, redirect, url_for, session
from sustainability_game import SustainabilityGame

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Initialize the game
game = SustainabilityGame()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    player_name = request.form.get('player_name')
    if not player_name:
        return redirect(url_for('home'))
    session['player_name'] = player_name
    game.player_name = player_name
    return redirect(url_for('game_view'))

@app.route('/game')
def game_view():
    player = {
        "name": game.player_name,
        "eco_points": game.eco_points,
        "energy": game.energy,
        "day": game.days,
        "sustainability": game.sustainability_level,
        "location": game.current_location
    }
    return render_template(
        'game.html',
        player=player,
        actions=game.locations[game.current_location]['actions']
    )

@app.route('/action/<action>')
def perform_action(action):
    if action in game.locations[game.current_location]['actions']:
        game.perform_action(action)
    return redirect(url_for('game_view'))

@app.route('/end_day')
def end_day():
    game.end_day()
    return redirect(url_for('game_view'))

@app.route('/change_location/<location>')
def change_location(location):
    if location in game.locations:
        game.current_location = location
    return redirect(url_for('game_view'))

@app.route('/quit')
def quit_game():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)