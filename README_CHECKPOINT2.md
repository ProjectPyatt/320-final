# Procedural Dungeon Generator with EIDOLON-7 Agent
## AI-Validated Dungeon Floor Generator with ADK Integration

**Course:** AI Engineering (CS 320)  
**Project Type:** Final Assignment - Checkpoint 2  
**Language:** Python 3.x  
**Output:** Command-line ASCII visualization + ADK Services

---

## 🚀 CURRENT STATUS (Updated: Dec 1, 2024)

### ✅ CHECKPOINT 1 COMPLETE

**Core Features Implemented:**
- ✅ Procedural dungeon generation (rooms + corridors)
- ✅ Biome-specific enemy and resource placement
- ✅ AI pathfinding validation (BFS algorithm)
- ✅ ASCII visualization with overlays
- ✅ Real-time animation feature
- ✅ 9 distinct biomes with unique themes
- ✅ 50+ enemies with spawn rules
- ✅ Full 100-floor progression system

### 🎯 CHECKPOINT 2 - NEW FEATURES

**1. Dungeon Quality Score (DQS) System** ✨
- Comprehensive quality metrics for generated dungeons
- Multi-factor evaluation:
  - **Pathability** - Percentage of reachable walkable space
  - **Resource Accessibility** - Percentage of reachable resources
  - **Room Connectivity** - Percentage of connected rooms
  - **Space Efficiency** - How well the space is utilized
- Overall DQS score (0-1) with letter grades (F to S)
- Detailed quality reports with recommendations

**2. EIDOLON-7 ADK Agent** 🤖
An intelligent agent providing three core services:

