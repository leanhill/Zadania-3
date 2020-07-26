from Plansza_lista_list import noughts_and_crosses
import pytest


@pytest.mark.parametrize("n, result", [([[1, 2, 0],
                                        [1, 1, 0],
                                        [1, 2, 2]], "Wygrana gracza X"),
                                       ([[2, 2, 0],
                                         [1, 1, 0],
                                         [1, 2, 2]], "Remis"),
                                       ([[1, 2, 0],
                                        [0, 1, 0],
                                        [1, 2, 1]], "Wygrana gracza X"),
                                       ([[2, 2, 0],
                                        [1, 1, 0],
                                        [2, 2, 2]], "Wygrana gracza Y")
                                       ])
def test_noughts_and_crosses(n, result):
    assert noughts_and_crosses(n) == result