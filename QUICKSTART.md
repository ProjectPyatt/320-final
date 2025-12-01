# QUICK START GUIDE - CHECKPOINT 2

## Installation

```bash
# Install dependencies
pip install -r requirements.txt --break-system-packages

# OR manually
pip install requests --break-system-packages
```

## Quick Tests

### 1. Test Basic Generation
```bash
# Simple floor generation
python main.py --floor 1

# With DQS evaluation
python main.py --floor 1 --evaluate
```

### 2. Test EIDOLON-7 Knowledge Service
```bash
# Query a biome
python eidolon.py --query-biome jungle

# Query an enemy
python eidolon.py --query-enemy frost_wyrm

# Get floor info
python eidolon.py --floor-info 33

# List all biomes
python eidolon.py --list-biomes
```

### 3. Test EIDOLON-7 Generation Service
```bash
# Generate with quality evaluation
python eidolon.py --generate --floor 1

# Generate with narration
python eidolon.py --generate --floor 12 --show-narration

# Generate specific biome
python eidolon.py --generate --floor 1 --biome vampire
```

### 4. Run Demo Script
```bash
# Full demonstration of all features
python demo.py
```

### 5. Test GitHub Integration (Optional)
```bash
# Set GitHub token
export GITHUB_TOKEN="ghp_your_token_here"

# Check for issue mentions
python eidolon.py --check-issues --project-repo hw9-yourusername

# Generate status report
python eidolon.py --generate-status --project-repo hw9-yourusername
```

## Key Commands Cheat Sheet

### Original Generator (main.py)
```bash
python main.py --floor 1 --validate           # Basic validation
python main.py --floor 1 --evaluate           # DQS evaluation
python main.py --floor 1 --animate            # Animation
python main.py --floor 11 --evaluate          # Boss floor with DQS
```

### EIDOLON-7 Agent (eidolon.py)
```bash
# Knowledge
python eidolon.py --query-biome [name]
python eidolon.py --query-enemy [name]
python eidolon.py --floor-info [number]

# Generation
python eidolon.py --generate --floor [number]
python eidolon.py --generate --floor [number] --biome [name]

# GitHub
python eidolon.py --check-issues --project-repo [name]
```

## Expected Output Examples

### DQS Evaluation
```
============================================================
DUNGEON QUALITY EVALUATION REPORT
============================================================
Floor: 1
Biome: JUNGLE
Dimensions: 60x40

OVERALL SCORE: 0.875 [A]
Quality: Excellent - High Quality
...
```

### EIDOLON-7 Knowledge Query
```
============================================================
BIOME: JUNGLE
============================================================
Theme: Lush, overgrown vegetation with hidden dangers
...
```

### EIDOLON-7 Generation
```
⚡ EIDOLON-7 INITIATING FLOOR MANIFESTATION ⚡
Generating Floor 1...

[ASCII DUNGEON MAP]

[DQS QUALITY REPORT]
```

## Troubleshooting

### Issue: Module not found
```bash
# Make sure you're in the project directory
cd 320-final-main

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Issue: GitHub API rate limit
```bash
# Use a GitHub token
export GITHUB_TOKEN="your_token"
```

### Issue: File not found errors
```bash
# Make sure data/ directory exists and contains:
# - biomes.json
# - enemies.json
# - resources.json
```

## What to Show Professor

1. **Run the demo script**: `python demo.py`
   - Shows all features in one run
   - Demonstrates both ADK services
   - Shows DQS evaluation

2. **Generate a few floors with evaluation**:
   ```bash
   python main.py --floor 1 --evaluate
   python main.py --floor 11 --evaluate
   python main.py --floor 50 --evaluate
   ```

3. **Show EIDOLON-7 knowledge queries**:
   ```bash
   python eidolon.py --query-biome vampire
   python eidolon.py --floor-info 33
   ```

4. **Show EIDOLON-7 generation**:
   ```bash
   python eidolon.py --generate --floor 12 --show-narration
   ```

5. **Explain GitHub integration** (even if not live):
   - Show the code in `src/github_integration.py`
   - Explain how it monitors and responds
   - Show example status report format

## Checkpoint 2 Checklist

✅ Mostly complete implementation  
✅ DQS metrics system working  
✅ EIDOLON-7 knowledge service functional  
✅ EIDOLON-7 generation service functional  
✅ GitHub integration code complete  
✅ Documentation updated  
✅ Examples provided  

## Next Steps for Checkpoint 3

- Deploy ADK agent (will be covered in class)
- Test live GitHub integration
- Polish any remaining bugs
- Add any requested features from feedback
