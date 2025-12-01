# VIDEO DEMO SCRIPT - CHECKPOINT 2
## Procedural Dungeon Generator with EIDOLON-7 Agent

**Duration:** 5-7 minutes  
**Purpose:** Demonstrate all Checkpoint 2 features for grading

---

## INTRO (30 seconds)

**[Show terminal with project directory]**

"Hi, I'm Brandon Pyatt, and this is my Checkpoint 2 submission for the CS 320 Dungeon Ascend Generator project. 

Today I'll be demonstrating three major additions:
1. The Dungeon Quality Score system
2. The EIDOLON-7 ADK agent
3. GitHub integration for issue monitoring

Let's get started."

---

## PART 1: Basic DQS Demonstration (1-2 minutes)

**[Terminal]**

"First, let me show you the original generator with the new DQS evaluation."

```bash
python main.py --floor 1 --evaluate
```

**[While it runs]**

"This generates a dungeon floor and evaluates it using our new Dungeon Quality Score system. The DQS uses four metrics: room connectivity, resource accessibility, pathability, and space efficiency."

**[Show output]**

"As you can see, we get:
- An ASCII visualization of the dungeon
- A comprehensive quality report
- An overall score with a letter grade
- Detailed breakdowns of each metric

This floor scored [X.XXX] with a grade of [GRADE], which means [DESCRIPTION].

The system validates that all rooms are connected and all resources are accessible using BFS pathfinding."

---

## PART 2: EIDOLON-7 Knowledge Service (2 minutes)

**[Terminal]**

"Now let me introduce EIDOLON-7, our ADK agent. EIDOLON-7 provides three services. First, the knowledge service."

```bash
python eidolon.py --greeting
```

**[Show greeting]**

"EIDOLON-7 is positioned as an 'Ancient Dungeon Overseer' - a lore-friendly interface for querying game mechanics."

```bash
python eidolon.py --query-biome jungle
```

**[While running]**

"You can ask about biomes, enemies, and resources using natural language queries."

**[Show output]**

"Here we see complete information about the Jungle biome: theme, characteristics, available resources, enemies, and the mega-boss."

```bash
python eidolon.py --floor-info 33
```

**[Show output]**

"You can also query floor progression. Floor 33 is a mega-boss floor in the mid-game tier with hard difficulty."

```bash
python eidolon.py --list-biomes
```

"The agent has access to all 9 biomes in the game, from Jungle to Astral Void."

---

## PART 3: EIDOLON-7 Generation Service (2 minutes)

**[Terminal]**

"The second service is dungeon generation with quality evaluation."

```bash
python eidolon.py --generate --floor 12 --show-narration
```

**[While running]**

"EIDOLON-7 can generate dungeons and automatically evaluate them. With the narration flag, we get lore-friendly flavor text."

**[Show output]**

"Look at the output:
- EIDOLON-7's narration about the floor manifestation
- The ASCII dungeon with enemies and resources
- A complete DQS evaluation report

This satisfies the ADK requirement for a natural language service that exposes project functionality."

```bash
python eidolon.py --generate --floor 1 --biome vampire
```

**[While running]**

"You can also request specific biomes. This is generating a vampire-themed floor."

**[Show output briefly]**

"Each generation includes the complete quality analysis, so you can compare different generations objectively."

---

## PART 4: GitHub Integration (1-2 minutes)

**[Terminal or show code]**

"The third service is GitHub issue monitoring. Let me show you how this works."

**[Option A: Show the code]**

```bash
cat src/github_integration.py | head -50
```

"The GitHubIssueMonitor class monitors the cs320f25/hw9-issues repository. When it detects an issue mentioning 'EIDOLON-7', it:

1. Checks if it has already responded
2. Analyzes my actual project repository
3. Generates a comprehensive status update
4. Posts it as a comment

Importantly, it analyzes MY repository, not the issues repository, to provide accurate status information."

**[Show status generation]**

```bash
python eidolon.py --generate-status --project-repo hw9-example
```

**[Show output]**

