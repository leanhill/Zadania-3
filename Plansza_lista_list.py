"""napisz funkcję która przyjmie jako argument listę list np:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

i w rezultacie zwróci jeden z możliwości: wygrana, remis lub przegrana. Plansza ta to plansza do gry w kółko i krzyżyk.
 Cyfry na planszy oznaczają: 0 - nie wypełnione pole, 1 - pole z wypełnionym "x"em i 2 - pole z wypełnionym "y"kiem.
 Do tego zadania koniecznie napisz test:)

- zaimplementuj sortowanie przez wstawiane - http://www.algorytm.edu.pl/algorytmy-maturalne/sortowanie-przez-wstawianie.html

- w artykule wyżej użyto terminu złożoności, tutaj materiał o tym czym to jest
- https://www.samouczekprogramisty.pl/podstawy-zlozonosci-obliczeniowej/ """

def noughts_and_crosses(game):
    result = "Remis"
    for i in range(0, 3):
        if game[i][0] == game[i][1] == game[i][2] == 1 or game[0][i] == game[1][i] == game[2][i] == 1:
            result = "Wygrana gracza X"
            break
        elif game[i][0] == game[i][1] == game[i][2] == 2 or game[0][i] == game[1][i] == game[2][i] == 2:
            result = "Wygrana gracza Y"
            break
        elif i == 0:
             if game[i][i] == game[i+1][i+1] == game[i+2][i+2] == 1:  
                 result = "Wygrana gracza X"
                 break
             elif game[i][i] == game[i+1][i+1] == game[i+2][i+2] == 2:
                 result = "Wygrana gracza Y"                          
    return result
