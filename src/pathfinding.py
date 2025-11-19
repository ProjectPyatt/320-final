"""
Pathfinding Module
AI pathfinding algorithms for dungeon validation
"""

from typing import List, Tuple, Set, Optional
from collections import deque
from .dungeon import Dungeon


class PathfindingValidator:
    """Validates dungeon connectivity using pathfinding algorithms"""

    def __init__(self, dungeon: Dungeon):
        self.dungeon = dungeon

    def validate_connectivity(self, start_pos: Optional[Tuple[int, int]] = None) -> dict:
        """
        Validate that all rooms and resources are reachable

        Returns:
            Dictionary with validation results
        """
        if not self.dungeon.rooms:
            return {
                'valid': False,
                'reason': 'No rooms in dungeon',
                'connected_rooms': 0,
                'total_rooms': 0
            }

        # Use first room center as start if not specified
        if start_pos is None:
            start_pos = self.dungeon.rooms[0].center

        # Find all reachable positions
        reachable = self.bfs_reachability(start_pos)

        # Check room connectivity
        connected_rooms = 0
        for room in self.dungeon.rooms:
            if room.center in reachable:
                connected_rooms += 1

        # Check resource accessibility
        accessible_resources = 0
        for resource_pos in self.dungeon.resources:
            if resource_pos in reachable:
                accessible_resources += 1

        all_rooms_connected = connected_rooms == len(self.dungeon.rooms)
        all_resources_accessible = accessible_resources == len(self.dungeon.resources)

        return {
            'valid': all_rooms_connected and all_resources_accessible,
            'connected_rooms': connected_rooms,
            'total_rooms': len(self.dungeon.rooms),
            'accessible_resources': accessible_resources,
            'total_resources': len(self.dungeon.resources),
            'reachable_tiles': len(reachable)
        }

    def bfs_reachability(self, start: Tuple[int, int]) -> Set[Tuple[int, int]]:
        """
        Breadth-First Search to find all reachable positions from start

        Args:
            start: Starting position (x, y)

        Returns:
            Set of all reachable positions
        """
        if not self.dungeon.is_walkable(start[0], start[1]):
            return set()

        visited = set()
        queue = deque([start])
        visited.add(start)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (nx, ny) not in visited and self.dungeon.is_walkable(nx, ny):
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return visited

    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Find a path between two points using BFS

        Args:
            start: Starting position
            goal: Goal position

        Returns:
            List of positions representing the path, or None if no path exists
        """
        if not self.dungeon.is_walkable(start[0], start[1]) or not self.dungeon.is_walkable(goal[0], goal[1]):
            return None

        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == goal:
                return path

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (nx, ny) not in visited and self.dungeon.is_walkable(nx, ny):
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))

        return None

    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        """Calculate Manhattan distance between two positions"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
