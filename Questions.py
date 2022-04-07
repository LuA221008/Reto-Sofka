import csv
import random


class Questions:

    def __init__(self):
        self.questionsDict = {}
        self.dataBaseName = 'Questions.csv'
        self.fillBankOfQuestions(self.dataBaseName)

    def getRandomQuestion(self, round):
        numOfQuestions = len(self.questionsDict[round])
        radomQuestion = random.randint(0, numOfQuestions - 1)
        return self.questionsDict[round][radomQuestion]

    def fillBankOfQuestions(self, data_base_name):
        with open(data_base_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    difficulty = int(row[0])
                    statement = row[1]
                    answer = row[2]
                    option1 = row[3]
                    option2 = row[4]
                    option3 = row[5]
                    currentQuestion = [statement, answer, option1, option2, option3]
                    if difficulty in self.questionsDict:
                        self.questionsDict[difficulty].append(currentQuestion)
                    else:
                        level = []
                        level.append(currentQuestion)
                        self.questionsDict[difficulty] = level
                    line_count += 1