"Here's an example status report. It includes:
- Implementation phase breakdown
- Recent activity
- Open issues or blockers
- Next steps
- EIDOLON-7's signature

This satisfies ADK Requirement #1 for GitHub issue monitoring."

**[Note about live testing]**

"For live testing, you'd set a GITHUB_TOKEN environment variable and run the check-issues command. The code is complete and ready for deployment in Checkpoint 3."

---

## PART 5: Comparison Demo (1 minute)

**[Terminal]**

"Let me quickly demonstrate the quality metrics across different floors."

```bash
python eidolon.py --generate --floor 1
```

**[Brief pause]**

"Floor 1 - Tutorial zone..."

```bash
python eidolon.py --generate --floor 11
```

"Floor 11 - First mega-boss floor..."

```bash
python eidolon.py --generate --floor 50
```

"Floor 50 - Mid-game, harder difficulty..."

**[Show comparison]**

"Notice how the DQS scores allow us to objectively compare quality across different generations. The metrics are consistent and meaningful."

---

## CLOSING (30 seconds)

**[Show file structure or README]**

"All code is well-documented with:
- A comprehensive README for Checkpoint 2
- A quick start guide
- Implementation summary
- Architecture documentation
- Test scripts

The project meets all Checkpoint 2 requirements:
✓ Mostly complete implementation
✓ ADK Service #1 - GitHub monitoring
✓ ADK Service #2 - Natural language services
✓ Complete documentation

Thank you for watching. I'm looking forward to deployment in Checkpoint 3!"

---

## ALTERNATIVE: Automated Demo Script

**[Instead of manual demo]**

"If you prefer, you can run the automated demo script that walks through all features:"

```bash
python demo.py
```

**[Let it run]**

"This interactive script demonstrates:
- Knowledge queries
- Generation with evaluation
- Quality comparisons
- GitHub integration explanation

And includes a comprehensive summary at the end."

---

## RECORDING TIPS

**Setup:**
- Clear terminal
- Larger font (for readability)
- Dark theme (easier on eyes)
- Terminal window: 80-100 columns wide

**Before Recording:**
```bash
clear
export PS1="$ "  # Simple prompt
cd 320-final-checkpoint2
```

**Optional: Pre-generate examples**
```bash
# Generate a few examples beforehand to show variety
python eidolon.py --generate --floor 1 --seed 42 --output floor1.txt
python eidolon.py --generate --floor 11 --seed 43 --output floor11.txt
python eidolon.py --generate --floor 50 --seed 44 --output floor50.txt
```

**Pacing:**
- Speak clearly and not too fast
- Pause after each command to show output
- Don't rush through the quality reports
- Emphasize the key metrics

**Key Points to Emphasize:**
1. DQS provides objective quality measurement
2. EIDOLON-7 has three distinct services
3. All services work via natural language
4. GitHub integration is complete and ready
5. Documentation is comprehensive

---

## BACKUP PLAN

If anything breaks during recording:

1. **Use the demo script** - It's tested and reliable
2. **Show pre-generated outputs** - Have examples ready
3. **Walk through code** - Show the implementation
4. **Reference documentation** - It's all there

---

## TIME BREAKDOWN

- Intro: 0:00 - 0:30
- DQS Demo: 0:30 - 2:00
- Knowledge Service: 2:00 - 4:00
- Generation Service: 4:00 - 6:00
- GitHub Integration: 6:00 - 7:00
- Closing: 7:00 - 7:30

**Total:** ~7:30 minutes

Can be shortened to 5 minutes by:
- Faster pacing
- Fewer examples
- Skip some knowledge queries
- Show GitHub code instead of demo

---

## SCREENSHOT CHECKLIST

If doing screenshots instead of video:

1. ✓ DQS evaluation report
2. ✓ EIDOLON-7 greeting
3. ✓ Biome query result
4. ✓ Floor info result
5. ✓ Generation with narration
6. ✓ Quality comparison table
7. ✓ Status report example
8. ✓ File structure
9. ✓ Architecture diagram
10. ✓ Test results

---

Good luck with your presentation!
