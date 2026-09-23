
from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)
def test_r04_rotate_left_empty_and_negative_steps():
    """R-04: Comprueba lista vacía, pasos negativos (rotación derecha) y pasos mayores a la longitud."""
    assert rotate_left([], 5) == []
    assert rotate_left([1, 2, 3, 4], -1) == [4, 1, 2, 3]
    assert rotate_left([1, 2, 3], 5) == [3, 1, 2]

def test_r05_round_score_halfway_cases():
    """R-05: Comprueba que los valores a mitad de camino (.5) siempre se redondeen hacia arriba."""
    assert round_score_to_ten(5) == 10
    assert round_score_to_ten(15) == 20
    assert round_score_to_ten(25) == 30
    assert round_score_to_ten(12) == 10
    assert round_score_to_ten(0) == 0


def test_r06_rank_teams_case_insensitive_tie_breaking():
    """R-06: Comprueba el ordenamiento descendente y el desempate alfabético case-insensitive."""
    teams = [("beta", 100), ("Alfa", 100), ("Árbol", 50), ("CHARLIE", 100)]
    expected = [("Alfa", 100), ("beta", 100), ("CHARLIE", 100), ("Árbol", 50)]
    assert rank_teams(teams) == expected