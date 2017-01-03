def begin():
    print(" =====||")
    print(" |    ||")
    print("      ||")
    print("      ||")
    print("      ||")
    print("      ||")
    print("      ||")
    print("========")


def oneError():
    print(" =====||")
    print(" |    ||")
    print(" 0    ||")
    print("      ||")
    print("      ||")
    print("      ||")
    print("      ||")
    print("========")


def twoError():
    print(" =====||")
    print(" |    ||")
    print(" 0    ||")
    print(" |    ||")
    print("      ||")
    print("      ||")
    print("      ||")
    print("========")


def threeError():
    print(" =====||")
    print(" |    ||")
    print(" 0    ||")
    print("/|    ||")
    print("      ||")
    print("      ||")
    print("      ||")
    print("========")


def fourError():
    print(" =====||")
    print(" |    ||")
    print(" 0    ||")
    print("/|\   ||")
    print("      ||")
    print("      ||")
    print("      ||")
    print("========")


def fiveError():
    print(" =====||")
    print(" |    ||")
    print(" 0    ||")
    print("/|\   ||")
    print(" |    ||")
    print("/     ||")
    print("      ||")
    print("========")


def sixError():
    print(" =====||")
    print(" |    ||")
    print(" 0    ||")
    print("/|\   ||")
    print(" |    ||")
    print("/ \   ||")
    print("      ||")
    print("========")


def end():
    print("|||||||  || \    ||    ||+++")
    print("||       ||\ \   ||    ||   ++")
    print("|||||||  || \ \  ||    ||   ++")
    print("||       ||  \ \ ||    ||   ++")
    print("|||||||  ||   \ \||    ||+++")
puzzle = "HANGMAN"
begin()
errors = len(puzzle)
i = 0
char = ""
while(i < errors):
    char += input()
    i += 1
    print(char)
