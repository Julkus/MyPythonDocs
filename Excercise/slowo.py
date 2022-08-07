"""
    Napisz program, który pobiera od użytkownika słowo, a następnie wyświetla słowo złożone z co drugiego znaku pobranego.
    W drugiej kolejności program powinien wyświetlić słowo z pozostałych liter.
"""

word_from_user = input(f'Wpisz proszę słowo: ')

new_word = ""
new_word2 = ""
iterate = 0

if __name__ == '__main__':

    for letter in word_from_user:
        if iterate %2 ==0:
            new_word += letter
        if iterate %2 !=0:
            new_word2 += letter

        iterate += 1
    print(new_word,", ", new_word2)


