import csv


class Player:

    def __init__(self):
        self.name = ""
        self.round = 1
        self.score = 0
        self.playerDB = 'Players.csv'

    def setNewPlayer(self, userName):

        self.name = userName
        return self.checkNewPlayer(userName)

    def checkNewPlayer(self, userName):

        with open(self.playerDB) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    if row[0] == userName:
                        csv_file.close()
                        return False
                    line_count += 1
            csv_file.close()
            return True

    def saveNewPlayer(self, userName):

        newUserData = [userName]
        with open(self.playerDB, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(newUserData)
            csv_file.close()

    def savePlayerInfo(self, usernaName):

        newData = [usernaName]
        with open(self.playerDB) as inf:
            reader = csv.reader(inf.readlines())
        with open(self.playerDB, 'w', newline='') as file:
            writer = csv.writer(file)
            for line in reader:
                if line[0] == usernaName:
                    writer.writerow(newData)
                    break
                else:
                    writer.writerow(line)
            writer.writerows(reader)
