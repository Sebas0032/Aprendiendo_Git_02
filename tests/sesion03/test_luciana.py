from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    round_score_to_ten,
    unique_tags,
    verify_python_version

)

def test_python_version_is_3_10_or_newer():
    """R-01: Se utiliza Python 3.10 o superior."""
    assert verify_python_version() is True

def test_normalize_answer_unicode_casefold():
    """R-03: casefold Unicode tambien con ß minuscula."""
    assert normalize_answer("Straße") == "strasse"