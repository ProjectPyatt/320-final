"""
Main Entry Point
Procedural Dungeon Generator
"""

import argparse
import sys
from src.generator import DungeonGenerator
from src.renderer import ASCIIRenderer
from src.pathfinding import PathfindingValidator


def main():
    parser = argparse.ArgumentParser(
        description='Procedural Dungeon Generator with AI Validation'
    )
    parser.add_argument(
        '--floor',
        type=int,
        default=1,
        help='Floor number to generate (1-100)'
    )
    parser.add_argument(
        '--biome',
        type=str,
        help='Force specific biome (jungle, snow, swamp, etc.)'
    )
    parser.add_argument(
        '--seed',
        type=int,
        help='Random seed for reproducible generation'
    )
    parser.add_argument(
        '--width',
        type=int,
        default=60,
        help='Dungeon width (default: 60)'
    )
    parser.add_argument(
        '--height',
        type=int,
        default=40,
        help='Dungeon height (default: 40)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Save output to file instead of printing to console'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Run pathfinding validation'
    )

    args = parser.parse_args()

    # Validate floor number
    if args.floor < 1 or args.floor > 100:
        print("Error: Floor number must be between 1 and 100")
        sys.exit(1)

    # Create generator
    generator = DungeonGenerator(seed=args.seed)

    print(f"Generating Floor {args.floor}...")
    if args.seed:
        print(f"Using seed: {args.seed}")

    # Generate dungeon
    dungeon = generator.generate(
        floor_number=args.floor,
        width=args.width,
        height=args.height
    )

    # Override biome if specified
    if args.biome:
        dungeon.biome = args.biome

    # Render dungeon
    renderer = ASCIIRenderer()
    output = renderer.render(dungeon, show_info=True)

    # Validate if requested
    if args.validate:
        print("\nRunning pathfinding validation...")
        validator = PathfindingValidator(dungeon)
        results = validator.validate_connectivity()

        print(f"Validation: {'PASS' if results['valid'] else 'FAIL'}")
        print(f"Connected Rooms: {results['connected_rooms']}/{results['total_rooms']}")
        print(f"Accessible Resources: {results['accessible_resources']}/{results['total_resources']}")
        print(f"Reachable Tiles: {results['reachable_tiles']}")
        print()

    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"\nDungeon saved to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
