#!/usr/bin/python3
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
puzzle = "HANGMAN"#загаданое слово
begin()
length = len(puzzle)
errors = 0
output = ""
i = 0
char = ""
#цикл ввода символов
while True:
    chars = 0
    char = input()
    for key in puzzle:
        if key == char:
            key = char
            print(key)
            output += key
            chars += 1

        #количество ошибок
        if errors == 1:
            oneError()
        elif errors == 2:
            twoError()
        elif errors == 3:
            threeError()
        elif errors == 4:
            fourError()
        elif errors == 5:
            fiveError()
        elif errors == 6:
            sixError()
    if chars == 0:
         errors += 1
    if errors == 7:
        end()
        break
    i += 1
print(output)
