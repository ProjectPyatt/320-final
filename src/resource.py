"""
Resource Module
Resource definitions and placement logic
"""

import json
from typing import Dict, List, Optional
from pathlib import Path
from enum import Enum


class ResourceRarity(Enum):
    """Resource rarity tiers"""
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"

    def get_drop_rate(self) -> float:
        """Get the drop rate for this rarity"""
        rates = {
            ResourceRarity.COMMON: 0.6,
            ResourceRarity.UNCOMMON: 0.3,
            ResourceRarity.RARE: 0.1
        }
        return rates[self]


class Resource:
    """Represents a resource that can be found in dungeons"""

    def __init__(self, name: str, data: dict):
        self.name = name
        self.rarity = ResourceRarity(data.get('rarity', 'common'))
        self.biome = data.get('biome', '')
        self.description = data.get('description', '')
        self.value = data.get('value', 1)

    def __repr__(self):
        return f"Resource({self.name}, {self.rarity.value})"


class ResourceManager:
    """Manages resource data and placement"""

    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            base_path = Path(__file__).parent.parent
            data_path = base_path / 'data' / 'resources.json'

        self.data_path = data_path
        self.resources: Dict[str, Resource] = {}
        self.load_resources()

    def load_resources(self):
        """Load resource data from JSON file"""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                for resource_name, resource_data in data.items():
                    self.resources[resource_name] = Resource(resource_name, resource_data)
        except FileNotFoundError:
            print(f"Warning: Resource data file not found at {self.data_path}")
        except json.JSONDecodeError as e:
            print(f"Error parsing resource data: {e}")

    def get_resource(self, name: str) -> Optional[Resource]:
        """Get a resource by name"""
        return self.resources.get(name)

    def get_resources_for_biome(self, biome: str) -> List[Resource]:
        """Get all resources that can be found in a biome"""
        return [r for r in self.resources.values() if r.biome == biome]

    def get_resources_by_rarity(self, biome: str, rarity: ResourceRarity) -> List[Resource]:
        """Get resources for a biome filtered by rarity"""
        return [r for r in self.get_resources_for_biome(biome) if r.rarity == rarity]
