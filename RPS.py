# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def jugada_ganadora(move):
    return {'R': 'P', 'P': 'S', 'S': 'R'}[move]

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"

    # Usa los últimos 3 movimientos del oponente para detectar patrones
    if len(opponent_history) >= 4:
        ultimas_jugadas = "".join(opponent_history[-4:])
        patterns = {}

        # Busca patrones en el historial
        for i in range(len(opponent_history) - 4):
            pattern = "".join(opponent_history[i:i+4])
            next_move = opponent_history[i + 4]
            if pattern not in patterns:
                patterns[pattern] = {"R": 0, "P": 0, "S": 0}
            patterns[pattern][next_move] += 1

        # Si se encuentra el patrón, predice la jugada más probable
        if ultimas_jugadas in patterns:
            prediccion = max(patterns[ultimas_jugadas], key=patterns[ultimas_jugadas].get)
            guess = jugada_ganadora(prediccion)

    return guess
