"""
- napisz funkcje która używając znaków: | i - wyrysuje planszę do gry:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---


funkcja powinna przyjmować  jako argument: ilość wierszy, ilość kolumn oraz szerokość komórki i wysokość komórki
 (liczone w ilości myślników i znaków | ).
"""
def game_area_printer(width, height, number_columns, number_rows):
    for i in range (number_rows):
        print((" " + "-" * width) * number_columns)
        for i in range (height):
            print(("|" + " " * (width)) * (number_columns + 1))
    print((" " + "-" * width) * number_columns)





