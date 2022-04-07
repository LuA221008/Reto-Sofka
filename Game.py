
class Game:

    def __init__(self, Player, Questions):

        self.player = Player
        self.score = Player.score
        self.round = Player.round
        self.user_name = Player.name
        self.questions = Questions
        self.current_question = []

    def setQuestion(self):

        self.current_question = self.questions.getRandomQuestion(self.round)

    def MapQuestions(self, question, randomQuestion):

        # retorna el lugar de la respuesta correcta en las opciones de la pregunta
        for option in range(0, len(randomQuestion)):
            if randomQuestion[option] == question[0]:
                return option

    def updateScore(self):

        if self.round == 5:
            self.score += 1000
        else:
            self.score += self.round * 100
        self.updateRound()
        self.savePlayerScore(self.player)

    def resetScore(self):

        self.score = 0
        self.round = 1
        self.savePlayerScore(self.player)

    def savePlayerScore(self, player):

        player.savePlayerInfo(self.user_name)

    def getCurrentQuestion(self):

        return self.current_question

    def getCurrentRound(self):

        return self.round

    def getScore(self):

        return self.score

    def updateRound(self):

        self.round += 1
