Dungeon Ascend Generator — Project Plan (CS 320)
Overview

This project implements a procedural dungeon generator that produces randomized ASCII dungeon floors using rooms, corridors, biomes, enemies, and resources.
A BFS-based validator evaluates each floor for connectivity, reachability, and resource accessibility.

An ADK agent, EIDOLON-7, provides natural language access to the generator and can answer questions about dungeon structure, biomes, enemies, and floor progression.

This document describes the current status of the project and the plan for completing the ADK integration.

Current Progress (Checkpoint 1 Complete)
Dungeon Generation

Grid-based floor creation

Room and corridor placement

Biome selection

Resource placement

Enemy placement

Configurable height/width

ASCII renderer

AI Validation

Implemented using classical search (BFS):

Room connectivity

Reachable tile count

Resource accessibility

Pathability evaluation

Basic “valid / invalid floor” logic

Data Files

biomes.json

enemies.json

resources.json

CLI Arguments

--floor

--validate

--animate

--speed

--width / --height

--biome

The generator, renderer, and validator are all functional.

Next Steps (Checkpoint 2)
1. Dungeon Quality Metrics

Add a structured evaluation layer that produces:

Pathability Percentage

Resource Accessibility Percentage

Connected Rooms Count

Total Walkable Tiles

Dungeon Quality Score (DQS)

These metrics will be returned to the user and used by the ADK agent.

Example:

Pathability: 92.4%
Resources Accessible: 100%
Connected Rooms: 6 / 6
DQS: 0.91 (Good)

2. ADK Natural Language Services (EIDOLON-7)

EIDOLON-7 will provide two services:

A. Dungeon Knowledge Service

Users can ask:

“Explain the Snow biome.”

“What enemies can spawn in the Vampire biome?”

“What happens on Floor 33?”

“List the resources available in the Swamp biome.”

“How does difficulty scale?”

EIDOLON-7 responds using the existing JSON data.

B. Dungeon Generation Service

Users can request:

“Generate Floor 12.”

“Make a dungeon in the Rocky biome.”

“Show me a small dungeon.”

“Evaluate this dungeon.”

The service will return:

ASCII dungeon

Pathability %

Resource accessibility %

Biome information

Optional narrative description

This fulfills the ADK natural language requirement.

Required ADK Feature: GitHub Issue Monitor

EIDOLON-7 will also:

Monitor the shared hw9-issues repository

Only respond to issues explicitly addressed to it

Analyze this project’s repository (not the issue repo)

Produce status updates including:

Implemented features

Remaining tasks

Known issues

Current generator status

Validation summary

This fulfills ADK Requirement #1.

How AI Is Used

This project does not use neural networks or model training.
The AI components are:

Classical Search (BFS)

Used to validate:

Dungeon reachability

Resource accessibility

Room connectivity

Overall map fairness

Evaluation Metrics

Numeric metrics act as a tuning and comparison mechanism, similar to evaluation loops in training, but without ML.

ADK Agent (LLM)

Used to:

Interpret natural language

Call the generator/validator

Explain biomes and enemies

Provide status updates

Final Deliverables

Fully functional dungeon generator

BFS-based validation system with DQS metrics

EIDOLON-7 ADK natural language services

GitHub issue monitoring bot

Updated documentation and examples

Optional Extensions

(Not required, but available if time allows)

Multi-floor generation

Heatmap visualization

Auto-tuning based on DQS

More in-world narrative responses
