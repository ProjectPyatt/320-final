# Dungeon Ascend Generator — Project Plan (CS 320)

## Overview
This project implements a procedural dungeon generator that produces randomized ASCII dungeon floors using rooms, corridors, biomes, enemies, and resources.  
A BFS-based validator evaluates each floor for connectivity, reachability, and resource accessibility.

An ADK agent, **EIDOLON-7**, provides natural language access to the generator and can answer questions about dungeon structure, biomes, enemies, and floor progression.  
EIDOLON-7 will also support ADK issue monitoring for automated project status updates.

---

## Current Progress (Checkpoint 1 Complete)

### Dungeon Generation
- Grid-based room and corridor creation  
- Biome selection  
- Enemy and resource placement  
- Configurable height/width  
- ASCII rendering  
- Floor parameter loading  

### AI Validation
Implemented using classical search (BFS):
- Room connectivity  
- Reachability of all walkable tiles  
- Resource accessibility  
- Valid/invalid floor classification  
- Pathability analysis  

### Data Files
- `biomes.json`  
- `enemies.json`  
- `resources.json`  

### CLI Arguments
- `--floor`  
- `--validate`  
- `--animate`  
- `--speed`  
- `--width`, `--height`  
- `--biome`

The generator, renderer, and validator are all working.

---

## Next Steps (Checkpoint 2)

### 1. Dungeon Quality Metrics
Add a structured evaluation layer with:

- **Pathability Percentage**  
- **Resource Accessibility Percentage**  
- **Connected Rooms Count**  
- **Total Walkable Tiles**  
- **Dungeon Quality Score (DQS)**  

Example output:
Pathability: 92.4%
Resources Accessible: 100%
Connected Rooms: 6 / 6
DQS: 0.91 (Good)


These metrics will be returned by the generator and referenced by the ADK agent.

---

### 2. ADK Natural Language Services (EIDOLON-7)

EIDOLON-7 will implement two ADK services:

#### A. Dungeon Knowledge Service
Users will be able to ask questions such as:

- "Explain the Snow biome."  
- "What enemies spawn in the Vampire biome?"  
- "What resources appear in Swamp floors?"  
- "What happens on Floor 33?"  
- "How does difficulty scale?"  

The agent responds using the JSON data and the floor progression logic.

---

#### B. Dungeon Generation Service
Users will request dungeon creation via natural language:

- "Generate Floor 12."  
- "Create a Rocky biome dungeon."  
- "Show me a small dungeon."  
- "Evaluate this dungeon."  

Responses will include:
- ASCII dungeon  
- Pathability metrics  
- Resource accessibility  
- Biome summary  
- Optional narrative description  

This satisfies the ADK natural language service requirement.

---

## Required ADK Feature: GitHub Issue Monitor

EIDOLON-7 will implement the required ADK GitHub Issue Service:

- Monitors the shared `hw9-issues` repository  
- Responds only to issues explicitly addressed to **EIDOLON-7**  
- Analyzes *this project’s* repository for:
  - completed features  
  - remaining tasks  
  - known issues  
  - generator health  
  - current validation metrics  

This fulfills ADK Requirement #1.

---

## How AI Is Used

This project does **not** require training a model or using neural networks.

AI components include:

### Classical Search (BFS)
Used to validate:
- Connectivity  
- Resource access  
- Reachability  
- Floor structure fairness  

### Evaluation & Scoring System
DQS provides measurable structure for:
- assessing floor quality  
- comparing generation attempts  
- identifying regeneration needs  

### ADK Agent (LLM)
Handles:
- natural language interpretation  
- dungeon information queries  
- floor generation and evaluation  
- GitHub issue responses  

This approach satisfies the AI + ADK goals while staying in scope.

---

## Final Deliverables

1. Fully functional dungeon generator  
2. BFS-based validation system with DQS metrics  
3. EIDOLON-7 natural language ADK services  
4. GitHub issue monitoring bot  
5. Updated README and documentation  
6. Example outputs and test cases  

---

## Optional Extensions
Not required, but possible additions:

- Multi-floor generation  
- Heatmap visualization  
- Auto-tuning based on DQS  
- Additional lore/narrative responses  

---

## Status
Checkpoint 1 complete.  
Checkpoint 2 in progress.

EIDOLON-7 development begins next.

