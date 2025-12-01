# SYSTEM ARCHITECTURE DIAGRAM

## Overall System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DUNGEON ASCEND GENERATOR                          │
│                     with EIDOLON-7 Agent                            │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACES                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │   main.py    │  │  eidolon.py  │  │   demo.py    │            │
│  │   (Original  │  │  (EIDOLON-7  │  │ (Demo Script)│            │
│  │   Generator) │  │   CLI)       │  │              │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│         │                 │                  │                      │
└─────────┼─────────────────┼──────────────────┼──────────────────────┘
          │                 │                  │
          └─────────────────┴──────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────────────┐
│                      CORE SERVICES LAYER                             │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │              EIDOLON-7 ADK AGENT                            │   │
│  │              (src/eidolon_agent.py)                         │   │
│  ├────────────────────────────────────────────────────────────┤   │
│  │                                                             │   │
│  │  Service 1: KNOWLEDGE SERVICE (ADK #2)                     │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │ - query_biome()      - list_biomes()                │  │   │
│  │  │ - query_enemy()      - list_enemies_by_biome()      │  │   │
│  │  │ - query_resource()   - list_resources_by_biome()    │  │   │
│  │  │ - get_floor_info()                                   │  │   │
│  │  └─────────────────────────────────────────────────────┘  │   │
│  │                                                             │   │
│  │  Service 2: GENERATION & EVALUATION SERVICE (ADK #2)      │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │ - generate_dungeon()                                 │  │   │
│  │  │ - evaluate_dungeon()                                 │  │   │
│  │  │ - narrate_floor_generation()                         │  │   │
│  │  └─────────────────────────────────────────────────────┘  │   │
│  │                                                             │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │          GITHUB INTEGRATION SERVICE (ADK #1)                │   │
│  │          (src/github_integration.py)                        │   │
│  ├────────────────────────────────────────────────────────────┤   │
│  │ - fetch_open_issues()     - post_comment()                 │   │
│  │ - is_mentioned()          - analyze_project_status()       │   │
│  │ - has_responded()         - generate_status_update()       │   │
│  │ - check_and_respond()                                      │   │
│  └────────────────────────────────────────────────────────────┘   │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────────────┐
│                   ENGINE LAYER (Core Logic)                          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐ │
│  │    Generator     │  │  Pathfinding     │  │  Quality Metrics │ │
│  │   (generator.py) │  │ (pathfinding.py) │  │ (quality_        │ │
│  │                  │  │                  │  │  metrics.py)     │ │
│  ├──────────────────┤  ├──────────────────┤  ├──────────────────┤ │
│  │ - generate()     │  │ - validate_      │  │ - evaluate()     │ │
│  │ - _select_biome()│  │   connectivity() │  │ - _calculate_dqs│ │
│  │ - _generate_     │  │ - bfs_           │  │ - generate_     │ │
│  │   rooms()        │  │   reachability() │  │   report()      │ │
│  │ - _place_enemies│  │ - find_path()    │  │                 │ │
│  │ - _place_        │  │                  │  │                 │ │
│  │   resources()    │  │                  │  │                 │ │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘ │
│         │                       │                       │           │
└─────────┼───────────────────────┼───────────────────────┼───────────┘
          │                       │                       │
┌─────────▼───────────────────────▼───────────────────────▼───────────┐
│                    DATA STRUCTURES LAYER                             │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │   Dungeon    │  │     Room     │  │   TileType   │            │
│  │ (dungeon.py) │  │ (dungeon.py) │  │ (dungeon.py) │            │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤            │
│  │ - width      │  │ - x, y       │  │ - WALL       │            │
│  │ - height     │  │ - width      │  │ - FLOOR      │            │
│  │ - grid       │  │ - height     │  │ - CORRIDOR   │            │
│  │ - rooms      │  │ - center     │  │ - EMPTY      │            │
│  │ - biome      │  │ - enemies    │  │              │            │
│  │ - enemies    │  │ - resources  │  │              │            │
│  │ - resources  │  │              │  │              │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │    Biome     │  │    Enemy     │  │   Resource   │            │
│  │  (biome.py)  │  │  (enemy.py)  │  │(resource.py) │            │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤            │
│  │ - name       │  │ - name       │  │ - name       │            │
│  │ - theme      │  │ - tier       │  │ - rarity     │            │
│  │ - resources  │  │ - biomes     │  │ - biomes     │            │
│  │ - enemies    │  │ - base_hp    │  │ - description│            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────────────┐
│                    DATA STORAGE LAYER                                │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │ biomes.json  │  │ enemies.json │  │resources.json│            │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤            │
│  │ 9 biomes:    │  │ 50+ enemies: │  │ Resources:   │            │
│  │ - jungle     │  │ - common     │  │ - common     │            │
│  │ - snow       │  │ - mini-boss  │  │ - uncommon   │            │
│  │ - swamp      │  │ - mega-boss  │  │ - rare       │            │
│  │ - vampire    │  │              │  │              │            │
│  │ - werewolf   │  │              │  │              │            │
│  │ - rocky      │  │              │  │              │            │
│  │ - satanic    │  │              │  │              │            │
│  │ - fairy      │  │              │  │              │            │
│  │ - astral_void│  │              │  │              │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                    EXTERNAL INTEGRATION                              │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │              GitHub API Integration                         │    │
│  ├────────────────────────────────────────────────────────────┤    │
│  │                                                             │    │
│  │  cs320f25/hw9-issues  ◄─────  EIDOLON-7  ─────► Your Repo │    │
│  │  (Issue Monitoring)            (Agent)     (Status Check)  │    │
│  │                                                             │    │
│  │  1. Monitor issues                                         │    │
│  │  2. Detect "EIDOLON-7" mentions                           │    │
│  │  3. Analyze your repository                                │    │
│  │  4. Generate status report                                 │    │
│  │  5. Post comment to issue                                  │    │
│  │                                                             │    │
│  └────────────────────────────────────────────────────────────┘    │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## Data Flow for Dungeon Generation with DQS

```
User Request: "Generate Floor 12"
        │
        ▼
┌───────────────────┐
│  EIDOLON-7 Agent  │
│  (eidolon.py)     │
└───────┬───────────┘
        │
        │ 1. Parse Request
        ▼
┌───────────────────┐
│  Generator        │
│  - Select biome   │
│  - Create rooms   │
│  - Place enemies  │
│  - Place resources│
└───────┬───────────┘
        │
        │ 2. Generate Dungeon
        ▼
┌───────────────────┐
│  Pathfinding      │
│  - BFS from start │
│  - Check connected│
│  - Check accessible│
└───────┬───────────┘
        │
        │ 3. Validate Connectivity
        ▼
┌───────────────────┐
│  Quality Metrics  │
│  - Calculate DQS  │
│  - Generate grade │
│  - Create report  │
└───────┬───────────┘
        │
        │ 4. Evaluate Quality
        ▼
┌───────────────────┐
│  Renderer         │
│  - Create ASCII   │
│  - Add overlays   │
└───────┬───────────┘
        │
        │ 5. Render Output
        ▼
┌───────────────────┐
│  Return to User   │
│  - ASCII dungeon  │
│  - DQS report     │
│  - Narration      │
└───────────────────┘
```

## DQS Scoring Algorithm

```
Input: Dungeon Object
        │
        ▼
┌─────────────────────────────────────────┐
│    Calculate Individual Metrics         │
├─────────────────────────────────────────┤
│                                          │
│  1. Pathability                         │
│     reachable_tiles / total_tiles       │
│     normalized to 0-1                   │
│     Weight: 20%                         │
│                                          │
│  2. Resource Accessibility              │
│     accessible_resources / total        │
│     Weight: 30%                         │
│                                          │
│  3. Room Connectivity                   │
│     connected_rooms / total_rooms       │
│     Weight: 35%                         │
│                                          │
│  4. Space Efficiency                    │
│     room_density optimization           │
│     Weight: 15%                         │
│                                          │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      Weighted Average Calculation        │
│                                          │
│  DQS = (0.35 × connectivity) +          │
│        (0.30 × accessibility) +          │
│        (0.20 × pathability) +            │
│        (0.15 × efficiency)               │
│                                          │
│  Result: 0.0 to 1.0                     │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│          Grade Assignment                │
│                                          │
│  0.95+ → S  (Perfect)                   │
│  0.90+ → A+ (Exceptional)               │
│  0.85+ → A  (Excellent)                 │
│  0.80+ → A- (Very Good)                 │
│  0.75+ → B+ (Good)                      │
│  0.70+ → B  (Above Average)             │
│  0.65+ → B- (Average)                   │
│  0.60+ → C+ (Below Average)             │
│  0.50+ → C  (Poor)                      │
│  <0.50 → F  (Unacceptable)              │
└──────────────┬──────────────────────────┘
               │
               ▼
        Final Report with
        Score, Grade, Metrics
```

## GitHub Issue Monitoring Flow

```
Cron Job / Manual Trigger
        │
        ▼
┌───────────────────────┐
│  Fetch Open Issues    │
│  from hw9-issues      │
└───────┬───────────────┘
        │
        ▼
For each issue:
        │
        ├─► Is "EIDOLON-7" mentioned? ──No──► Skip
        │                               
        Yes
        │
        ├─► Already responded? ──Yes──► Skip
        │                               
        No
        │
        ▼
┌───────────────────────┐
│  Analyze Project Repo │
│  - Fetch commits      │
│  - Check issues       │
│  - Get repo info      │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│  Generate Status      │
│  - Phase breakdown    │
│  - Recent commits     │
│  - Open issues        │
│  - Next steps         │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│  Post Comment         │
│  to hw9-issues        │
└───────────────────────┘
```
