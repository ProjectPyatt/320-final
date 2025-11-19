"""
Generator Module
Procedural generation algorithms for dungeon creation
"""

import random
from typing import List, Tuple, Optional
from .dungeon import Dungeon, Room, TileType


class DungeonGenerator:
    """Handles procedural generation of dungeon floors"""

    def __init__(self, seed: Optional[int] = None):
        self.seed = seed
        if seed is not None:
            random.seed(seed)

    def generate(self, floor_number: int, width: int = 60, height: int = 40) -> Dungeon:
        """
        Generate a complete dungeon floor

        Args:
            floor_number: The floor level (1-100)
            width: Dungeon grid width
            height: Dungeon grid height

        Returns:
            Generated Dungeon instance
        """
        dungeon = Dungeon(width, height, floor_number)

        # Determine floor parameters based on progression
        params = self._get_floor_parameters(floor_number)

        # Select biome
        biome = self._select_biome(floor_number)
        dungeon.biome = biome

        # Generate rooms
        rooms = self._generate_rooms(dungeon, params['room_count'], params['is_boss_floor'])

        # Connect rooms with corridors
        self._connect_rooms(dungeon)

        # Place enemies (placeholder)
        # TODO: Implement enemy placement

        # Place resources (placeholder)
        # TODO: Implement resource placement

        return dungeon

    def _get_floor_parameters(self, floor_number: int) -> dict:
        """Determine parameters based on floor progression"""
        is_boss_floor = floor_number % 11 == 0 and floor_number > 0

        if floor_number <= 10:
            # Tutorial Zone
            return {
                'room_count': random.randint(4, 6),
                'enemy_density': 'low',
                'enemy_count': random.randint(5, 8),
                'mini_boss_chance': 0.1,
                'difficulty_multiplier': 1.0,
                'is_boss_floor': is_boss_floor
            }
        elif floor_number <= 20:
            # Early Game
            return {
                'room_count': random.randint(5, 8),
                'enemy_density': 'medium',
                'enemy_count': random.randint(8, 12),
                'mini_boss_chance': 0.2,
                'difficulty_multiplier': 1.2,
                'is_boss_floor': is_boss_floor
            }
        elif floor_number <= 40:
            # Mid Game
            return {
                'room_count': random.randint(7, 10),
                'enemy_density': 'high',
                'enemy_count': random.randint(12, 18),
                'mini_boss_chance': 0.3,
                'difficulty_multiplier': 1.8,
                'is_boss_floor': is_boss_floor
            }
        elif floor_number <= 70:
            # Late-Mid Game
            return {
                'room_count': random.randint(8, 12),
                'enemy_density': 'high',
                'enemy_count': random.randint(15, 22),
                'mini_boss_chance': 0.4,
                'difficulty_multiplier': 2.5,
                'is_boss_floor': is_boss_floor
            }
        else:
            # Endgame
            return {
                'room_count': random.randint(10, 15),
                'enemy_density': 'very_high',
                'enemy_count': random.randint(18, 30),
                'mini_boss_chance': 0.5,
                'difficulty_multiplier': 4.0,
                'is_boss_floor': is_boss_floor
            }

    def _select_biome(self, floor_number: int) -> str:
        """Select biome based on floor progression"""
        if floor_number <= 10:
            # Early floors: simple biomes
            return random.choice(['jungle', 'snow', 'swamp'])
        elif floor_number <= 30:
            # Mid-early: all except astral
            biomes = ['jungle', 'snow', 'swamp', 'vampire', 'werewolf', 'rocky', 'satanic', 'fairy']
            return random.choice(biomes)
        elif floor_number <= 70:
            # Late-mid: emphasis on themed biomes
            biomes = ['jungle', 'snow', 'swamp', 'vampire', 'vampire', 'werewolf', 'werewolf',
                     'rocky', 'satanic', 'satanic', 'fairy', 'astral_void']
            return random.choice(biomes)
        else:
            # Endgame: emphasis on astral void
            biomes = ['jungle', 'snow', 'swamp', 'vampire', 'werewolf', 'rocky', 'satanic',
                     'fairy', 'astral_void', 'astral_void', 'astral_void']
            return random.choice(biomes)

    def _generate_rooms(self, dungeon: Dungeon, room_count: int, is_boss_floor: bool) -> List[Room]:
        """Generate non-overlapping rooms"""
        rooms = []
        max_attempts = 1000

        for i in range(room_count):
            for attempt in range(max_attempts):
                # Determine room size
                if is_boss_floor and i == 0:
                    # First room on boss floor is the boss room
                    width = random.randint(12, 15)
                    height = random.randint(12, 15)
                else:
                    room_size = random.choice(['small', 'medium', 'large'])
                    if room_size == 'small':
                        width = random.randint(3, 5)
                        height = random.randint(3, 5)
                    elif room_size == 'medium':
                        width = random.randint(6, 10)
                        height = random.randint(6, 10)
                    else:  # large
                        width = random.randint(11, 15)
                        height = random.randint(11, 15)

                # Random position
                x = random.randint(1, dungeon.width - width - 1)
                y = random.randint(1, dungeon.height - height - 1)

                # Check for overlap with existing rooms
                new_room = Room(x, y, width, height, len(rooms))

                if not self._room_overlaps(new_room, rooms):
                    if is_boss_floor and i == 0:
                        new_room.is_boss_room = True
                    dungeon.add_room(new_room)
                    rooms.append(new_room)
                    break

        return rooms

    def _room_overlaps(self, new_room: Room, existing_rooms: List[Room], buffer: int = 2) -> bool:
        """Check if a room overlaps with existing rooms (with buffer space)"""
        for room in existing_rooms:
            if (new_room.x < room.x + room.width + buffer and
                new_room.x + new_room.width + buffer > room.x and
                new_room.y < room.y + room.height + buffer and
                new_room.y + new_room.height + buffer > room.y):
                return True
        return False

    def _connect_rooms(self, dungeon: Dungeon):
        """Connect all rooms with corridors"""
        if len(dungeon.rooms) < 2:
            return

        # Connect each room to the next one
        for i in range(len(dungeon.rooms) - 1):
            room1 = dungeon.rooms[i]
            room2 = dungeon.rooms[i + 1]
            dungeon.create_corridor(room1.center, room2.center)

        # Optionally add some extra connections for variety
        if len(dungeon.rooms) > 3:
            # Connect first and last room
            dungeon.create_corridor(dungeon.rooms[0].center, dungeon.rooms[-1].center)
