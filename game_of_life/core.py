"""Core logic for Conway's Game of Life."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


NEIGHBOR_OFFSETS = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
)


@dataclass
class GameOfLife:
    width: int
    height: int
    alive: set[tuple[int, int]] = field(default_factory=set)

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def clear(self) -> None:
        self.alive.clear()

    def set_alive(self, cells: Iterable[tuple[int, int]]) -> None:
        for x, y in cells:
            if self.in_bounds(x, y):
                self.alive.add((x, y))

    def toggle(self, x: int, y: int) -> None:
        if not self.in_bounds(x, y):
            return
        if (x, y) in self.alive:
            self.alive.remove((x, y))
        else:
            self.alive.add((x, y))

    def step(self) -> None:
        neighbor_counts: dict[tuple[int, int], int] = {}

        for x, y in self.alive:
            for dx, dy in NEIGHBOR_OFFSETS:
                nx, ny = x + dx, y + dy
                if not self.in_bounds(nx, ny):
                    continue
                neighbor_counts[(nx, ny)] = neighbor_counts.get((nx, ny), 0) + 1

        new_alive: set[tuple[int, int]] = set()
        for cell, count in neighbor_counts.items():
            if count == 3 or (count == 2 and cell in self.alive):
                new_alive.add(cell)

        self.alive = new_alive