**A. Knowledge Service (ADK Requirement #2)**
Natural language queries about game mechanics:
```bash
# Query biomes, enemies, and resources
python eidolon.py --query-biome jungle
python eidolon.py --query-enemy frost_wyrm
python eidolon.py --query-resource stardust
python eidolon.py --floor-info 33
python eidolon.py --list-biomes
```

**B. Generation & Evaluation Service (ADK Requirement #2)**
Generate dungeons with quality analysis:
```bash
# Generate with quality evaluation
python eidolon.py --generate --floor 12
python eidolon.py --generate --floor 1 --biome rocky --show-narration
python eidolon.py --generate --floor 50 --seed 12345 --output floor50.txt
```

**C. GitHub Issue Monitoring (ADK Requirement #1)**
Automated issue monitoring and response:
```bash
# Check for mentions and respond
python eidolon.py --check-issues --project-repo hw9-yourusername
python eidolon.py --generate-status --project-repo hw9-yourusername
```

---

## 📦 Installation & Setup

### Requirements
```
Python 3.8+
requests (for GitHub integration)
```

### Install Dependencies
```bash
pip install requests --break-system-packages
```

### Project Structure
```
320-final-main/
├── main.py                  # Original dungeon generator CLI
├── eidolon.py              # EIDOLON-7 agent CLI
├── data/
│   ├── biomes.json         # Biome configurations
│   ├── enemies.json        # Enemy data
│   └── resources.json      # Resource definitions
├── src/
│   ├── dungeon.py          # Dungeon data structures
│   ├── generator.py        # Generation algorithms
│   ├── pathfinding.py      # BFS validation
│   ├── quality_metrics.py  # DQS evaluation system ✨
│   ├── eidolon_agent.py    # EIDOLON-7 ADK agent ✨
│   ├── github_integration.py # Issue monitoring ✨
│   ├── biome.py            # Biome system
│   ├── enemy.py            # Enemy management
│   ├── resource.py         # Resource system
│   └── renderer.py         # ASCII rendering
└── README.md
```

---

## 🎮 Usage Guide

### Original Generator (main.py)

#### Basic Generation
```bash
# Generate floor 1
python main.py --floor 1

# With animation
python main.py --floor 1 --animate --speed 0.5

# With validation
python main.py --floor 1 --validate

# With DQS evaluation ✨
python main.py --floor 1 --evaluate

# All features combined
python main.py --floor 12 --animate --validate --evaluate --speed 0.3
```

#### Advanced Options
```bash
# Specific biome
python main.py --floor 1 --biome vampire

# Custom dimensions
python main.py --floor 1 --width 80 --height 50

# Reproducible generation
python main.py --floor 1 --seed 42

# Save to file
python main.py --floor 1 --output floor1.txt
```

### EIDOLON-7 Agent (eidolon.py) ✨

#### Knowledge Queries
```bash
# Biome information
python eidolon.py --query-biome jungle
python eidolon.py --list-biomes
python eidolon.py --biome-enemies vampire
python eidolon.py --biome-resources snow

# Enemy information
python eidolon.py --query-enemy frost_wyrm
python eidolon.py --query-enemy vampire_lord

# Resource information
python eidolon.py --query-resource stardust
python eidolon.py --query-resource moonstone_shards

# Floor progression
python eidolon.py --floor-info 1
python eidolon.py --floor-info 33
python eidolon.py --floor-info 99
```

#### Generation with Evaluation
```bash
# Basic generation with DQS
python eidolon.py --generate --floor 1

# With narration (lore-friendly flavor text)
python eidolon.py --generate --floor 12 --show-narration

# Specific biome
python eidolon.py --generate --floor 1 --biome rocky

# Reproducible with seed
python eidolon.py --generate --floor 50 --seed 12345

# Custom size
python eidolon.py --generate --floor 1 --width 80 --height 50

# Save to file
python eidolon.py --generate --floor 1 --output floor1_report.txt
```

#### GitHub Integration
```bash
# Check for issue mentions (requires GITHUB_TOKEN env var)
export GITHUB_TOKEN="your_token_here"
python eidolon.py --check-issues --project-repo hw9-yourusername

# Generate status report only
python eidolon.py --generate-status --project-repo hw9-yourusername
```

#### Interactive Mode
```bash
# Start interactive shell
python eidolon.py --interactive

# Available commands in interactive mode:
EIDOLON-7> biomes
EIDOLON-7> biome jungle
EIDOLON-7> enemy frost_wyrm
EIDOLON-7> resource stardust
EIDOLON-7> floor 33
EIDOLON-7> generate 12
EIDOLON-7> help
EIDOLON-7> exit
```

---

## 🏗️ Architecture & AI Components

### Classical AI: BFS Pathfinding
The generator uses **Breadth-First Search** (BFS) to validate:
- All rooms are connected and reachable
- All resources are accessible to the player
- No isolated areas or dead ends exist
- Complete floor traversability

This classical AI algorithm ensures quality without requiring machine learning.

### Dungeon Quality Score (DQS) System

The DQS provides objective, quantifiable metrics:

**Individual Metrics:**
1. **Pathability** (0-1): Reachable tiles / Total walkable area
2. **Resource Accessibility** (0-1): Accessible resources / Total resources
3. **Room Connectivity** (0-1): Connected rooms / Total rooms
4. **Space Efficiency** (0-1): How efficiently space is used

**Overall Score Calculation:**
Weighted average:
- Room Connectivity: 35% (most critical)
- Resource Accessibility: 30%
- Pathability: 20%
- Space Efficiency: 15%

**Grading Scale:**
- S (0.95+): Perfect - Legendary Quality
- A+ (0.90-0.94): Exceptional
- A (0.85-0.89): Excellent
- A- (0.80-0.84): Very Good
- B+ (0.75-0.79): Good
- B (0.70-0.74): Above Average
- B- (0.65-0.69): Average
- C+ (0.60-0.64): Below Average
- C (0.50-0.59): Poor
- F (<0.50): Unacceptable

### EIDOLON-7 Agent Architecture

**Design Philosophy:**
- Lore-friendly: Positioned as an "Ancient Dungeon Overseer"
- Knowledge archive for game mechanics
- Quality evaluator and diagnostic system
- Natural language interface for generation

**Service Implementations:**

1. **Knowledge Service** (ADK Requirement #2)
   - Query biomes, enemies, resources
   - Floor progression information
   - Game mechanics explanations
   - Uses JSON data files as knowledge base

2. **Generation Service** (ADK Requirement #2)
   - Natural language dungeon generation
   - Automatic DQS evaluation
   - Optional narration and lore
   - Reproducible with seeds

3. **GitHub Service** (ADK Requirement #1)
   - Monitors `cs320f25/hw9-issues` repository
   - Responds ONLY when "EIDOLON-7" is mentioned
   - Analyzes YOUR project repository for status
   - Posts comprehensive status updates

---

## 📊 Example Outputs

### DQS Evaluation Report Example
```
============================================================
DUNGEON QUALITY EVALUATION REPORT
============================================================
Floor: 12
Biome: VAMPIRE
Dimensions: 60x40

OVERALL SCORE: 0.892 [A+]
Quality: Exceptional - Near Perfect

METRICS BREAKDOWN:
------------------------------------------------------------
  Room Connectivity:       100.0% (7/7 rooms)
  Resource Accessibility:  95.0% (19/20 resources)
  Pathability:             87.5% (875 reachable tiles)
  Space Efficiency:        95.2%

RAW STATISTICS:
------------------------------------------------------------
  Total Rooms:             7
  Total Enemies:           12
  Total Resources:         20
  Reachable Tiles:         875

✓ VALIDATION: PASSED
============================================================
```

### EIDOLON-7 Narration Example
```
⚡ EIDOLON-7 INITIATING FLOOR MANIFESTATION ⚡

Floor 12 has manifested within the VAMPIRE realm.
Shadows dance in gothic corridors.
Quality Assessment: Exceptional structure. This floor approaches ideal form.
```

---

## 🤖 ADK Service Documentation

### Required Service #1: GitHub Issue Monitoring

**Repository:** `cs320f25/hw9-issues`

**How It Works:**
1. EIDOLON-7 monitors all open issues in hw9-issues
2. Detects when an issue mentions "EIDOLON-7" semantically
3. Checks if it has already responded
4. Analyzes YOUR project repository (not hw9-issues)
5. Posts comprehensive status update as a comment

**Trigger Examples:**
- "Hey EIDOLON-7, can you give me a status update?"
- "@EIDOLON-7 what's the current state of the project?"
- "EIDOLON-7: show me your implementation progress"

**Status Report Includes:**
- Implementation phase breakdown
- Recent commits and activity
- Open issues/blockers
- Next steps
- Generated by EIDOLON-7 signature

**Setup:**
```bash
# Set GitHub token
export GITHUB_TOKEN="ghp_your_token_here"

# Run monitor
python eidolon.py --check-issues --project-repo hw9-yourusername
```

### Required Service #2: Natural Language Dungeon Service

**Two Core Capabilities:**

**A. Knowledge Service**
Ask questions about game mechanics in natural language:
- Biome themes and characteristics
- Enemy types and stats
- Resource locations
- Floor progression rules
- Difficulty scaling

**B. Generation & Evaluation Service**
Generate dungeons with natural language:
- "Generate Floor 12"
- "Create a Rocky biome dungeon"
- "Show me a small map"
- "Evaluate this floor"

Returns:
- ASCII dungeon visualization
- Pathability analysis
- Resource accessibility
- DQS score and grade
- Quality recommendations
- Optional lore narration

---

## 🎓 Assignment Compliance

### Checkpoint 2 Requirements ✅

**1. Mostly Complete Implementation**
✅ All major features implemented
✅ Core functionality working (with expected bugs)
✅ ADK agent components functional

**2. Required ADK Service #1: GitHub Issue Monitoring**
✅ Monitors cs320f25/hw9-issues
✅ Responds when "EIDOLON-7" is mentioned
✅ Analyzes OWN repository (not hw9-issues)
✅ Posts status updates as comments
✅ Only responds to issues directed at bot

**3. Required ADK Service #2: Project-Specific NL Service**
✅ Knowledge service (biomes, enemies, resources)
✅ Generation service (create dungeons via NL)
✅ Evaluation service (DQS quality analysis)

**4. Documentation**
✅ Updated README with setup instructions
✅ API documentation for both ADK services
✅ Examples of agent interactions
✅ Bot name (EIDOLON-7) clearly defined

### AI Engineering Components

**Classical AI:**
- BFS pathfinding for validation
- Constraint satisfaction (spawn rules)
- Heuristic optimization (quality metrics)
- Procedural generation algorithms

**ADK Agent:**
- Natural language knowledge queries
- Dungeon generation via NL interface
- Automated quality evaluation
- GitHub automation

**No ML Required:**
This project achieves AI objectives using classical algorithms, which is appropriate and acceptable for CS 320.

---

## 🧪 Testing Examples

### Test DQS System
```bash
# Generate multiple floors and compare scores
python main.py --floor 1 --evaluate
python main.py --floor 11 --evaluate  # Boss floor
python main.py --floor 50 --evaluate
python main.py --floor 99 --evaluate  # Boss floor
```

### Test EIDOLON-7 Knowledge
```bash
# Query different biomes
python eidolon.py --query-biome jungle
python eidolon.py --query-biome astral_void

# Query enemies
python eidolon.py --query-enemy jungle_titan
python eidolon.py --query-enemy celestial_sentinel

# Floor progression
python eidolon.py --floor-info 1
python eidolon.py --floor-info 33
python eidolon.py --floor-info 100
```

### Test Generation Service
```bash
# Different biomes
python eidolon.py --generate --floor 1 --biome jungle
python eidolon.py --generate --floor 1 --biome vampire
python eidolon.py --generate --floor 1 --biome astral_void

# Different sizes
python eidolon.py --generate --floor 1 --width 40 --height 30
python eidolon.py --generate --floor 1 --width 80 --height 60

# With narration
python eidolon.py --generate --floor 12 --show-narration
```

---

## 🔧 Known Issues & Future Work

### Known Issues
- Some edge cases may produce disconnected rooms (rare)
- Animation may flicker on some terminals
- GitHub API rate limiting if token not provided

### Future Enhancements (Optional)
- A* pathfinding (more advanced than BFS)
- Color-coded ASCII output
- JSON export of dungeons
- Multi-floor generation
- Performance benchmarking

---

## 📝 Credits

**Student:** Brandon Pyatt  
**Course:** AI Engineering (CS 320)  
**Instructor:** Professor DeFreez  

**Inspired by:** "Dungeon Ascend" game concept

**Agent Name:** EIDOLON-7 (Ancient Dungeon Overseer)

---

**Last Updated:** December 1, 2024  
**Checkpoint:** 2 (Substantial Progress)
