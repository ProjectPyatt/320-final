"""
Renderer Module
ASCII rendering for dungeon visualization
"""

from .dungeon import Dungeon, TileType
from typing import Optional


class ASCIIRenderer:
    """Renders dungeons as ASCII art"""

    def __init__(self):
        self.symbols = {
            TileType.WALL: '#',
            TileType.FLOOR: '.',
            TileType.CORRIDOR: ',',
            TileType.DOOR: '+',
            TileType.ENTRANCE: 'E',
            TileType.EXIT: 'X',
            TileType.EMPTY: ' '
        }

    def render(self, dungeon: Dungeon, show_info: bool = True) -> str:
        """
        Render the dungeon as ASCII art

        Args:
            dungeon: The dungeon to render
            show_info: Whether to show dungeon info header

        Returns:
            String representation of the dungeon
        """
        lines = []

        if show_info:
            lines.append(self._render_header(dungeon))
            lines.append("")

        # Render the grid
        for row in dungeon.grid:
            line = ""
            for tile in row:
                line += self.symbols.get(tile, ' ')
            lines.append(line)

        if show_info:
            lines.append("")
            lines.append(self._render_footer(dungeon))

        return "\n".join(lines)

    def _render_header(self, dungeon: Dungeon) -> str:
        """Render dungeon information header"""
        header = f"=== FLOOR {dungeon.floor_number} ==="
        if dungeon.biome:
            header += f" | Biome: {dungeon.biome.upper()}"
        header += f" | Rooms: {len(dungeon.rooms)}"
        return header

    def _render_footer(self, dungeon: Dungeon) -> str:
        """Render dungeon statistics footer"""
        stats = []
        stats.append(f"Enemies: {len(dungeon.enemies)}")
        stats.append(f"Resources: {len(dungeon.resources)}")
        return " | ".join(stats)

    def render_with_overlay(self, dungeon: Dungeon, enemies: list = None, resources: list = None) -> str:
        """
        Render dungeon with enemies and resources overlaid

        Args:
            dungeon: The dungeon to render
            enemies: List of enemy positions [(x, y, symbol), ...]
            resources: List of resource positions [(x, y, symbol), ...]

        Returns:
            String representation with overlays
        """
        # Create a copy of the grid
        grid_copy = [row[:] for row in dungeon.grid]

        # Overlay resources
        if resources:
            for x, y, symbol in resources:
                if 0 <= y < len(grid_copy) and 0 <= x < len(grid_copy[0]):
                    if dungeon.is_walkable(x, y):
                        grid_copy[y][x] = symbol

        # Overlay enemies (on top of resources)
        if enemies:
            for x, y, symbol in enemies:
                if 0 <= y < len(grid_copy) and 0 <= x < len(grid_copy[0]):
                    if dungeon.is_walkable(x, y):
                        grid_copy[y][x] = symbol

        lines = [self._render_header(dungeon), ""]

        for row in grid_copy:
            line = ""
            for tile in row:
                if isinstance(tile, TileType):
                    line += self.symbols.get(tile, ' ')
                else:
                    line += tile  # Already a symbol
            lines.append(line)

        lines.append("")
        lines.append(self._render_footer(dungeon))

        return "\n".join(lines)
