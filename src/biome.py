"""
Biome Module
Biome definitions and management
"""

import json
from typing import Dict, List, Optional
from pathlib import Path


class Biome:
    """Represents a dungeon biome with its characteristics"""

    def __init__(self, name: str, data: dict):
        self.name = name
        self.theme = data.get('theme', '')
        self.characteristics = data.get('characteristics', [])
        self.resources = data.get('resources', [])
        self.common_enemies = data.get('common_enemies', [])
        self.mini_bosses = data.get('mini_bosses', [])
        self.mega_boss = data.get('mega_boss', '')

    def __repr__(self):
        return f"Biome({self.name})"


class BiomeManager:
    """Manages biome data and selection"""

    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            # Default to data/biomes.json relative to this file
            base_path = Path(__file__).parent.parent
            data_path = base_path / 'data' / 'biomes.json'

        self.data_path = data_path
        self.biomes: Dict[str, Biome] = {}
        self.load_biomes()

    def load_biomes(self):
        """Load biome data from JSON file"""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                for biome_name, biome_data in data.items():
                    self.biomes[biome_name] = Biome(biome_name, biome_data)
        except FileNotFoundError:
            print(f"Warning: Biome data file not found at {self.data_path}")
        except json.JSONDecodeError as e:
            print(f"Error parsing biome data: {e}")

    def get_biome(self, name: str) -> Optional[Biome]:
        """Get a biome by name"""
        return self.biomes.get(name)

    def get_all_biomes(self) -> List[str]:
        """Get list of all biome names"""
        return list(self.biomes.keys())
