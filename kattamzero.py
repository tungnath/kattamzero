from flask import Flask, request, jsonify, render_template

from utils.gameit import process_player_turn

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/handle_click', methods=['POST'])
def handle_click():
    data = request.json
    number = data['number']
    player = data['player']
    player_tiles = data['player_tiles']

    print(f"request details : number->{number}, player->{player}, player_tiles->{player_tiles}")

    result = process_player_turn(number, player, player_tiles)

    return jsonify({"message": result['message'], "status": 200, "win": result['win']})


if __name__ == "__main__":
    app.run(debug=True)
