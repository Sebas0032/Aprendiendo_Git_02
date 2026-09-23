from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    round_score_to_ten,
    unique_tags,

)


def test_normalize_answer_unicode_casefold():
    """R-03: casefold Unicode tambien con ß minuscula."""
    assert normalize_answer("Straße") == "strasse"