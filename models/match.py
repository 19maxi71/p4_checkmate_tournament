import sys
import os

# Chemin relatif
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

import json
from dataclasses import dataclass
from typing import Optional
from models.player import Player


@dataclass
class Match:
    player1: Player
    player2: Player
    result: Optional[str] = None

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Match à partir d'un dictionnaire."""
        return cls(
            player1=Player.from_dict(data.get("player1")),
            player2=Player.from_dict(data.get("player2")),
            result=data.get("result", None),
        )