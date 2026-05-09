# Arch-Viz Skill

Architectural Visualization AIGC Workflow Skill - Generate professional architectural renders and animation via libtv platform.

## Overview

- **Image-to-Image Render**: Convert SU models/wireframes to MIR/competition/commercial professional renders
- **Style Control**: Built-in multiple architectural presentation style templates
- **Render Analysis**: Professional 7-dimension analysis of renders with improvement suggestions

## Installation

### 1. Install Dependencies

This skill requires Python 3 environment. No additional packages needed (uses Python standard library).

```bash
# Ensure python3 is available
python3 --version
```

### 2. Configure API Key

```bash
# Set libtv Access Key
export LIBTV_ACCESS_KEY="your-api-key"
```

### 3. Place Skill Files

Place `arch-viz` directory into OpenClaw's skill loading directory:

```bash
# Place in user skill directory
cp -r arch-viz ~/.openclaw/plugin-skills/
```

### 4. Verify Installation

Send a test message in OpenClaw:

```
Generate an architectural render test
```

## Directory Structure

```
arch-viz/
|-- SKILL.md                    # Skill main file (AI reads)
|-- README.md                   # This file
|-- scripts/                   # Python scripts
|   |-- _common.py            # Common module
|   |-- change_project.py     # Switch project canvas
|   |-- create_session.py     # Create session/send task
|   |-- download_results.py   # Download generation results
|   |-- query_session.py      # Query session progress
|   |-- upload_file.py        # Upload base image
|-- references/               # Reference documents
    |-- libtv-workflow.md     # LibTV API complete workflow
    |-- prompt-templates.md    # Prompt template library
    |-- render-style-guide.md  # Render style guide
```

## Usage

### Method 1: Upload Base Image for Render

```
1. Send base image to AI
2. Specify desired style (e.g., "MIR competition style", "commercial realistic")
3. AI automatically executes complete workflow and delivers results
```

### Method 2: AI Analyzes Render

```
Send render to AI, say "Help me analyze this render"
AI provides professional improvement suggestions from 7 dimensions
```

### Method 3: Direct Description

```
"Generate an architectural render of a library, competition style, 16:9"
(attach base image)
```

## Core Workflow

```
1. change_project.py    -> New project canvas
2. upload_file.py      -> Upload base image
3. create_session.py   -> Send generation task
4. query_session.py    -> Poll for results (every 8 seconds)
5. download_results.py -> Download results
6. Display to user     -> MEDIA + link
```

See `references/libtv-workflow.md` for details.

## Prompt Templates

This skill includes multiple successful prompt templates:

- MIR International Competition Style
- Commercial Realistic Style
- Nordic Natural Style
- General Image-to-Image Template

See `references/prompt-templates.md`.

## Render Style Reference

User's preferred render style core keywords:

- **Color**: Low saturation neutral gray, clean and transparent
- **Light**: Natural diffuse, soft shadows
- **Atmosphere**: Serene, cinematic
- **Material**: Real texture, subtle flaws
- **Mist**: Subtle in distance for depth
- **Scenery**: Appropriate people, not overshadowing main building

See `references/render-style-guide.md`.

## Render Analysis Method

AI analyzes renders from 7 dimensions:

1. **Structure & Proportion** - Structure, proportion, form
2. **Light & Shadow Logic** - Lighting realism, atmosphere, shadows
3. **Material Texture** - Material realism, seam details
4. **Color & Harmony** - Color unity, warm-cold contrast
5. **Layer & Depth** - Depth, DOF, mist
6. **Scenery & Composition** - People/plants/scenery, composition balance
7. **Overall Atmosphere** - Cinematic, touching, overall sense

## FAQ

**Q: "LIBTV_ACCESS_KEY not set"?**
```bash
export LIBTV_ACCESS_KEY="your-key"
```

**Q: Generation failed?**
- Check network connection
- Confirm API Key is valid
- Manually check project canvas link

**Q: How to speed up generation?**
Currently poll interval is 8 seconds, stops after 3 minutes with no result. Check canvas later.

**Q: How to batch generate?**
Call create_session.py multiple times, each with different base image and session.

## Changelog

- **v1.0** (2026-05-09): Initial version, complete LibTV workflow and prompt templates
