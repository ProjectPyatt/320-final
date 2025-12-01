"""
Dungeon Quality Score (DQS) Module
Comprehensive evaluation metrics for dungeon quality assessment
"""

from typing import Dict, Tuple
from .dungeon import Dungeon
from .pathfinding import PathfindingValidator


class DungeonQualityMetrics:
    """Evaluates dungeon quality using multiple metrics"""

    def __init__(self, dungeon: Dungeon):
        self.dungeon = dungeon
        self.validator = PathfindingValidator(dungeon)

    def evaluate(self) -> Dict:
        """
        Perform comprehensive dungeon quality evaluation
        
        Returns:
            Dictionary containing all quality metrics and overall DQS score
        """
        # Get basic validation results
        validation = self.validator.validate_connectivity()
        
        # Calculate individual metrics
        pathability = self._calculate_pathability(validation)
        resource_accessibility = self._calculate_resource_accessibility(validation)
        room_connectivity = self._calculate_room_connectivity(validation)
        space_efficiency = self._calculate_space_efficiency(validation)
        
        # Calculate overall DQS (weighted average)
        dqs = self._calculate_dqs(
            pathability,
            resource_accessibility,
            room_connectivity,
            space_efficiency
        )
        
        return {
            'dungeon_quality_score': round(dqs, 3),
            'metrics': {
                'pathability': round(pathability, 3),
                'resource_accessibility': round(resource_accessibility, 3),
                'room_connectivity': round(room_connectivity, 3),
                'space_efficiency': round(space_efficiency, 3)
            },
            'raw_data': {
                'connected_rooms': validation['connected_rooms'],
                'total_rooms': validation['total_rooms'],
                'accessible_resources': validation['accessible_resources'],
                'total_resources': validation['total_resources'],
                'reachable_tiles': validation['reachable_tiles'],
                'total_tiles': self.dungeon.width * self.dungeon.height,
                'total_enemies': len(self.dungeon.enemies)
            },
            'validation': {
                'valid': validation['valid'],
                'all_rooms_connected': validation['connected_rooms'] == validation['total_rooms'],
                'all_resources_accessible': validation['accessible_resources'] == validation['total_resources']
            },
            'grade': self._get_quality_grade(dqs)
        }

    def _calculate_pathability(self, validation: Dict) -> float:
        """
        Calculate pathability percentage (reachable tiles / total walkable area)
        
        Returns:
            Float between 0 and 1
        """
        total_tiles = self.dungeon.width * self.dungeon.height
        reachable_tiles = validation['reachable_tiles']
        
        if total_tiles == 0:
            return 0.0
        
        # Normalize by reasonable expectation (not all tiles should be walkable)
        # A good dungeon should have 30-60% walkable space
        pathability_ratio = reachable_tiles / total_tiles
        
        # Scale to 0-1 where 0.4 (40% walkable) = 1.0 score
        if pathability_ratio >= 0.4:
            return 1.0
        else:
            return pathability_ratio / 0.4

    def _calculate_resource_accessibility(self, validation: Dict) -> float:
        """
        Calculate resource accessibility percentage
        
        Returns:
            Float between 0 and 1
        """
        total = validation['total_resources']
        accessible = validation['accessible_resources']
        
        if total == 0:
            return 1.0  # No resources = technically all accessible
        
        return accessible / total

    def _calculate_room_connectivity(self, validation: Dict) -> float:
        """
        Calculate room connectivity percentage
        
        Returns:
            Float between 0 and 1
        """
        total = validation['total_rooms']
        connected = validation['connected_rooms']
        
        if total == 0:
            return 0.0
        
        return connected / total

    def _calculate_space_efficiency(self, validation: Dict) -> float:
        """
        Calculate space efficiency (how well the space is utilized)
        
        Returns:
            Float between 0 and 1
        """
        total_tiles = self.dungeon.width * self.dungeon.height
        reachable_tiles = validation['reachable_tiles']
        
        if total_tiles == 0:
            return 0.0
        
        # Calculate room area
        room_area = sum(room.get_area() for room in self.dungeon.rooms)
        
        # Good efficiency is when reachable tiles are well distributed
        # and room density is balanced
        room_density = room_area / total_tiles if total_tiles > 0 else 0
        
        # Optimal room density is around 20-40%
        if 0.2 <= room_density <= 0.4:
            density_score = 1.0
        elif room_density < 0.2:
            density_score = room_density / 0.2
        else:
            density_score = max(0, 1.0 - (room_density - 0.4) / 0.3)
        
        return density_score

    def _calculate_dqs(self, pathability: float, resource_access: float, 
                      room_connectivity: float, space_efficiency: float) -> float:
        """
        Calculate overall Dungeon Quality Score using weighted average
        
        Weights:
        - Room Connectivity: 35% (most critical)
        - Resource Accessibility: 30% (very important)
        - Pathability: 20% (important)
        - Space Efficiency: 15% (nice to have)
        
        Returns:
            Float between 0 and 1
        """
        weights = {
            'room_connectivity': 0.35,
            'resource_accessibility': 0.30,
            'pathability': 0.20,
            'space_efficiency': 0.15
        }
        
        dqs = (
            room_connectivity * weights['room_connectivity'] +
            resource_access * weights['resource_accessibility'] +
            pathability * weights['pathability'] +
            space_efficiency * weights['space_efficiency']
        )
        
        return max(0.0, min(1.0, dqs))

    def _get_quality_grade(self, dqs: float) -> Tuple[str, str]:
        """
        Convert DQS score to letter grade and description
        
        Returns:
            Tuple of (grade, description)
        """
        if dqs >= 0.95:
            return ('S', 'Perfect - Legendary Quality')
        elif dqs >= 0.90:
            return ('A+', 'Exceptional - Near Perfect')
        elif dqs >= 0.85:
            return ('A', 'Excellent - High Quality')
        elif dqs >= 0.80:
            return ('A-', 'Very Good - Minor Issues')
        elif dqs >= 0.75:
            return ('B+', 'Good - Playable')
        elif dqs >= 0.70:
            return ('B', 'Above Average - Some Issues')
        elif dqs >= 0.65:
            return ('B-', 'Average - Noticeable Issues')
        elif dqs >= 0.60:
            return ('C+', 'Below Average - Significant Issues')
        elif dqs >= 0.50:
            return ('C', 'Poor - Major Problems')
        else:
            return ('F', 'Unacceptable - Critically Flawed')

    def generate_report(self) -> str:
        """
        Generate a human-readable quality report
        
        Returns:
            Formatted string report
        """
        results = self.evaluate()
        
        grade, description = results['grade']
        
        report = []
        report.append("=" * 60)
        report.append("DUNGEON QUALITY EVALUATION REPORT")
        report.append("=" * 60)
        report.append(f"Floor: {self.dungeon.floor_number}")
        report.append(f"Biome: {self.dungeon.biome.upper() if self.dungeon.biome else 'UNKNOWN'}")
        report.append(f"Dimensions: {self.dungeon.width}x{self.dungeon.height}")
        report.append("")
        report.append(f"OVERALL SCORE: {results['dungeon_quality_score']:.3f} [{grade}]")
        report.append(f"Quality: {description}")
        report.append("")
        report.append("METRICS BREAKDOWN:")
        report.append("-" * 60)
        
        metrics = results['metrics']
        report.append(f"  Room Connectivity:       {metrics['room_connectivity']:.1%} "
                     f"({results['raw_data']['connected_rooms']}/{results['raw_data']['total_rooms']} rooms)")
        report.append(f"  Resource Accessibility:  {metrics['resource_accessibility']:.1%} "
                     f"({results['raw_data']['accessible_resources']}/{results['raw_data']['total_resources']} resources)")
        report.append(f"  Pathability:             {metrics['pathability']:.1%} "
                     f"({results['raw_data']['reachable_tiles']} reachable tiles)")
        report.append(f"  Space Efficiency:        {metrics['space_efficiency']:.1%}")
        report.append("")
        report.append("RAW STATISTICS:")
        report.append("-" * 60)
        report.append(f"  Total Rooms:             {results['raw_data']['total_rooms']}")
        report.append(f"  Total Enemies:           {results['raw_data']['total_enemies']}")
        report.append(f"  Total Resources:         {results['raw_data']['total_resources']}")
        report.append(f"  Reachable Tiles:         {results['raw_data']['reachable_tiles']}")
        report.append("")
        
        # Validation status
        if results['validation']['valid']:
            report.append("✓ VALIDATION: PASSED")
        else:
            report.append("✗ VALIDATION: FAILED")
            if not results['validation']['all_rooms_connected']:
                report.append("  - Some rooms are not connected")
            if not results['validation']['all_resources_accessible']:
                report.append("  - Some resources are not accessible")
        
        report.append("=" * 60)
        
        return "\n".join(report)
