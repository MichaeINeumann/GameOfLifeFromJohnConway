"""Tkinter GUI for Conway's Game of Life."""
from __future__ import annotations

import random
import tkinter as tk
from tkinter import ttk

from .core import GameOfLife
from .patterns import PATTERNS, Pattern


class GameOfLifeGUI:
    def __init__(
        self,
        root: tk.Tk,
        game: GameOfLife,
        cell_size: int = 8,
        view_width: int = 80,
        view_height: int = 60,
    ) -> None:
        self.root = root
        self.game = game
        self.cell_size = cell_size
        self.view_width = view_width
        self.view_height = view_height
        self.running = False
        self.after_id: str | None = None

        self.offset_x = (self.game.width - self.view_width) // 2
        self.offset_y = (self.game.height - self.view_height) // 2

        self.root.title("Conway's Game of Life")

        self.canvas = tk.Canvas(
            root,
            width=self.view_width * self.cell_size,
            height=self.view_height * self.cell_size,
            bg="white",
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.bind("<Button-1>", self.on_click)

        control_frame = ttk.Frame(root, padding=8)
        control_frame.grid(row=0, column=1, sticky="nsew")

        ttk.Button(control_frame, text="Start", command=self.start).grid(row=0, column=0, sticky="ew")
        ttk.Button(control_frame, text="Stop", command=self.stop).grid(row=0, column=1, sticky="ew")
        ttk.Button(control_frame, text="Step", command=self.step_once).grid(row=1, column=0, sticky="ew")
        ttk.Button(control_frame, text="Clear", command=self.clear).grid(row=1, column=1, sticky="ew")
        ttk.Button(control_frame, text="Random", command=self.randomize).grid(row=2, column=0, columnspan=2, sticky="ew")

        ttk.Label(control_frame, text="Muster").grid(row=3, column=0, columnspan=2, pady=(10, 0))
        for index, pattern in enumerate(PATTERNS, start=4):
            ttk.Button(
                control_frame,
                text=pattern.name,
                command=lambda p=pattern: self.spawn_pattern(p),
            ).grid(row=index, column=0, columnspan=2, sticky="ew", pady=1)

        for column in range(2):
            control_frame.columnconfigure(column, weight=1)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.draw()

    def view_to_world(self, x: int, y: int) -> tuple[int, int]:
        return x + self.offset_x, y + self.offset_y

    def world_to_view(self, x: int, y: int) -> tuple[int, int]:
        return x - self.offset_x, y - self.offset_y

    def on_click(self, event: tk.Event) -> None:
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        wx, wy = self.view_to_world(x, y)
        self.game.toggle(wx, wy)
        self.draw()

    def draw(self) -> None:
        self.canvas.delete("all")
        for x, y in self.game.alive:
            vx, vy = self.world_to_view(x, y)
            if 0 <= vx < self.view_width and 0 <= vy < self.view_height:
                x0 = vx * self.cell_size
                y0 = vy * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="#222", outline="")

    def start(self) -> None:
        if self.running:
            return
        self.running = True
        self.tick()

    def stop(self) -> None:
        self.running = False
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

    def tick(self) -> None:
        if not self.running:
            return
        self.game.step()
        self.draw()
        self.after_id = self.root.after(100, self.tick)

    def step_once(self) -> None:
        self.game.step()
        self.draw()

    def clear(self) -> None:
        self.stop()
        self.game.clear()
        self.draw()

    def randomize(self) -> None:
        self.stop()
        self.game.clear()
        chance = 0.15
        for y in range(self.view_height):
            for x in range(self.view_width):
                if random.random() < chance:
                    wx, wy = self.view_to_world(x, y)
                    self.game.set_alive([(wx, wy)])
        self.draw()

    def spawn_pattern(self, pattern: Pattern) -> None:
        self.stop()
        self.game.clear()
        start_x = self.offset_x + (self.view_width // 2) - 10
        start_y = self.offset_y + (self.view_height // 2) - 10
        cells = [(start_x + x, start_y + y) for x, y in pattern.cells]
        self.game.set_alive(cells)
        self.draw()
