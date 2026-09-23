from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)
#R7
def test_unique_tags_preserves_first_occurrence_and_is_case_sensitive():
    assert unique_tags(["chimbombìn", "Chimbombìn", "CHIMBOMBÌN", "chimbombìn", "linasa"]) == [
        "chimbombìn",
        "Chimbombìn",
        "CHIMBOMBÌN",
        "linasa",
    ]
#R8
def test_average_score_returns_zero_for_empty_collection():
    assert average_score([]) == 0.0