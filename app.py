from flask import Flask, render_template, request, redirect, url_for, session
from sustainability_game import SustainabilityGame

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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

    global game
    game = SustainabilityGame()
    game.player_name = player_name
    
    return redirect(url_for('game_view'))

@app.route('/game')
def game_view():
    if game.days > 7:  # End the game after 7 days
        return redirect(url_for('game_over'))

    player = {
        "name": game.player_name,
        "eco_points": game.eco_points,
        "energy": game.energy,
        "day": game.days,
        "sustainability": game.sustainability_level,
        "location": game.current_location
    }
    location = game.locations[game.current_location]
    return render_template(
        'game.html',
        player=player,
        location=location,
        actions=location['actions'],
        game=game,  # Pass the game object to the template
        tip=session.pop('sustainability_tip', None)
    )

@app.route('/action/<action>')
def perform_action(action):
    result = game.perform_action(action)
    if "error" in result:
        return redirect(url_for('game_view'))
    return redirect(url_for('game_view'))

@app.route('/change_location/<location>')
def change_location(location):
    if location in game.locations:
        game.current_location = location
        game.energy -= 5  # Traveling consumes energy
    return redirect(url_for('game_view'))

@app.route('/end_day')
def end_day():
    game.end_day()
    return redirect(url_for('game_view'))

@app.route('/random_tip')
def random_tip():
    session['sustainability_tip'] = game.get_random_tip()
    return redirect(url_for('game_view'))

@app.route('/game_over')
def game_over():
    return render_template(
        'game_over.html',
        stats={
            "name": game.player_name,
            "days": game.days,
            "eco_points": game.eco_points,
            "sustainability": game.sustainability_level
        }
    )

if __name__ == '__main__':
    app.run(debug=True)