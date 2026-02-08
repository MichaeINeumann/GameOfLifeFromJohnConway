"""Common Game of Life patterns."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Pattern:
    name: str
    cells: tuple[tuple[int, int], ...]


BLINKER = Pattern(
    "Blinker",
    ((0, 0), (1, 0), (2, 0)),
)

TOAD = Pattern(
    "Toad",
    ((1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)),
)

GLIDER = Pattern(
    "Glider",
    ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)),
)

LIGHTWEIGHT_SPACESHIP = Pattern(
    "LWSS",
    ((1, 0), (4, 0), (0, 1), (0, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3)),
)

GOSPER_GLIDER_GUN = Pattern(
    "Gosper Gun",
    (
        (0, 4), (1, 4), (0, 5), (1, 5),
        (10, 4), (10, 5), (10, 6),
        (11, 3), (11, 7),
        (12, 2), (12, 8),
        (13, 2), (13, 8),
        (14, 5),
        (15, 3), (15, 7),
        (16, 4), (16, 5), (16, 6),
        (17, 5),
        (20, 2), (20, 3), (20, 4),
        (21, 2), (21, 3), (21, 4),
        (22, 1), (22, 5),
        (24, 0), (24, 1), (24, 5), (24, 6),
        (34, 2), (34, 3), (35, 2), (35, 3),
    ),
)

PATTERNS = (
    BLINKER,
    TOAD,
    GLIDER,
    LIGHTWEIGHT_SPACESHIP,
    GOSPER_GLIDER_GUN,
)
