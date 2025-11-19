"""
Dungeon Module
Main dungeon class representing a single floor
"""

from typing import List, Tuple, Optional
from enum import Enum


class TileType(Enum):
    """Enumeration of tile types in the dungeon"""
    WALL = '#'
    FLOOR = '.'
    CORRIDOR = ','
    DOOR = '+'
    ENTRANCE = 'E'
    EXIT = 'X'
    EMPTY = ' '


class Room:
    """Represents a single room in the dungeon"""

    def __init__(self, x: int, y: int, width: int, height: int, room_id: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room_id = room_id
        self.center = (x + width // 2, y + height // 2)
        self.enemies = []
        self.resources = []
        self.is_boss_room = False

    def contains_point(self, x: int, y: int) -> bool:
        """Check if a point is within this room"""
        return self.x <= x < self.x + self.width and self.y <= y < self.y + self.height

    def get_area(self) -> int:
        """Return the area of the room"""
        return self.width * self.height

    def __repr__(self):
        return f"Room(id={self.room_id}, pos=({self.x},{self.y}), size={self.width}x{self.height})"


class Dungeon:
    """Main dungeon class representing a single floor"""

    def __init__(self, width: int, height: int, floor_number: int):
        self.width = width
        self.height = height
        self.floor_number = floor_number
        self.grid = [[TileType.EMPTY for _ in range(width)] for _ in range(height)]
        self.rooms: List[Room] = []
        self.biome = None
        self.enemies = []
        self.resources = []
        self.entrance_pos = None
        self.exit_pos = None

    def add_room(self, room: Room):
        """Add a room to the dungeon and update the grid"""
        self.rooms.append(room)
        # Fill room with floor tiles
        for y in range(room.y, room.y + room.height):
            for x in range(room.x, room.x + room.width):
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.grid[y][x] = TileType.FLOOR
        # Add walls around the room
        self._add_room_walls(room)

    def _add_room_walls(self, room: Room):
        """Add walls around a room"""
        # Top and bottom walls
        for x in range(room.x, room.x + room.width):
            if 0 <= x < self.width:
                if room.y > 0:
                    self.grid[room.y][x] = TileType.WALL
                if room.y + room.height < self.height:
                    self.grid[room.y + room.height - 1][x] = TileType.WALL
        # Left and right walls
        for y in range(room.y, room.y + room.height):
            if 0 <= y < self.height:
                if room.x > 0:
                    self.grid[y][room.x] = TileType.WALL
                if room.x + room.width < self.width:
                    self.grid[y][room.x + room.width - 1] = TileType.WALL

    def create_corridor(self, start: Tuple[int, int], end: Tuple[int, int]):
        """Create a corridor between two points using L-shaped path"""
        x1, y1 = start
        x2, y2 = end

        # Horizontal then vertical
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if 0 <= x < self.width and 0 <= y1 < self.height:
                if self.grid[y1][x] == TileType.EMPTY:
                    self.grid[y1][x] = TileType.CORRIDOR

        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= x2 < self.width and 0 <= y < self.height:
                if self.grid[y][x2] == TileType.EMPTY:
                    self.grid[y][x2] = TileType.CORRIDOR

    def get_tile(self, x: int, y: int) -> TileType:
        """Get tile type at position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return TileType.EMPTY

    def is_walkable(self, x: int, y: int) -> bool:
        """Check if a position is walkable"""
        tile = self.get_tile(x, y)
        return tile in [TileType.FLOOR, TileType.CORRIDOR, TileType.DOOR, TileType.ENTRANCE, TileType.EXIT]

    def __repr__(self):
        return f"Dungeon(floor={self.floor_number}, biome={self.biome}, rooms={len(self.rooms)})"
