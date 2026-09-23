"""Funciones iniciales de Campus Challenge.

Revisa su comportamiento según los requisitos de la actividad.
"""


def normalize_answer(answer):
    """Normaliza una respuesta para compararla sin distinguir mayúsculas."""
    return answer.strip().casefold()


def rotate_left(items: list, steps: int) -> list:
    """R-04: Rotación izquierda circular.
    Admite lista vacía, pasos negativos (rotación a la derecha) y conserva la entrada original.
    """
    if not items:
        return []

    n = len(items)
    effective_steps = steps % n
    return items[effective_steps:] + items[:effective_steps]


def round_score_to_ten(score: int) -> int:
    """R-05: Redondea a la decena más cercana.
    En casos intermedios exactos (.5), redondea siempre hacia arriba.
    """
    remainder = score % 10
    if remainder >= 5:
        return score + (10 - remainder)
    return score - remainder


def rank_teams(entries: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """R-06: Clasifica por puntuación descendente.
    Resuelve empates por nombre del equipo en orden alfabético
    sin distinción de mayúsculas/minúsculas. Conserva la lista original."""
    return sorted(entries, key=lambda x: (-x[1], x[0].casefold()),)



def unique_tags(tags):
    """Elimina etiquetas repetidas."""
    return list(set(tags))


def average_score(scores):
    """Devuelve la media aritmética de las puntuaciones."""
    return sum(scores) / len(scores)