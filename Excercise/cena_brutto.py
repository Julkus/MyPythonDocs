"""
    Napisz funkcje, ktora na podstawie podanego slownika
    z zakupami jako kluczami oraz z krotka (tuple) z cena i podatkiem,
    wyliczy kwote brutto calych zakupow.
    Parametr grocery_list moze miec postac:
    {"mleko": (5.00, 10), "ser": (4.50, 15), "jogurt": (3, 25)}.
    Pierwsza wartosc w krotce to cena netto, druga to podatek (np. dla 10%
    podatku danego produktu i jego ceny brutto 10 pln, cena brutto bedzie
    wynosila 1.1*10). Nalezy zsumowac ceny brutto dla kazdego produktu
    i zwrocic wynik.
    Nalezy przyjac, ze uzytkownik nie poda blednych wartosci (czyli, ze
    cena nigdy nie bedzie ujemna, a podatek zawsze bedzie sie miescil
    w zbiorze <0; 100>.
"""


def calculate_brutto_prize(grocery_list):
    """Oblicza cene brutto wszystkich zakupow z grocery_list.

    :param grocery_list: slownik, w ktorym kluczami sa stringi reprezentujace zakupy,
        a wartosciami krotki (tuple) z dwiema liczbami: cena produktu i jego podatkiem.
    :return: sume wszystkich wartosci brutto z listy (jako liczba).

    """
    pass

# grocery_list = {}
#
# product = input(f'Podaj produkt do zakupu: ')
# price = input(f'Podaj cenę netto: ')
# tax = input(f'Podaj wartość podatku w %: ')
#
# if product not in grocery_list:
#     grocery_list[product] = tuple(map(float, price + int(tax)))
#
# print(grocery_list) to jest źle:)

grocery_list = {"mleko": (5.00, 10), "ser": (4.50, 15), "jogurt": (3, 25)}

def calculate_brutto_prize(grocery_list):
    for product in grocery_list.keys:
        grocery_list.get(product)[0]*grocery_list(product)[1]/100+grocery_list.get(product)[0] #get zabezpieczenie
    # gdyby nie było klucza w słowniku, żeby nie zwróciło none
        suma +=cena

    return suma
print(f'Suma zakupów wynosi: {calculate_brutto_prize(grocery_list)}')


