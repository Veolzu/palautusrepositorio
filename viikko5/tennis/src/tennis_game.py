class TennisGame:
    ENDGAME_POINTS = 4

    EQUAL_LOVE_ALL = 0
    EQUAL_FIFTEEN_ALL = 1
    EQUAL_THIRTY_ALL = 2

    ADVANTAGE = 1
    WIN = 2

    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FOURTY = 3
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score = ""
    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def when_equal_score(self):
        if self.m_score1 == self.EQUAL_LOVE_ALL:
            self.score = "Love-All"
        elif self.m_score1 == self.EQUAL_FIFTEEN_ALL:
            self.score = "Fifteen-All"
        elif self.m_score1 == self.EQUAL_THIRTY_ALL:
            self.score = "Thirty-All"
        else:
            self.score = "Deuce"

    def when_endgame(self):
        score_difference = self.m_score1 - self. m_score2

        if score_difference == self.ADVANTAGE:
            self.score = "Advantage player1"
        elif score_difference == -self.ADVANTAGE:
            self.score = "Advantage player2"
        elif score_difference >= self.WIN:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"

    def scoring_for_player(self, player_score):
        if player_score == self.LOVE:
            self.score = self.score + "Love"
        elif player_score == self.FIFTEEN:
            self.score = self.score + "Fifteen"
        elif player_score == self.THIRTY:
            self.score = self.score + "Thirty"
        elif player_score == self.FOURTY:
            self.score = self.score + "Forty"
    def get_score(self):
        self.score = ""
        if self.m_score1 == self.m_score2:
            self.when_equal_score()

        elif self.m_score1 >= self.ENDGAME_POINTS or self.m_score2 >= self.ENDGAME_POINTS:
            self.when_endgame()
        else:
            self.scoring_for_player(self.m_score1)
            self.score = self.score + "-"
            self.scoring_for_player(self.m_score2)

        return self.score
