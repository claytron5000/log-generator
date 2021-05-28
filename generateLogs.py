import datetime
import random


def generateDate(startDateTime, endDateTime):
    delta = endDateTime - startDateTime
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return startDateTime + datetime.timedelta(seconds=random_second)


# test
start = datetime.datetime.strptime("2021-05-12", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-05-18", "%Y-%m-%d")
# print(generateDate(start, end))


def generateRandomResponseCode():
    err = random.choices(["ERROR", "INFO", "WARNING"], [1, 55, 5])

    if err[0] == "ERROR":
        code = random.choice([400, 403, 404, 500])
    elif err[0] == "INFO":
        code = random.choices([200, 201, 301], [50, 18, 9])
    else:
        code = random.choice([301, 302, 339])

    return "{} {}".format(err[0], code[0])


def file_len(fname):
    i = -1
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def gererateFilePath():
    length = file_len("files.txt")
    randomLine = random.randrange(length)
    with open("files.txt") as fp:
        for i, line in enumerate(fp):
            if i == randomLine:
                return line

    return ""


def generateRow():
    return "[{}] {} {} {}".format(generateDate(start, end), random.randrange(10000), generateRandomResponseCode(), gererateFilePath())


# test
print(generateRow())
