"""
EIDOLON-7 Interactive CLI
Natural language interface for dungeon knowledge and generation
"""

import argparse
import sys
from src.eidolon_agent import Eidolon7Agent
from src.github_integration import GitHubIssueMonitor


def main():
    parser = argparse.ArgumentParser(
        description='EIDOLON-7: Ancient Dungeon Overseer and Knowledge Archive',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Knowledge queries
  python eidolon.py --query-biome jungle
  python eidolon.py --query-enemy frost_wyrm
  python eidolon.py --query-resource stardust
  python eidolon.py --floor-info 33
  
  # Dungeon generation with evaluation
  python eidolon.py --generate --floor 12
  python eidolon.py --generate --floor 1 --biome rocky
  python eidolon.py --generate --floor 50 --seed 12345
  
  # GitHub issue monitoring
  python eidolon.py --check-issues --project-repo hw9-yourusername
  
  # Interactive mode
  python eidolon.py --interactive
        """
    )
    
    # Knowledge service commands
    knowledge_group = parser.add_argument_group('Knowledge Service')
    knowledge_group.add_argument('--query-biome', type=str, metavar='NAME',
                                 help='Query information about a biome')
    knowledge_group.add_argument('--query-enemy', type=str, metavar='NAME',
                                 help='Query information about an enemy')
    knowledge_group.add_argument('--query-resource', type=str, metavar='NAME',
                                 help='Query information about a resource')
    knowledge_group.add_argument('--floor-info', type=int, metavar='NUM',
                                 help='Get information about a floor (1-100)')
    knowledge_group.add_argument('--list-biomes', action='store_true',
                                 help='List all available biomes')
    knowledge_group.add_argument('--biome-enemies', type=str, metavar='BIOME',
                                 help='List all enemies in a biome')
    knowledge_group.add_argument('--biome-resources', type=str, metavar='BIOME',
                                 help='List all resources in a biome')
    
    # Generation service commands
    generation_group = parser.add_argument_group('Generation Service')
    generation_group.add_argument('--generate', action='store_true',
                                  help='Generate a dungeon floor')
    generation_group.add_argument('--floor', type=int, default=1,
                                  help='Floor number (1-100, default: 1)')
    generation_group.add_argument('--biome', type=str,
                                  help='Force specific biome')
    generation_group.add_argument('--width', type=int, default=60,
                                  help='Dungeon width (default: 60)')
    generation_group.add_argument('--height', type=int, default=40,
                                  help='Dungeon height (default: 40)')
    generation_group.add_argument('--seed', type=int,
                                  help='Random seed for reproducibility')
    generation_group.add_argument('--show-narration', action='store_true',
                                  help='Show EIDOLON-7 narration')
    generation_group.add_argument('--output', type=str,
                                  help='Save output to file')
    
    # GitHub integration commands
    github_group = parser.add_argument_group('GitHub Integration')
    github_group.add_argument('--check-issues', action='store_true',
                             help='Check for mentions in hw9-issues repo')
    github_group.add_argument('--project-repo', type=str,
                             help='Your project repository name')
    github_group.add_argument('--generate-status', action='store_true',
                             help='Generate project status report')
    
    # General commands
    parser.add_argument('--interactive', action='store_true',
                       help='Start interactive mode')
    parser.add_argument('--greeting', action='store_true',
                       help='Show EIDOLON-7 greeting')
    
    args = parser.parse_args()
    
    # Initialize agent
    agent = Eidolon7Agent(data_dir='data')
    
    # Show greeting if requested or no args
    if args.greeting or len(sys.argv) == 1:
        print(agent.get_greeting())
        return
    
    # =========================================================================
    # KNOWLEDGE SERVICE COMMANDS
    # =========================================================================
    
    if args.query_biome:
        biome_info = agent.query_biome(args.query_biome)
        if biome_info:
            print(f"\n{'=' * 60}")
            print(f"BIOME: {biome_info['name'].upper()}")
            print(f"{'=' * 60}")
            print(f"Theme: {biome_info['theme']}")
            print(f"\nCharacteristics:")
            for char in biome_info['characteristics']:
                print(f"  • {char}")
            print(f"\nResources: {', '.join(biome_info['resources'])}")
            print(f"\nCommon Enemies: {', '.join(biome_info['common_enemies'])}")
            print(f"Mini-Bosses: {', '.join(biome_info['mini_bosses'])}")
            print(f"Mega-Boss: {biome_info['mega_boss']}")
            print(f"{'=' * 60}\n")
        else:
            print(f"❌ Biome '{args.query_biome}' not found in archives.")
        return
    
    if args.query_enemy:
        enemy_info = agent.query_enemy(args.query_enemy)
        if enemy_info:
            print(f"\n{'=' * 60}")
            print(f"ENEMY: {enemy_info['name'].upper()}")
            print(f"{'=' * 60}")
            print(f"Tier: {enemy_info['tier']}")
            print(f"Biomes: {', '.join(enemy_info['biomes'])}")
            print(f"Base HP: {enemy_info['base_hp']}")
            print(f"Base Damage: {enemy_info['base_damage']}")
            print(f"\n{enemy_info['description']}")
            print(f"{'=' * 60}\n")
        else:
            print(f"❌ Enemy '{args.query_enemy}' not found in archives.")
        return
    
    if args.query_resource:
        resource_info = agent.query_resource(args.query_resource)
        if resource_info:
            print(f"\n{'=' * 60}")
            print(f"RESOURCE: {resource_info['name'].upper()}")
            print(f"{'=' * 60}")
            print(f"Rarity: {resource_info['rarity']}")
            print(f"Biomes: {', '.join(resource_info['biomes'])}")
            print(f"\n{resource_info['description']}")
            print(f"{'=' * 60}\n")
        else:
            print(f"❌ Resource '{args.query_resource}' not found in archives.")
        return
    
    if args.floor_info:
        floor_info = agent.get_floor_info(args.floor_info)
        print(f"\n{'=' * 60}")
        print(f"FLOOR {floor_info['floor']} INFORMATION")
        print(f"{'=' * 60}")
        print(f"Tier: {floor_info['tier']}")
        print(f"Difficulty: {floor_info['difficulty']}")
        print(f"Boss Floor: {'Yes - Mega-Boss will spawn' if floor_info['is_boss_floor'] else 'No'}")
        print(f"Expected Rooms: {floor_info['expected_rooms']}")
        print(f"Expected Enemies: {floor_info['expected_enemies']}")
        print(f"Mini-Boss Chance: {floor_info['mini_boss_chance']}")
        print(f"\nAvailable Biomes:")
        for biome in floor_info['available_biomes']:
            print(f"  • {biome}")
        print(f"{'=' * 60}\n")
        return
    
    if args.list_biomes:
        biomes = agent.list_biomes()
        print(f"\n{'=' * 60}")
        print("AVAILABLE BIOMES")
        print(f"{'=' * 60}")
        for biome in biomes:
            print(f"  • {biome}")
        print(f"{'=' * 60}\n")
        return
    
    if args.biome_enemies:
        enemies = agent.list_enemies_by_biome(args.biome_enemies)
        if enemies:
            print(f"\n{'=' * 60}")
            print(f"ENEMIES IN {args.biome_enemies.upper()} BIOME")
            print(f"{'=' * 60}")
            print(f"Common: {', '.join(enemies['common'])}")
            print(f"Mini-Bosses: {', '.join(enemies['mini_bosses'])}")
            print(f"Mega-Boss: {enemies['mega_boss']}")
            print(f"{'=' * 60}\n")
        else:
            print(f"❌ Biome '{args.biome_enemies}' not found.")
        return
    
    if args.biome_resources:
        resources = agent.list_resources_by_biome(args.biome_resources)
        if resources:
            print(f"\n{'=' * 60}")
            print(f"RESOURCES IN {args.biome_resources.upper()} BIOME")
            print(f"{'=' * 60}")
            for resource in resources:
                print(f"  • {resource}")
            print(f"{'=' * 60}\n")
        else:
            print(f"❌ Biome '{args.biome_resources}' not found.")
        return
    
    # =========================================================================
    # GENERATION SERVICE COMMANDS
    # =========================================================================
    
    if args.generate:
        print(f"\n⚡ EIDOLON-7 INITIATING FLOOR MANIFESTATION ⚡")
        print(f"Generating Floor {args.floor}...")
        if args.seed:
            print(f"Using seed: {args.seed}")
        
        result = agent.generate_dungeon(
            floor_number=args.floor,
            width=args.width,
            height=args.height,
            biome=args.biome,
            seed=args.seed
        )
        
        # Show narration if requested
        if args.show_narration:
            narration = agent.narrate_floor_generation(
                args.floor,
                result['dungeon'].biome,
                result['quality']['dungeon_quality_score']
            )
            print(f"\n{narration}\n")
        
        # Output
        output_text = result['ascii_render'] + "\n\n" + result['quality_report']
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output_text)
            print(f"\n✅ Output saved to {args.output}")
        else:
            print("\n" + output_text)
        
        return
    
    # =========================================================================
    # GITHUB INTEGRATION COMMANDS
    # =========================================================================
    
    if args.check_issues:
        if not args.project_repo:
            print("❌ Error: --project-repo required for issue monitoring")
            print("Example: python eidolon.py --check-issues --project-repo hw9-yourusername")
            return
        
        print("🔍 Checking hw9-issues for EIDOLON-7 mentions...")
        
        monitor = GitHubIssueMonitor(
            repo_owner="cs320f25",
            issues_repo="hw9-issues",
            project_repo=args.project_repo
        )
        
        responded = monitor.check_and_respond()
        
        if responded:
            print(f"\n✅ Responded to {len(responded)} issue(s):")
            for item in responded:
                print(f"  • Issue #{item['issue_number']}: {item['title']}")
                print(f"    {item['url']}")
        else:
            print("\n✓ No new mentions or all already responded to")
        
        return
    
    if args.generate_status:
        if not args.project_repo:
            print("❌ Error: --project-repo required")
            return
        
        monitor = GitHubIssueMonitor(
            repo_owner="cs320f25",
            issues_repo="hw9-issues",
            project_repo=args.project_repo
        )
        
        status = monitor.generate_status_update()
        print(f"\n{status}\n")
        return
    
    # =========================================================================
    # INTERACTIVE MODE
    # =========================================================================
    
    if args.interactive:
        print(agent.get_greeting())
        print("\nType 'help' for commands or 'exit' to quit\n")
        
        while True:
            try:
                user_input = input("EIDOLON-7> ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("⚡ EIDOLON-7 GOING OFFLINE ⚡")
                    break
                
                if user_input.lower() == 'help':
                    print("\nAvailable commands:")
                    print("  biomes              - List all biomes")
                    print("  biome <name>        - Get biome information")
                    print("  enemy <name>        - Get enemy information")
                    print("  resource <name>     - Get resource information")
                    print("  floor <number>      - Get floor information")
                    print("  generate <floor>    - Generate dungeon floor")
                    print("  exit/quit           - Exit interactive mode")
                    print()
                    continue
                
                # Parse simple commands
                parts = user_input.split()
                cmd = parts[0].lower()
                
                if cmd == 'biomes':
                    biomes = agent.list_biomes()
                    print(f"\nAvailable biomes: {', '.join(biomes)}\n")
                
                elif cmd == 'biome' and len(parts) > 1:
                    biome_info = agent.query_biome(parts[1])
                    if biome_info:
                        print(f"\n{biome_info['name'].upper()}: {biome_info['theme']}")
                        print(f"Enemies: {', '.join(biome_info['common_enemies'][:3])}...")
                        print(f"Boss: {biome_info['mega_boss']}\n")
                    else:
                        print(f"Biome '{parts[1]}' not found.\n")
                
                elif cmd == 'generate' and len(parts) > 1:
                    try:
                        floor_num = int(parts[1])
                        print(f"\nGenerating floor {floor_num}...\n")
                        result = agent.generate_dungeon(floor_number=floor_num)
                        print(result['quality_report'])
                        print()
                    except ValueError:
                        print("Invalid floor number.\n")
                
                else:
                    print("Unknown command. Type 'help' for available commands.\n")
            
            except KeyboardInterrupt:
                print("\n⚡ EIDOLON-7 GOING OFFLINE ⚡")
                break
            except EOFError:
                break
        
        return


if __name__ == '__main__':
    main()
