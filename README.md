# Procedural Dungeon Generator
## AI-Validated Dungeon Floor Generator with Biome-Based Constraints

**Course:** AI Engineering (CS 320)
**Project Type:** Final Assignment
**Language:** Python 3.x
**Output:** Command-line ASCII visualization

---

## 🚀 CURRENT STATUS (Updated: Nov 19, 2025)

### ✅ PHASE 1 COMPLETE!

**What's Working:**
- ✅ Procedural dungeon generation (rooms + corridors)
- ✅ Biome-specific enemy and resource placement
- ✅ **AI pathfinding validation (BFS algorithm)** - THE KEY AI COMPONENT
- ✅ ASCII visualization with overlays
- ✅ **REAL-TIME ANIMATION** - Watch the AI generate dungeons!

**Professor Feedback:**
- ✅ Changed scope from 100 floors → 3 high-quality floors
- ✅ ASCII terminal output approved (no graphics needed)
- ✅ Animation feature added for impressive demos

### 🎯 Quick Start

```bash
# Basic generation
python main.py --floor 1

# With validation (shows AI pathfinding)
python main.py --floor 1 --validate

# WITH ANIMATION (watch it generate in real-time!)
python main.py --floor 1 --animate --speed 0.5

# All options
python main.py --floor 2 --width 60 --height 40 --animate --speed 0.3 --validate
```

### 📋 Next Steps

