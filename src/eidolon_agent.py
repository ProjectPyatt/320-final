"""
EIDOLON-7 Agent
ADK Agent for Dungeon Ascend Generator
Provides knowledge services and natural language dungeon generation
"""

import json
import os
from typing import Dict, Optional, List
from .generator import DungeonGenerator
from .renderer import ASCIIRenderer
from .quality_metrics import DungeonQualityMetrics


class Eidolon7Agent:
    """
    EIDOLON-7: Ancient Dungeon Overseer and Knowledge Archive
    
    An ADK agent that provides:
    1. Knowledge Service - Answer questions about biomes, enemies, resources, and game mechanics
    2. Generation Service - Generate and evaluate dungeons based on natural language requests
    3. Evaluation Service - Analyze dungeon quality and provide feedback
    """
    
    def __init__(self, data_dir: str = "data"):
        self.name = "EIDOLON-7"
        self.data_dir = data_dir
        self.biomes_data = self._load_biomes()
        self.enemies_data = self._load_enemies()
        self.resources_data = self._load_resources()
        self.generator = DungeonGenerator()
        self.renderer = ASCIIRenderer()
        
    def _load_biomes(self) -> Dict:
        """Load biome data from JSON"""
        path = os.path.join(self.data_dir, 'biomes.json')
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def _load_enemies(self) -> Dict:
        """Load enemy data from JSON"""
        path = os.path.join(self.data_dir, 'enemies.json')
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def _load_resources(self) -> Dict:
        """Load resource data from JSON"""
        path = os.path.join(self.data_dir, 'resources.json')
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    # =========================================================================
    # KNOWLEDGE SERVICE - ADK Natural Language Service for Dungeon Information
    # =========================================================================
    
    def query_biome(self, biome_name: str) -> Optional[Dict]:
        """
        Query information about a specific biome
        
        Args:
            biome_name: Name of the biome (e.g., 'jungle', 'snow', 'vampire')
        
        Returns:
            Dictionary with biome information or None if not found
        """
        biome_name = biome_name.lower().replace(' ', '_')
        
        if biome_name not in self.biomes_data:
            return None
        
        biome = self.biomes_data[biome_name]
        return {
            'name': biome_name,
            'theme': biome.get('theme', 'Unknown'),
            'characteristics': biome.get('characteristics', []),
            'resources': biome.get('resources', []),
            'common_enemies': biome.get('common_enemies', []),
            'mini_bosses': biome.get('mini_bosses', []),
            'mega_boss': biome.get('mega_boss', 'Unknown')
        }
    
    def query_enemy(self, enemy_name: str) -> Optional[Dict]:
        """
        Query information about a specific enemy
        
        Args:
            enemy_name: Name of the enemy
        
        Returns:
            Dictionary with enemy information or None if not found
        """
        enemy_name = enemy_name.lower().replace(' ', '_')
        
        if enemy_name not in self.enemies_data:
            return None
        
        enemy = self.enemies_data[enemy_name]
        return {
            'name': enemy.get('name', enemy_name),
            'tier': enemy.get('tier', 'Unknown'),
            'biomes': enemy.get('biomes', []),
            'base_hp': enemy.get('base_hp', 0),
            'base_damage': enemy.get('base_damage', 0),
            'description': enemy.get('description', 'No description available')
        }
    
    def query_resource(self, resource_name: str) -> Optional[Dict]:
        """
        Query information about a specific resource
        
        Args:
            resource_name: Name of the resource
        
        Returns:
            Dictionary with resource information or None if not found
        """
        resource_name = resource_name.lower().replace(' ', '_')
        
        if resource_name not in self.resources_data:
            return None
        
        resource = self.resources_data[resource_name]
        return {
            'name': resource.get('name', resource_name),
            'rarity': resource.get('rarity', 'Unknown'),
            'biomes': resource.get('biomes', []),
            'description': resource.get('description', 'No description available')
        }
    
    def get_floor_info(self, floor_number: int) -> Dict:
        """
        Get information about a specific floor's parameters
        
        Args:
            floor_number: Floor number (1-100)
        
        Returns:
            Dictionary with floor progression information
        """
        is_boss_floor = floor_number % 11 == 0 and floor_number > 0
        
        # Determine tier
        if floor_number <= 10:
            tier = "Tutorial Zone"
            difficulty = "Very Easy"
            expected_rooms = "4-6"
            expected_enemies = "5-8"
            boss_chance = "10%"
        elif floor_number <= 20:
            tier = "Early Game"
            difficulty = "Easy"
            expected_rooms = "5-8"
            expected_enemies = "8-12"
            boss_chance = "20%"
        elif floor_number <= 40:
            tier = "Mid Game"
            difficulty = "Moderate"
            expected_rooms = "7-10"
            expected_enemies = "12-18"
            boss_chance = "30%"
        elif floor_number <= 70:
            tier = "Late-Mid Game"
            difficulty = "Hard"
            expected_rooms = "8-12"
            expected_enemies = "15-22"
            boss_chance = "40%"
        else:
            tier = "Endgame"
            difficulty = "Very Hard"
            expected_rooms = "10-15"
            expected_enemies = "18-30"
            boss_chance = "50%"
        
        # Determine available biomes
        if floor_number <= 10:
            biomes = ["Jungle", "Snow", "Swamp"]
        elif floor_number <= 30:
            biomes = ["Jungle", "Snow", "Swamp", "Vampire", "Werewolf", "Rocky", "Satanic", "Fairy"]
        elif floor_number <= 70:
            biomes = ["All biomes including Astral Void (rare)"]
        else:
            biomes = ["All biomes with emphasis on Astral Void"]
        
        return {
            'floor': floor_number,
            'tier': tier,
            'difficulty': difficulty,
            'is_boss_floor': is_boss_floor,
            'expected_rooms': expected_rooms,
            'expected_enemies': expected_enemies,
            'mini_boss_chance': boss_chance,
            'available_biomes': biomes
        }
    
    def list_biomes(self) -> List[str]:
        """Get list of all available biomes"""
        return list(self.biomes_data.keys())
    
    def list_enemies_by_biome(self, biome_name: str) -> Dict[str, List[str]]:
        """
        Get all enemies that can spawn in a biome
        
        Args:
            biome_name: Name of the biome
        
        Returns:
            Dictionary with enemy lists by tier
        """
        biome_name = biome_name.lower().replace(' ', '_')
        
        if biome_name not in self.biomes_data:
            return {}
        
        biome = self.biomes_data[biome_name]
        return {
            'common': biome.get('common_enemies', []),
            'mini_bosses': biome.get('mini_bosses', []),
            'mega_boss': biome.get('mega_boss', 'None')
        }
    
    def list_resources_by_biome(self, biome_name: str) -> List[str]:
        """
        Get all resources that can be found in a biome
        
        Args:
            biome_name: Name of the biome
        
        Returns:
            List of resource names
        """
        biome_name = biome_name.lower().replace(' ', '_')
        
        if biome_name not in self.biomes_data:
            return []
        
        return self.biomes_data[biome_name].get('resources', [])
    
    # =========================================================================
    # GENERATION SERVICE - ADK Natural Language Dungeon Generation
    # =========================================================================
    
    def generate_dungeon(self, floor_number: int = 1, width: int = 60, 
                        height: int = 40, biome: Optional[str] = None,
                        seed: Optional[int] = None) -> Dict:
        """
        Generate a dungeon and evaluate its quality
        
        Args:
            floor_number: Floor number to generate (1-100)
            width: Dungeon width
            height: Dungeon height
            biome: Optional specific biome to use
            seed: Optional random seed
        
        Returns:
            Dictionary with dungeon, ASCII render, and quality metrics
        """
        # Create generator with seed if provided
        if seed is not None:
            self.generator = DungeonGenerator(seed=seed)
        
        # Generate dungeon
        dungeon = self.generator.generate(floor_number, width, height)
        
        # Override biome if specified
        if biome:
            biome = biome.lower().replace(' ', '_')
            if biome in self.biomes_data:
                dungeon.biome = biome
        
        # Evaluate quality
        quality_eval = DungeonQualityMetrics(dungeon)
        quality_results = quality_eval.evaluate()
        
        # Render ASCII
        enemies_overlay = [(pos[0], pos[1], 'E' if i == 0 else 'e') 
                          for i, pos in enumerate(dungeon.enemies)]
        resources_overlay = [(pos[0], pos[1], '$') for pos in dungeon.resources]
        ascii_render = self.renderer.render_with_overlay(
            dungeon, enemies_overlay, resources_overlay
        )
        
        return {
            'dungeon': dungeon,
            'ascii_render': ascii_render,
            'quality': quality_results,
            'quality_report': quality_eval.generate_report(),
            'floor_info': self.get_floor_info(floor_number)
        }
    
    def evaluate_dungeon(self, dungeon) -> Dict:
        """
        Evaluate an existing dungeon's quality
        
        Args:
            dungeon: Dungeon object to evaluate
        
        Returns:
            Dictionary with quality metrics and report
        """
        quality_eval = DungeonQualityMetrics(dungeon)
        quality_results = quality_eval.evaluate()
        
        return {
            'quality': quality_results,
            'quality_report': quality_eval.generate_report()
        }
    
    # =========================================================================
    # NARRATION & LORE - Optional flavor text for responses
    # =========================================================================
    
    def get_greeting(self) -> str:
        """Return EIDOLON-7's greeting message"""
        return (
            "⚡ EIDOLON-7 ONLINE ⚡\n"
            "Ancient Dungeon Overseer | Knowledge Archive | Quality Evaluator\n"
            "I am the eternal witness to countless dungeon manifestations.\n"
            "Query me for knowledge, or command me to generate and evaluate floors.\n"
        )
    
    def narrate_floor_generation(self, floor_number: int, biome: str, 
                                 quality_score: float) -> str:
        """
        Generate narrative flavor text for a floor generation
        
        Args:
            floor_number: The generated floor number
            biome: The biome type
            quality_score: The DQS score (0-1)
        
        Returns:
            Narrative text
        """
        grade_narration = {
            'S': "A perfect manifestation. The architects themselves would be proud.",
            'A': "Exceptional structure. This floor approaches ideal form.",
            'B': "A solid construction. Functional and navigable.",
            'C': "Adequate, though flawed. Improvements could be made.",
            'F': "This structure contains critical deficiencies."
        }
        
        if quality_score >= 0.95:
            grade = 'S'
        elif quality_score >= 0.85:
            grade = 'A'
        elif quality_score >= 0.70:
            grade = 'B'
        elif quality_score >= 0.50:
            grade = 'C'
        else:
            grade = 'F'
        
        biome_narration = {
            'jungle': "Dense vegetation obscures the paths ahead.",
            'snow': "Frost crystallizes on ancient stone.",
            'swamp': "Murky waters conceal treacherous depths.",
            'vampire': "Shadows dance in gothic corridors.",
            'werewolf': "The full moon illuminates primal territory.",
            'rocky': "Stone echoes with the weight of ages.",
            'satanic': "Infernal flames illuminate twisted passages.",
            'fairy': "Enchantments shimmer in the air.",
            'astral_void': "Cosmic energies warp space itself."
        }
        
        return (
            f"Floor {floor_number} has manifested within the {biome.upper()} realm.\n"
            f"{biome_narration.get(biome, 'The dungeon takes form.')}\n"
            f"Quality Assessment: {grade_narration.get(grade, 'Analysis complete.')}"
        )
