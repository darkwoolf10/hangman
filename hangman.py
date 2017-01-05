# !/usr/bin/python3
# Короче тебе надо если char in puzzle искать re.find_all по чару в
# puzzle. После, по найденым индексам (в цикле, даже если
# буква одна) менять по индексу буквы в secret и вывести secret

from pictures import *

puzzle = "HANGMAN"# загаданое слово
begin()
length = len(puzzle)
errors = 0
output = ""
i = 0
char = ""
secret = "_" * length
print(secret)
#цикл ввода символов
while True:
    chars = 0
    char = input()
    for key in puzzle:
        if key == char:
            secret[] = key
            print(key)
            output += key
            chars += 1  # Если не найдт совпадений, то в конце цикла выполнеться условие

    # количество ошибок
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
