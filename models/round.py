import sys
import os

# Chemin relatif
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from datetime import datetime
from dataclasses import dataclass, field
from models.match import Match
from typing import Optional, List


@dataclass
class Round:
    name: str
    start_datetime: str
    end_datetime: Optional[str] = None
    matches: List[Match] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Round à partir d'un dictionnaire."""
        round = cls(
            name=data.get("name", "Unknown Round"),
            start_datetime=data.get("start_datetime", "Unknown Start Date"),
            end_datetime=data.get("end_datetime", None),
        )
        round.matches = [
            Match.from_dict(match_data) for match_data in data.get("matches", [])
        ]
        return round
