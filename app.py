from flask import Flask, render_template, request, redirect, url_for, session
from sustainability_game import SustainabilityGame

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    player_name = request.form.get('player_name')
    if not player_name:
        return redirect(url_for('home'))

    app.game = SustainabilityGame()  # Attach the game object to the app instance
    app.game.player_name = player_name
    
    return redirect(url_for('game_view'))

@app.route('/game')
def game_view():
    if not hasattr(app, 'game') or app.game.energy <= 0 or app.game.days > 7:
        return redirect(url_for('game_over'))

    player = {
        "name": app.game.player_name,
        "eco_points": app.game.eco_points,
        "energy": app.game.energy,
        "day": app.game.days,
        "sustainability": round(app.game.sustainability_level),
        "location": app.game.current_location
    }
    location = app.game.locations[app.game.current_location]
    return render_template(
        'game.html',
        player=player,
        location=location,
        actions=location['actions'],
        tip=session.pop('sustainability_tip', None),
        game={"locations": app.game.locations}  # Pass game.locations explicitly
    )

@app.route('/action/<action>')
def perform_action(action):
    result = app.game.perform_action(action)
    if "error" in result:
        return redirect(url_for('game_view'))
    return redirect(url_for('game_view'))

@app.route('/change_location/<location>')
def change_location(location):
    if location in app.game.locations:
        app.game.current_location = location
        app.game.energy -= 5  
    return redirect(url_for('game_view'))

@app.route('/end_day')
def end_day():
    app.game.end_day()
    return redirect(url_for('game_view'))

@app.route('/random_tip')
def random_tip():
    session['sustainability_tip'] = app.game.get_random_tip()
    return redirect(url_for('game_view'))

@app.route('/game_over')
def game_over():
    reason = "You ran out of energy!" if app.game.energy <= 0 else "You completed 7 days!"
    suggestions = "Try to balance your energy and eco points better next time!" if app.game.energy <= 0 else "Great job! Aim for a higher sustainability level next time!"
    return render_template(
        'game_over.html',
        stats={
            "name": app.game.player_name,
            "days": app.game.days,
            "eco_points": app.game.eco_points,
            "sustainability": round(app.game.sustainability_level),
            "reason": reason,
            "suggestions": suggestions
        }
    )

if __name__ == '__main__':
    app.run(debug=True)