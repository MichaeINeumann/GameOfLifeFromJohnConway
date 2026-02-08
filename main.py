"""Run the Game of Life application."""
from __future__ import annotations

import tkinter as tk

from game_of_life.core import GameOfLife
from game_of_life.gui import GameOfLifeGUI


def main() -> None:
    game = GameOfLife(width=10_000, height=10_000)
    root = tk.Tk()
    GameOfLifeGUI(root, game)
    root.mainloop()


if __name__ == "__main__":
    main()
