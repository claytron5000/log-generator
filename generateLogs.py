import datetime
import random
import os.path


class LogGenerator:

    def __init__(self, startDate: datetime, endDate: datetime):
        self.start = startDate
        self.end = endDate

    def generateDate(self, startDateTime, endDateTime):
        delta = endDateTime - startDateTime
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return startDateTime + datetime.timedelta(seconds=random_second)

    def generateRandomResponseCode(self):
        err = random.choices(["ERROR", "INFO", "WARNING"], [10, 55, 5])

        if err[0] == "ERROR":
            code = random.choices(["400", "403", "404", "422", "418", "451", "438", "500", "502"], [3, 4, 5, 4, 3, 4, 1, 4, 2])
        elif err[0] == "INFO":
            code = random.choices(["200", "201", "301"], [50, 18, 9])
        else:
            code = random.choices(["301", "302", "308"], [1, 1, 1])

        return "{} {}".format(err[0], str(code[0]))

    def file_len(self, fname):
        i = -1
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def gererateFilePath(self):
        length = self.file_len("files.txt")
        randomLine = random.randrange(length)
        with open("files.txt") as fp:
            for i, line in enumerate(fp):
                if i == randomLine:
                    return line

        return ""

    def generateErrorPath(self):
        return random.choice(["sites/all/libraries/phpmailer/find.php", "modules/menu/the/answer.php"])

    def generateRow(self):
        responseCode = self.generateRandomResponseCode()
        # print(responseCode)
        if responseCode == "ERROR 438":
            return "[{}] {} {} {}".format(
            self.generateDate(self.start, self.end),
            random.randrange(10000),
            responseCode,
            self.generateErrorPath()
            ) + "\n"
        else:
            return "[{}] {} {} {}".format(
                self.generateDate(self.start, self.end),
                random.randrange(10000),
                responseCode,
                self.gererateFilePath()
            )

    def generateLogs(self, number: int):
        if os.path.exists("./logs.txt"):
            with open("logs.txt", "w") as logfile:
                for i in range(number):
                    line = self.generateRow()
                    logfile.write(line)
        else:
            with open("logs.txt", "x") as logfile:
                for i in range(number):
                    line = self.generateRow()
                    logfile.write(line)


start = datetime.datetime.strptime("2021-05-12", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-05-18", "%Y-%m-%d")
generator = LogGenerator(start, end)
generator.generateLogs(10_000)
