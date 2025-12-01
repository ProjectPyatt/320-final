#!/usr/bin/env python3
"""
EIDOLON-7 Demonstration Script
Showcases all features for Checkpoint 2
"""

import sys
import time
from src.eidolon_agent import Eidolon7Agent


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def wait_for_input():
    """Wait for user to press Enter"""
    input("\nPress Enter to continue...")


def main():
    print("\n" + "⚡" * 35)
    print("  EIDOLON-7 CHECKPOINT 2 DEMONSTRATION")
    print("  Dungeon Ascend Generator with ADK Integration")
    print("⚡" * 35 + "\n")
    
    # Initialize agent
    agent = Eidolon7Agent(data_dir='data')
    
    # Greeting
    print(agent.get_greeting())
    wait_for_input()
    
    # =========================================================================
    # PART 1: KNOWLEDGE SERVICE DEMO
    # =========================================================================
    
    print_section("PART 1: KNOWLEDGE SERVICE (ADK Requirement #2)")
    
    print("EIDOLON-7 can answer questions about biomes, enemies, and resources.\n")
    
    # Biome query
    print("Query: Tell me about the Jungle biome")
    biome_info = agent.query_biome('jungle')
    if biome_info:
        print(f"\n🌴 {biome_info['name'].upper()} BIOME")
        print(f"Theme: {biome_info['theme']}")
        print(f"Common Enemies: {', '.join(biome_info['common_enemies'])}")
        print(f"Mega-Boss: {biome_info['mega_boss']}")
    
    wait_for_input()
    
    # Enemy query
    print("\nQuery: Tell me about the Frost Wyrm")
    enemy_info = agent.query_enemy('frost_wyrm')
    if enemy_info:
        print(f"\n❄️ {enemy_info['name'].upper()}")
        print(f"Tier: {enemy_info['tier']}")
        print(f"Base HP: {enemy_info['base_hp']}")
        print(f"Base Damage: {enemy_info['base_damage']}")
        print(f"Biomes: {', '.join(enemy_info['biomes'])}")
    
    wait_for_input()
    
    # Floor info
    print("\nQuery: What happens on Floor 33?")
    floor_info = agent.get_floor_info(33)
    print(f"\n🏰 FLOOR {floor_info['floor']}")
    print(f"Tier: {floor_info['tier']}")
    print(f"Difficulty: {floor_info['difficulty']}")
    print(f"Boss Floor: {'Yes - Mega-Boss will spawn!' if floor_info['is_boss_floor'] else 'No'}")
    print(f"Expected Enemies: {floor_info['expected_enemies']}")
    
    wait_for_input()
    
    # =========================================================================
    # PART 2: DUNGEON GENERATION SERVICE DEMO
    # =========================================================================
    
    print_section("PART 2: GENERATION SERVICE (ADK Requirement #2)")
    
    print("EIDOLON-7 can generate dungeons and evaluate their quality.\n")
    print("Generating Floor 1 (Tutorial Zone)...")
    
    result1 = agent.generate_dungeon(floor_number=1, width=50, height=30)
    
    print("\n" + result1['ascii_render'])
    
    wait_for_input()
    
    print("\nQuality Evaluation:")
    print(result1['quality_report'])
    
    wait_for_input()
    
    # Show narration
    print("\nWith Narration:")
    narration = agent.narrate_floor_generation(
        1,
        result1['dungeon'].biome,
        result1['quality']['dungeon_quality_score']
    )
    print(f"\n{narration}\n")
    
    wait_for_input()
    
    # Generate a boss floor
    print_section("Generating Floor 11 (First Mega-Boss Floor)...")
    
    result2 = agent.generate_dungeon(floor_number=11, width=50, height=30)
    
    print("\n" + result2['ascii_render'])
    print("\n" + result2['quality_report'])
    
    narration2 = agent.narrate_floor_generation(
        11,
        result2['dungeon'].biome,
        result2['quality']['dungeon_quality_score']
    )
    print(f"\n{narration2}\n")
    
    wait_for_input()
    
    # =========================================================================
    # PART 3: QUALITY METRICS COMPARISON
    # =========================================================================
    
    print_section("PART 3: DUNGEON QUALITY SCORE (DQS) SYSTEM")
    
    print("Let's compare quality scores across different floors:\n")
    
    floors_to_test = [1, 11, 33, 50]
    results = []
    
    for floor_num in floors_to_test:
        print(f"Generating Floor {floor_num}...", end=" ")
        result = agent.generate_dungeon(floor_number=floor_num, width=50, height=30)
        dqs = result['quality']['dungeon_quality_score']
        grade = result['quality']['grade'][0]
        results.append((floor_num, dqs, grade, result['dungeon'].biome))
        print(f"DQS: {dqs:.3f} [{grade}] ({result['dungeon'].biome.upper()})")
    
    print("\n📊 Quality Score Summary:")
    print("-" * 70)
    print(f"{'Floor':<10} {'DQS Score':<15} {'Grade':<10} {'Biome':<20}")
    print("-" * 70)
    for floor, dqs, grade, biome in results:
        print(f"{floor:<10} {dqs:<15.3f} {grade:<10} {biome.upper():<20}")
    print("-" * 70)
    
    wait_for_input()
    
    # =========================================================================
    # PART 4: GITHUB INTEGRATION INFO
    # =========================================================================
    
    print_section("PART 4: GITHUB ISSUE MONITORING (ADK Requirement #1)")
    
    print("EIDOLON-7 monitors the cs320f25/hw9-issues repository.")
    print("When an issue mentions 'EIDOLON-7', the agent responds.\n")
    
    print("How it works:")
    print("1. Monitor hw9-issues for open issues")
    print("2. Detect mentions of 'EIDOLON-7' (semantic matching)")
    print("3. Check if already responded (avoid spam)")
    print("4. Analyze YOUR project repository")
    print("5. Post comprehensive status update\n")
    
    print("Example trigger:")
    print("  'Hey EIDOLON-7, can you give me a status update?'\n")
    
    print("Response includes:")
    print("  - Implementation phase breakdown")
    print("  - Recent commits and activity")
    print("  - Open issues/blockers")
    print("  - Next steps")
    print("  - EIDOLON-7 signature\n")
    
    print("To test:")
    print("  export GITHUB_TOKEN='your_token'")
    print("  python eidolon.py --check-issues --project-repo hw9-yourname")
    
    wait_for_input()
    
    # =========================================================================
    # SUMMARY
    # =========================================================================
    
    print_section("DEMONSTRATION COMPLETE")
    
    print("✅ Checkpoint 2 Requirements Met:\n")
    print("1. Mostly Complete Implementation")
    print("   ✓ Core dungeon generation working")
    print("   ✓ BFS validation implemented")
    print("   ✓ DQS metrics system added")
    print("   ✓ EIDOLON-7 agent functional\n")
    
    print("2. Required ADK Service #1: GitHub Issue Monitoring")
    print("   ✓ Monitors cs320f25/hw9-issues")
    print("   ✓ Responds to 'EIDOLON-7' mentions")
    print("   ✓ Analyzes project repository")
    print("   ✓ Posts status updates\n")
    
    print("3. Required ADK Service #2: Natural Language Service")
    print("   ✓ Knowledge queries (biomes, enemies, resources)")
    print("   ✓ Generation service (create dungeons)")
    print("   ✓ Evaluation service (DQS analysis)\n")
    
    print("4. Documentation")
    print("   ✓ Updated README with setup instructions")
    print("   ✓ API documentation for ADK services")
    print("   ✓ Examples of interactions")
    print("   ✓ Bot name clearly defined (EIDOLON-7)\n")
    
    print("\n⚡ EIDOLON-7 DEMONSTRATION COMPLETE ⚡\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚡ EIDOLON-7 GOING OFFLINE ⚡\n")
        sys.exit(0)
