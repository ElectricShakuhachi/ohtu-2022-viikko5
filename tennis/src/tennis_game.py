class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player_names = {1: player1_name, 2: player2_name}
        self.situation = {1 : 0, 2 : 0}
        self.score_names = {0 : "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        for n in [1, 2]:
            if self.player_names[n] == player_name:
                player = n
        self.situation[player] += 1

    def get_score(self):
        score_difference = self.situation[1] - self.situation[2]
        if score_difference == 0:
            if self.situation[1] == 4:
                return "Deuce"
            return self.score_names[self.situation[1]] + "-All"
        if max(self.situation.values()) >= 4:
            if score_difference == 1:
                return f"Advantage {self.player_names[1]}"
            if score_difference == -1:
                return f"Advantage {self.player_names[2]}"
            if score_difference >= 2:
                return f"Win for {self.player_names[1]}"
            if score_difference <= -2:
                return f"Win for {self.player_names[2]}"
        return self.score_names[self.situation[1]] + "-" + self.score_names[self.situation[2]]