**Phase 2: Polish & Finalize (TODO)**
1. Create 3 polished example floors for professor
2. Write demonstration script
3. Add more detailed validation output
4. Performance optimization (if needed)
5. Final testing and documentation

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Goals](#project-goals)
3. [Technical Scope](#technical-scope)
4. [Biome System](#biome-system)
5. [Enemy Classification](#enemy-classification)
6. [Resource System](#resource-system)
7. [Floor Progression (1-100)](#floor-progression-1-100)
8. [Generation Algorithm](#generation-algorithm)
9. [AI Validation System](#ai-validation-system)
10. [Implementation Plan](#implementation-plan)
11. [Project Deliverables](#project-deliverables)

---

## Project Overview

A procedural dungeon generator that creates randomized floor layouts with biome-specific enemies, resources, and constraints. The system uses AI pathfinding algorithms to validate that all generated dungeons are navigable and all resources are accessible.

**Inspired by:** "Dungeon Ascend" game concept - a roguelike where players ascend through 100 floors of varied biomes.

---

## Project Goals

### Primary Objectives
1. Generate randomized dungeon floors with rooms and corridors
2. Implement 9 distinct biomes with unique characteristics
3. Apply rule-based enemy and resource spawning
4. Validate dungeon connectivity using pathfinding algorithms
5. Support 100-floor progression system with scaling difficulty

### AI Engineering Components
- **Pathfinding:** A* or BFS for connectivity validation
- **Constraint Satisfaction:** Rule-based enemy spawning
- **Procedural Generation:** Algorithmic dungeon layout creation
- **Heuristic Optimization:** Valid dungeon generation with minimal retries

---

## Technical Scope

### What's Included
- Grid-based dungeon generation (2D)
- ASCII visualization in terminal
- 9 biomes with specific spawn rules
- 50+ enemy types with biome restrictions
- Resource placement with accessibility validation
- Floor progression system (1-100)
- Boss spawn rules (Mini-Boss, Mega-Boss)
- Configurable parameters (size, density, difficulty)

### What's NOT Included
- Game mechanics (combat, player movement, abilities)
- Graphical interface or sprites
- Save/load functionality
- Real-time gameplay
- Character progression systems

---

## Biome System

### 1. Jungle Biome
**Theme:** Lush, overgrown vegetation with hidden dangers

**Characteristics:**
- Dense foliage and vines
- Hidden paths and ambush points
- High resource availability

**Resources:**
- Hardwood (Common) - Used for basic crafting
- Ironwood (Uncommon) - Durable material
- Medicinal Herbs (Common) - Healing items
- Rare Orchids (Rare) - Valuable alchemy ingredient
- Jungle Fruits (Common) - Food source
- Poison Glands (Uncommon) - Dropped by enemies

**Common Enemies:**
- Jungle Creepers
- Fire Sprites
- Arcane Wisps

**Mini-Bosses:**
- Hydra Spawn
- Toxic Maw

**Mega-Boss:**
- Jungle Titan

---

### 2. Snow Biome
**Theme:** Frozen wasteland with limited visibility

**Characteristics:**
- Slippery terrain
- Reduced movement speed
- Cold damage hazards

**Resources:**
- Ice Crystals (Common) - Crafting material
- Frozen Herbs (Uncommon) - Preservation
- Rare Minerals (Rare) - Embedded in ice
- Frost Shards (Uncommon) - Magical component
- Yeti Fur (Uncommon) - Dropped by enemies
- Glacial Water (Common) - Pure water source

**Common Enemies:**
- Frost Imps
- Ice Revenants (as common variant)
- Crystal Scavengers

**Mini-Bosses:**
- Frost Banshee
- Ice Revenant (full)

**Mega-Boss:**
- Frost Wyrm

---

### 3. Swamp Biome
**Theme:** Murky, fog-covered wetlands

**Characteristics:**
- Hidden water paths
- Poison hazards
- Visibility reduction

**Resources:**
- Swamp Moss (Common) - Alchemy base
- Murky Water (Common) - Basic resource
- Poison Sacs (Uncommon) - Enemy drops
- Bog Iron (Uncommon) - Low-grade metal
- Fungal Spores (Rare) - Potent alchemy
- Reed Bundles (Common) - Crafting material

**Common Enemies:**
- Swamp Sludges
- Plague Rats
- Banshee Wailers

**Mini-Bosses:**
- Mud Behemoth
- Toxic Maw

**Mega-Boss:**
- Swamp Leviathan

---

### 4. Vampire Theme Biome
**Theme:** Gothic architecture, dark and eerie

**Characteristics:**
- Blood-themed aesthetics
- Dark corridors
- Life-draining hazards

**Resources:**
- Blood Vials (Uncommon) - Ritual component
- Ancient Tomes (Rare) - Knowledge/lore
- Silver Ore (Uncommon) - Anti-undead material
- Gothic Relics (Rare) - Valuable artifacts
- Bat Wings (Common) - Enemy drops
- Darkwood (Uncommon) - Building material

**Common Enemies:**
- Blood Bats
- Shadow Stalkers
- Cursed Armor

**Mini-Bosses:**
- Spectral Knight
- Crimson Witch

**Mega-Boss:**
- Vampire Lord

---

### 5. Werewolf Theme Biome
**Theme:** Forested areas under a full moon

**Characteristics:**
- Dense forest terrain
- Pack enemy behavior
- Night-time aesthetics

**Resources:**
- Wolf Pelts (Common) - Crafting material
- Moonstone Shards (Rare) - Magical gem
- Forest Herbs (Common) - Medicinal
- Silver Dust (Uncommon) - Purification
- Claw Fragments (Uncommon) - Enemy drops
- Ancient Bark (Uncommon) - Strong material

**Common Enemies:**
- Moonlight Wolves
- Shadow Stalkers
- Rogue Mercenaries

**Mini-Bosses:**
- Shadow Assassin
- Boulder Beast

**Mega-Boss:**
- Lycan Alpha

---

### 6. Rocky Biome
**Theme:** Mountainous terrain with caves

**Characteristics:**
- Rockfall hazards
- Cave systems
- High mineral content

**Resources:**
- Iron Ore (Common) - Basic metal
- Copper Ore (Common) - Crafting metal
- Gemstones (Rare) - Valuable minerals
- Stone Blocks (Common) - Building material
- Cave Crystals (Uncommon) - Light source
- Obsidian Shards (Rare) - Sharp crafting material

**Common Enemies:**
- Stone Sentinels
- Crystal Scavengers
- Goblin Tinkers

**Mini-Bosses:**
- Stone Golem
- Boulder Beast

**Mega-Boss:**
- Giant Stone Guardian

---

### 7. Satanic/Infernal Biome
**Theme:** Hellish landscapes with fire hazards

**Characteristics:**
- Fire damage zones
- Demonic enemies
- Ritual-based aesthetics

**Resources:**
- Brimstone (Common) - Sulfur material
- Demon Ichor (Uncommon) - Dark alchemy
- Hellfire Ash (Uncommon) - Volatile material
- Soul Fragments (Rare) - Mystical component
- Infernal Iron (Uncommon) - Heat-forged metal
- Cursed Relics (Rare) - Powerful but dangerous

**Common Enemies:**
- Infernal Minions
- Fire Sprites
- Shadow Stalkers

**Mini-Bosses:**
- Inferno Drake
- Magma Goliath

**Mega-Boss:**
- Demon Warlord

---

### 8. Fairy/Fae Biome
**Theme:** Enchanted forest with illusions

**Characteristics:**
- Deceptive paths
- Illusion-based challenges
- Magical creatures

**Resources:**
- Fairy Dust (Rare) - Potent magic catalyst
- Enchanted Flowers (Uncommon) - Alchemy
- Moonwell Water (Rare) - Pure magical water
- Sprite Wings (Uncommon) - Enemy drops
- Dream Silk (Rare) - Ethereal fabric
- Glowshrooms (Common) - Bioluminescent fungi

**Common Enemies:**
- Fae Sprites
- Arcane Wisps
- Mystic Oracles

**Mini-Bosses:**
- Rogue Elementalist
- Arcane Sentinel

**Mega-Boss:**
- Fae Queen

---

### 9. Astral Void Biome
**Theme:** Cosmic/space aesthetic with gravitational anomalies

**Characteristics:**
- Starfield visuals
- Gravity effects
- Cosmic hazards

**Resources:**
- Stardust (Uncommon) - Cosmic material
- Void Crystals (Rare) - Dimensional energy
- Meteorite Fragments (Uncommon) - Space metal
- Astral Essence (Rare) - Pure magical energy
- Nebula Gas (Uncommon) - Exotic resource
- Cosmic Ore (Rare) - Otherworldly metal

**Common Enemies:**
- Astral Specters
- Arcane Wisps
- Thunderbirds

**Mini-Bosses:**
- Thunder Wraith
- Crystal Colossus

**Mega-Boss:**
- Celestial Sentinel

---

## Enemy Classification

### Enemy Tiers
1. **Common Enemies** - Spawn frequently, lower difficulty
2. **Mini-Bosses** - Spawn occasionally, moderate difficulty
3. **Mega-Bosses** - Spawn every 11th floor, highest difficulty

### Total Enemy Count
- **Common Enemies:** 24 types
- **Mini-Bosses:** 20 types
- **Mega-Bosses:** 9 types (one per biome)

### Enemy Spawn Rules
1. Enemies can only spawn in their designated biomes
2. Some enemies can spawn in multiple biomes (e.g., Shadow Stalkers, Arcane Wisps)
3. Mini-boss spawn chance increases with floor depth
4. Mega-bosses ONLY appear on floors 11, 22, 33, 44, 55, 66, 77, 88, 99

---

## Resource System

### Resource Rarity Tiers
- **Common** (60% drop rate) - Basic crafting materials
- **Uncommon** (30% drop rate) - Intermediate materials
- **Rare** (10% drop rate) - High-value materials

### Resource Placement Rules
1. Resources must be in accessible rooms (not blocked by walls)
2. Each biome spawns 3-5 resource types
3. Rarity affects spawn quantity (more common = more spawns)
4. Resources can spawn in:
   - Room corners
   - Along walls
   - In the center of large rooms
   - Not in corridors

---

## Floor Progression (1-100)

### Floor Structure

**Floors 1-10: Tutorial Zone**
- Biomes: Jungle, Snow, Swamp (rotating)
- Enemy density: Low (5-8 enemies per floor)
- Mini-boss chance: 10%
- Room count: 4-6 rooms
- Difficulty multiplier: 1.0x

**Floors 11-20: Early Game**
- Floor 11: **MEGA-BOSS** (Jungle Titan, Frost Wyrm, or Swamp Leviathan)
- Biomes: All except Astral Void
- Enemy density: Medium (8-12 enemies per floor)
- Mini-boss chance: 20%
- Room count: 5-8 rooms
- Difficulty multiplier: 1.2x

**Floors 21-30: Mid-Early Game**
- Floor 22: **MEGA-BOSS**
- Biomes: All except Astral Void
- Enemy density: Medium (10-15 enemies per floor)
- Mini-boss chance: 25%
- Room count: 6-9 rooms
- Difficulty multiplier: 1.5x

**Floors 31-40: Mid Game**
- Floor 33: **MEGA-BOSS**
- Floor 44: **MEGA-BOSS**
- Biomes: All biomes available
- Enemy density: High (12-18 enemies per floor)
- Mini-boss chance: 30%
- Room count: 7-10 rooms
- Difficulty multiplier: 1.8x

**Floors 41-70: Late-Mid Game**
- Mega-bosses on floors 44, 55, 66
- Biomes: All biomes, higher chance of themed biomes (Vampire, Werewolf, Satanic)
- Enemy density: High (15-22 enemies per floor)
- Mini-boss chance: 40%
- Room count: 8-12 rooms
- Difficulty multiplier: 2.0x - 2.5x

**Floors 71-99: Endgame**
- Mega-bosses on floors 77, 88, 99
- Biomes: All biomes, emphasis on Astral Void
- Enemy density: Very High (18-30 enemies per floor)
- Mini-boss chance: 50%
- Room count: 10-15 rooms
- Difficulty multiplier: 3.0x - 4.0x

**Floor 100: Final Floor**
- Special design (not implemented in initial version)
- Could be final confrontation area

### Boss Spawn Rules

**Mega-Boss Rules:**
- Floors: 11, 22, 33, 44, 55, 66, 77, 88, 99
- Guaranteed spawn in special boss room
- Boss matches current floor biome
- No common enemies in boss room
- Boss room is always the largest room on the floor

**Mini-Boss Rules:**
- Random spawn based on floor progression chance
- Spawns in regular rooms (not corridors)
- Can have 1-3 common enemies as support
- Mini-boss must match floor biome

### Difficulty Scaling
- **Enemy Health:** Base HP × Difficulty Multiplier × Floor Multiplier
- **Enemy Damage:** Base Damage × Difficulty Multiplier
- **Floor Multiplier:** 1 + (Floor / 100)
  - Floor 1: 1.01x
  - Floor 50: 1.5x
  - Floor 100: 2.0x

---

## Generation Algorithm

### High-Level Overview
1. **Determine Floor Parameters**
   - Floor number determines biome pool, enemy density, room count
   - Check if current floor is mega-boss floor

2. **Select Biome**
   - Weighted random selection based on floor progression
   - Early floors favor simpler biomes (Jungle, Snow, Swamp)
   - Later floors introduce complex biomes (Astral Void)

3. **Generate Room Layout**
   - Create N rooms with random sizes
   - Place rooms on grid without overlap
   - Generate corridors connecting all rooms

4. **Place Enemies**
   - Apply biome-specific spawn rules
   - Place mega-boss if applicable
   - Roll for mini-boss spawn
   - Fill remaining slots with common enemies

5. **Place Resources**
   - Determine resource types from biome
   - Place resources in accessible locations
   - Apply rarity-based spawn rates

6. **Validate Dungeon**
   - Run pathfinding to ensure all rooms are connected
   - Verify all resources are accessible
   - Check that spawn rules are satisfied

7. **Output Result**
   - Render ASCII visualization
   - Display floor stats (biome, enemies, resources)

### Room Generation
- **Small Room:** 3x3 to 5x5 tiles
- **Medium Room:** 6x6 to 10x10 tiles
- **Large Room:** 11x11 to 15x15 tiles
- **Boss Room:** Always large (12x12 minimum)

### Corridor Generation
- Width: 1-2 tiles
- Path: Straight lines with 90-degree turns (L-shapes)
- Algorithm: Connect room centers using Manhattan distance

---

## AI Validation System

### Pathfinding Requirements
The generator must use AI pathfinding to validate:

1. **Connectivity Check**
   - All rooms must be reachable from starting room
   - Use BFS or A* from spawn point
   - If any room is unreachable, regenerate corridors

2. **Resource Accessibility**
   - All resource locations must be pathable
   - No resources spawned in isolated areas

3. **Enemy Placement Validation**
   - Enemies spawn in reachable areas
   - Boss rooms have valid path from entrance

### Pathfinding Algorithms

**Option 1: Breadth-First Search (BFS)**
- Simpler to implement
- Guarantees shortest path
- Good for validation (just need to check reachability)

**Option 2: A\* Search**
- More sophisticated
- Uses heuristics (Manhattan distance)
- Better for finding optimal paths
- Demonstrates stronger AI knowledge

**Recommended:** Start with BFS for validation, optionally upgrade to A* for bonus points.

### Validation Metrics
The system should output:
- Total rooms: X
- Connected rooms: X/X
- Resources placed: X
- Accessible resources: X/X
- Enemies placed: X
- Valid placements: X/X
- Generation attempts: X (before success)

---

## Implementation Plan

### Phase 1: Core Generation (Week 1)
- [ ] Set up project structure
- [ ] Implement grid-based dungeon class
- [ ] Create room generation algorithm
- [ ] Implement corridor generation
- [ ] Basic ASCII rendering

### Phase 2: Biome & Enemy System (Week 1-2)
- [ ] Define biome data structures
- [ ] Implement enemy classification system
- [ ] Create spawn rule engine
- [ ] Add resource placement logic

### Phase 3: AI Validation (Week 2)
- [ ] Implement BFS pathfinding
- [ ] Add connectivity validation
- [ ] Resource accessibility checks
- [ ] Regeneration on validation failure

### Phase 4: Floor Progression (Week 2-3)
- [ ] Implement 100-floor system
- [ ] Add difficulty scaling
- [ ] Boss spawn rules
- [ ] Floor-specific parameters

### Phase 5: Polish & Testing (Week 3)
- [ ] Configuration system (CLI args)
- [ ] Comprehensive testing
- [ ] Documentation
- [ ] Example outputs

---

## Project Deliverables

### Required Outputs
1. **Source Code**
   - Well-commented Python code
   - Modular architecture
   - Clear separation of concerns

2. **README.md** (this document)
   - Complete project documentation
   - Usage instructions
   - Design decisions

3. **Example Outputs**
   - 5-10 generated dungeon floor examples
   - Variety of biomes and floor numbers
   - Validation statistics

4. **Demo Script**
   - Generate floors 1, 11, 50, 99
   - Show different biomes
   - Demonstrate validation

### Bonus Features (Optional)
- [ ] Save generated dungeons to file
- [ ] JSON export of dungeon data
- [ ] Detailed statistics tracking
- [ ] Color-coded ASCII output
- [ ] Multiple generation algorithms
- [ ] Performance benchmarking

---

## Technical Requirements

### Dependencies
```
Python 3.8+
Standard library only (no external packages required)
```

### File Structure
```
320-final/
├── README.md (this file)
├── src/
│   ├── __init__.py
│   ├── dungeon.py         # Main dungeon class
│   ├── generator.py       # Generation algorithms
│   ├── biome.py          # Biome definitions
│   ├── enemy.py          # Enemy data and rules
│   ├── resource.py       # Resource system
│   ├── pathfinding.py    # AI validation
│   └── renderer.py       # ASCII output
├── data/
│   ├── biomes.json       # Biome configurations
│   ├── enemies.json      # Enemy data
│   └── resources.json    # Resource definitions
├── examples/
│   └── sample_floors/    # Generated examples
├── tests/
│   └── test_*.py        # Unit tests
└── main.py              # Entry point
```

### Running the Generator
```bash
# Generate a random floor
python main.py

# Generate specific floor
python main.py --floor 1

# With AI validation (shows pathfinding)
python main.py --floor 1 --validate

# WITH ANIMATION (real-time generation visualization!)
python main.py --floor 1 --animate

# Animation with custom speed (seconds between steps)
python main.py --floor 1 --animate --speed 0.3  # Fast
python main.py --floor 1 --animate --speed 1.0  # Slow for demos

# All features combined
python main.py --floor 2 --width 60 --height 40 --animate --validate --speed 0.5

# Generate with specific biome
python main.py --biome jungle

# Generate and save to file
python main.py --floor 1 --output floor_1.txt
```

---

## Success Criteria

### Minimum Viable Product (MVP)
- [x] Generates valid dungeon layouts
- [x] Implements at least 5 biomes
- [x] Has biome-specific enemy spawning
- [x] Uses pathfinding for validation
- [x] Supports basic floor progression

### Full Implementation
- [x] All 9 biomes implemented
- [x] All 50+ enemies with spawn rules
- [x] Full 100-floor progression
- [x] Resource system with accessibility
- [x] Boss spawn rules (mini + mega)
- [x] Difficulty scaling
- [x] Comprehensive validation

### Excellent (A-Grade)
- All full implementation features
- Clean, well-documented code
- Comprehensive testing
- Performance optimization
- Bonus features implemented
- Strong demonstration of AI concepts

---

## Notes and Design Decisions

### Why ASCII?
- Fast to implement
- Easy to debug
- No dependencies
- Professor can easily run and grade
- Focus on algorithms, not graphics

### Why Command-Line?
- Simplicity for a few-week project
- Emphasizes the AI/algorithm component
- Easy to demonstrate and test
- Can generate many examples quickly

### Scope Boundaries
**In Scope:**
- Dungeon generation and validation
- Spawn rules and constraints
- AI pathfinding

**Out of Scope:**
- Player movement or combat
- Inventory systems
- Crafting mechanics
- Save/load game state
- Multiplayer or networking

---

## Credits

**Student:** [Your Name]
**Course:** AI Engineering (CS 320)
**Semester:** [Current Semester]

**Inspired by:** "Dungeon Ascend" game concept from personal game design document

---

**Last Updated:** November 19, 2025
