from random import shuffle
from tkinter import *

from Player import Player
from Questions import Questions
from Game import Game


class Window:

    def __init__(self):
        self.root = Tk()
        self.questions = Questions()
        self.player = Player()
        self.configureMainWindow()
        self.root.mainloop()

    def configureMainWindow(self):

        self.root.title("PREGUNTADOS")
        self.root.configure(background='black')
        self.root.geometry("1000x700")
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        pageTitle = Label(self.root, text="Preguntados", font=("Microsoft Sans Serif", 45), bg='black',
                          fg="#1AC7FF")
        pageTitle.grid(column=2, row=0, padx=10, pady=10)
        putYourUserName = Label(self.root, text="Give us your name", font=("Microsoft Sans Serif", 25),
                                bg='black', fg="white")
        putYourUserName.grid(column=2, row=5, padx=10, pady=10)
        inputUserName = Entry(self.root, bg='#1AC7FF', fg='black', font=("Microsoft Sans Serif", 15), )
        inputUserName.grid(column=2, row=6, padx=10, pady=10)
        submitButton = Button(self.root, text="Start",
                              command=lambda: self.validateUserName(inputUserName.get()),
                              width=10, height=1, bg='#5AE500', fg='white',
                              font=("Microsoft Sans Serif", 15))  # width, height en pixeles
        submitButton.grid(row=7, column=2, padx=20, pady=20)

    def validateUserName(self, userName):

        playerName = userName

        if playerName:
            self.player.saveNewPlayer(playerName)
            self.startGame()
        else:
            typeOfError = 1
            self.displayErrorMessage(typeOfError)

    def startGame(self):

        for widgets in self.root.winfo_children():
            widgets.destroy()
        self.configureQuestionsWindow()

    def configureQuestionsWindow(self):

        game = Game(self.player, self.questions)
        self.setQuestionsWindow(game)

    def setQuestionsWindow(self, game):

        if game.getCurrentRound() == 6:
            self.gameCleared(game)
        else:
            game.setQuestion()
            currentRound = game.getCurrentRound()
            currentQuestion = game.getCurrentQuestion()
            options = currentQuestion[1:]
            questionStatement = currentQuestion[0]
            currentScore = game.getScore()
            shuffle(options)
            realAnswer = game.MapQuestions(currentQuestion[1:], options)
            self.buildQuestionsWindow(questionStatement, currentRound, options, realAnswer, currentScore, game)

    def buildQuestionsWindow(self, questionStatement, currentRound, options, realAnswer, currentScore, game):

        roundTitle = Label(self.root, text="Level: " + str(currentRound), font=("Microsoft Sans Serif", 25), bg='black',
                           fg="#1AC7FF")
        roundTitle.grid(column=2, row=0, padx=10, pady=10)
        questionStamentLabel = Label(self.root, text=questionStatement, font=("Microsoft Sans Serif", 25), bg='black',
                                     fg="white")
        questionStamentLabel.grid(column=2, row=1, padx=10, pady=10)
        scoreLabel = Label(self.root, text="Puntaje: " + str(currentScore), font=("Microsoft Sans Serif", 20), bg='black',
                           fg="#1AC7FF")
        scoreLabel.grid(column=3, row=0, padx=10, pady=10)
        userAnswer = IntVar()
        Radiobutton(self.root, text=options[0], variable=userAnswer, value=0, bg='black', fg='#1DB954', font=("Microsoft Sans Serif", 15)).grid(column=2,
                                                                                                             row=2)
        Radiobutton(self.root, text=options[1], variable=userAnswer, value=1, bg='black', fg='#1DB954', font=("Microsoft Sans Serif", 15)).grid(column=2,
                                                                                                             row=3)
        Radiobutton(self.root, text=options[2], variable=userAnswer, value=2, bg='black', fg='#1DB954', font=("Microsoft Sans Serif", 15)).grid(column=2,
                                                                                                             row=4)
        Radiobutton(self.root, text=options[3], variable=userAnswer, value=3, bg='black', fg='#1DB954', font=("Microsoft Sans Serif", 15)).grid(column=2,
                                                                                                             row=5)
        validateAns = Button(self.root, text="Submit",
                             command=lambda: self.validateUserAns(realAnswer, userAnswer.get(), game), width=10,
                             height=1, bg='#1AC7FF', fg='white', font=("Microsoft Sans Serif", 20))
        validateAns.grid(row=7, column=2, padx=20, pady=20)

    def validateUserAns(self, realAnswer, userAnswer, game):

        if userAnswer == realAnswer:
            for widgets in self.root.winfo_children():
                widgets.destroy()
            self.updateGame(game)
        else:
            for widgets in self.root.winfo_children():
                widgets.destroy()
            self.gameOver(game)

    def updateGame(self, game):

        game.updateScore()
        self.setQuestionsWindow(game)

    def gameOver(self, game):

        game.resetScore()
        self.showGameOver()

    def showGameOver(self):

        error = Toplevel(self.root)
        error.configure(background='black')
        error.geometry("600x250")
        error.title("Game over")
        Label(error, text="Juego terminado: has perdido", font=('Windows Sans Serif', 20), bg='black',
              fg="#1AC7FF").place(x=150, y=80)

    def gameCleared(self, game):

        cleared = Toplevel(self.root)
        cleared.configure(background='black')
        cleared.geometry("750x250")
        cleared.title("Felicitaciones")
        Label(cleared, text="Ganaste!!!", font=('Windows Sans Serif', 20), bg='black', fg="#1AC7FF").place(x=150, y=80)
        Label(cleared, text="Tu puntaje: " + str(game.getScore()), font=('Windows Sans Serif', 20), bg='black',
              fg="#F80332").place(x=150, y=160)

