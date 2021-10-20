import math
def citire_list():
    result_list = []
    dimensiune = int(input("Dimensiune lista: "))

    while dimensiune:
        element = float(input("Introduceti un element: "))
        result_list.append(element)
        dimensiune -= 1

    return result_list

def gaseste_partea_intreaga(lista):
    """

    :param lista: Aceasta functie primeste o lista de numere tip float
    :return: Aceasta functie returneaza o lista in care se afla toate partile intregi ale numerelor din lista
    """
    result = []

    for numar in lista:
            result.append(int(numar))

    return result

def test_gaseste_partea_intreaga():
    assert gaseste_partea_intreaga([3.4, 5.4, 3.89]) == [3, 5, 3]
    assert gaseste_partea_intreaga([7.9, 15.4, 63.89]) == [7, 15, 63]
    assert gaseste_partea_intreaga([8.567, 13.32, 17.89]) == [8, 13, 17]

def interval_deschis(lista, cs, cd):
    """

    :param lista: Acesta functie primeste o lista de float-uri
    :param cs: Acest parametru indica capatul din stanga al intervalului dat
    :param cd: Acest parametru indica capatul din dreapta al intervalului dat
    :return: Functia returneaza o lista in carte toate elementele sunt cuprinse in intervalul deschis (cs, cd) dat si in caz contrar o lista goala
    """
    rezult=[]
    for start in  lista:
        if start > cs:
            if start <cd:
                rezult.append(start)
    return rezult

def test_interval_deschis():
    assert interval_deschis([2.3, 3.4, 5.4], 4, 5) == []
    assert interval_deschis([4.3, 3.4, 8.90], 3, 10) == [4.3, 3.4, 8.90]
    assert interval_deschis([-7.3, 4.4, -5.01], 4, 20) == [4.4]

def get_numbers_with_int_part_div_of_fractional_part(lista):
    """

    :param lista: Aceasta functie primeste ca parametru o lista de numere de tip float
    :return: Aceasta functie returneaza o lista goala daca nu exista niciun numar care sa respecte cerinta si o lista cu numere de tip cerinta data
    """
    rezult=[]
    for start in lista:
        if(int(str(start).split('.')[1]) != 0):
            if int(str(start).split('.')[1]) % int(start) == 0:
                rezult.append(start)
    return rezult

def test_get_numbers_with_int_part_div_of_fractional_part():
    assert get_numbers_with_int_part_div_of_fractional_part([1.5, 3.3, 8.0, 8.9]) == [1.5, 3.3]
    assert get_numbers_with_int_part_div_of_fractional_part([2.6, 3.15, 15.17, 13.13]) == [2.6, 3.15, 13.13]
    assert get_numbers_with_int_part_div_of_fractional_part([4.32, 54.108, 5.3]) == [4.32, 54.108]

def main():
    while True:
     print("1. Citirea unei liste de numere float")
     print("2. Afișarea părții întregi a tuturor numerelor din listă")
     print("3. Afisarea tuturor numerelor care apartin unui interval deschis citit de la tastatura")
     print("4. Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare")
     print("x.")

     optiune = input("Alege comanda ta: ")
     if optiune == "1":
        lista = citire_list()
     elif optiune == "2":
        print(f"Lista cu partile intregi din lista initiala este: {gaseste_partea_intreaga(lista)}")
     elif optiune == "3":
        capatul_din_stanga = int(input("Alege capatul din stanga: "))
        capatul_din_dreapta = int(input("Alege capatul din dreapta: "))
        print(f"Numerele care apartin intervalului deschis sunt: {interval_deschis(lista, capatul_din_stanga, capatul_din_dreapta)}")
     elif optiune == "4":
        print(f"Numerele care au partea fractionara divizibila cu partea intreaga sunt: {get_numbers_with_int_part_div_of_fractional_part(lista)}")
     elif optiune == "x":
         break


test_get_numbers_with_int_part_div_of_fractional_part()
test_interval_deschis()
test_gaseste_partea_intreaga()
main()