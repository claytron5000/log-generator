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

    # test

    # print(generateDate(start, end))

    def generateRandomResponseCode(self):
        err = random.choices(["ERROR", "INFO", "WARNING"], [1, 55, 5])

        if err[0] == "ERROR":
            code = random.choice(["400", "403", "404", "500"])
        elif err[0] == "INFO":
            code = random.choices(["200", "201", "301"], [50, 18, 9])
        else:
            code = random.choice(["301", "302", "339"])

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

    def generateRow(self):
        return "[{}] {} {} {}".format(
            self.generateDate(self.start, self.end),
            random.randrange(10000),
            self.generateRandomResponseCode(),
            self.gererateFilePath()
        )

    # test
    # print(generateRow())

    def generateLogs(self, number: int):
        if os.path.exists("./logs.txt"):
            with open("logs.txt", "w") as log:
                for i in range(number):
                    line = self.generateRow()
                    log.write(line)
        else:
            with open("logs.txt", "x") as log:
                for i in range(number):
                    line = self.generateRow()
                    log.write(line)


# generateLogs(10000)
start = datetime.datetime.strptime("2021-05-12", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-05-18", "%Y-%m-%d")
generator = LogGenerator(start, end)
generator.generateLogs(1000000)
