"""
Enemy Module
Enemy data structures and spawn rules
"""

import json
from typing import Dict, List, Optional
from pathlib import Path
from enum import Enum


class EnemyTier(Enum):
    """Enemy difficulty tiers"""
    COMMON = "common"
    MINI_BOSS = "mini_boss"
    MEGA_BOSS = "mega_boss"


class Enemy:
    """Represents an enemy with its properties"""

    def __init__(self, name: str, data: dict):
        self.name = name
        self.tier = EnemyTier(data.get('tier', 'common'))
        self.biomes = data.get('biomes', [])
        self.description = data.get('description', '')
        self.abilities = data.get('abilities', [])
        self.base_hp = data.get('base_hp', 100)
        self.base_damage = data.get('base_damage', 10)

    def get_scaled_hp(self, floor_number: int, difficulty_multiplier: float) -> int:
        """Calculate scaled HP for this enemy"""
        floor_multiplier = 1 + (floor_number / 100)
        return int(self.base_hp * difficulty_multiplier * floor_multiplier)

    def get_scaled_damage(self, difficulty_multiplier: float) -> int:
        """Calculate scaled damage for this enemy"""
        return int(self.base_damage * difficulty_multiplier)

    def can_spawn_in_biome(self, biome: str) -> bool:
        """Check if this enemy can spawn in the given biome"""
        return biome in self.biomes

    def __repr__(self):
        return f"Enemy({self.name}, {self.tier.value})"


class EnemyManager:
    """Manages enemy data and spawn logic"""

    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            base_path = Path(__file__).parent.parent
            data_path = base_path / 'data' / 'enemies.json'

        self.data_path = data_path
        self.enemies: Dict[str, Enemy] = {}
        self.load_enemies()

    def load_enemies(self):
        """Load enemy data from JSON file"""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                for enemy_name, enemy_data in data.items():
                    self.enemies[enemy_name] = Enemy(enemy_name, enemy_data)
        except FileNotFoundError:
            print(f"Warning: Enemy data file not found at {self.data_path}")
        except json.JSONDecodeError as e:
            print(f"Error parsing enemy data: {e}")

    def get_enemy(self, name: str) -> Optional[Enemy]:
        """Get an enemy by name"""
        return self.enemies.get(name)

    def get_enemies_for_biome(self, biome: str, tier: Optional[EnemyTier] = None) -> List[Enemy]:
        """Get all enemies that can spawn in a biome, optionally filtered by tier"""
        result = []
        for enemy in self.enemies.values():
            if enemy.can_spawn_in_biome(biome):
                if tier is None or enemy.tier == tier:
                    result.append(enemy)
        return result

    def get_mega_boss_for_biome(self, biome: str) -> Optional[Enemy]:
        """Get the mega boss for a specific biome"""
        for enemy in self.enemies.values():
            if enemy.tier == EnemyTier.MEGA_BOSS and enemy.can_spawn_in_biome(biome):
                return enemy
        return None
