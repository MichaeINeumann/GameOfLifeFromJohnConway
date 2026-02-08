# Conway's Game of Life (Python)

Dieses Repository implementiert John Conways „Game of Life“ als zellulären Automaten auf einem 2D-Gitter.
Die Spielfläche hat **mindestens 100.000.000 Felder** (Standard: 10.000 × 10.000), wird aber über eine
kleine, schnelle Ansicht dargestellt, damit die Simulation auch auf normalen Rechnern läuft.

## Features

- Minimalistische, nachvollziehbare Core-Logik (sparse set für lebendige Zellen)
- GUI ist gekapselt (Tkinter)
- Buttons für bekannte Muster (Blinker, Toad, Glider, LWSS, Gosper Glider Gun)
- Randomize-Button für einen schnellen Start

## Voraussetzungen

- Python 3.10+
- Tkinter (kommt bei den meisten Python-Installationen bereits mit)

## Setup (venv)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Starten

```bash
python main.py
```

## Bedienung

- Klick auf das Grid toggelt eine Zelle.
- **Start**/ **Stop** steuern die Simulation.
- **Step** berechnet genau einen Tick.
- **Clear** löscht alle Zellen.
- **Random** füllt die Ansicht zufällig.
- Buttons unter „Muster“ erzeugen bekannte Startformationen.
