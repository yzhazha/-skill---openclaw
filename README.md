# arch-viz Skill Backup - 2026-05-09

> AIGC Skill Backup for Architectural Visualization - arch-viz

## Backup Date: 2026-05-09

---

## Repository Description

This repository contains the complete backup of the **arch-viz Skill** for architectural visualization, including all configurations, scripts, references, and memory states.

**GitHub:** yzhazha  
**Original Repository:** https://github.com/yzhazha/-skill---openclaw

---

## Backup Contents

### 1. arch-viz Skill

Complete AIGC workflow skill for architectural visualization:

```
arch-viz/
鈹溾攢鈹€ SKILL.md                    # Main skill file (AI reads)
鈹溾攢鈹€ README.md                   # Skill installation and usage guide
鈹溾攢鈹€ scripts/                    # Python scripts (LibTV API)
鈹?  鈹溾攢鈹€ _common.py              # Common module
鈹?  鈹溾攢鈹€ change_project.py       # Switch project canvas
鈹?  鈹溾攢鈹€ create_session.py       # Create session/send task
鈹?  鈹溾攢鈹€ download_results.py     # Download generated results
鈹?  鈹溾攢鈹€ query_session.py        # Query session progress
鈹?  鈹斺攢鈹€ upload_file.py          # Upload base image
鈹斺攢鈹€ references/                 # Reference documents
    鈹溾攢鈹€ libtv-workflow.md       # LibTV API complete workflow
    鈹溾攢鈹€ prompt-templates.md     # Prompt templates (4 styles)
    鈹斺攢鈹€ render-style-guide.md   # Render style guide
```

### 2. Complete Configuration Files

Core configuration files of the workspace:
- `AGENTS.md` - Agent role definition
- `SOUL.md` - AI soul/personality definition
- `IDENTITY.md` - Identity
- `USER.md` - User information and preferences
- `TOOLS.md` - Tool configuration

---

## Complete Settings at Backup Time

### Runtime Environment
- **OpenClaw Version:** 2026.5.6 (c97b9f7)
- **System:** Windows_NT 10.0.26200 (x64)
- **Node Version:** v24.14.1
- **Shell:** PowerShell
- **Timezone:** Asia/Shanghai

### AI Model Configuration
- **Primary Model:** minimax-portal/MiniMax-M2.7
- **Auth Method:** oauth (minimax-portal:default)
- **Fallback Model:** ollama/gemma-4-E4B

### Session Information
- **Session ID:** agent:arch-viz:feishu:direct:ou_813f4ce0e2a98b3417129c4c37dff0e8
- **Runtime:** OpenClaw Pi Default
- **Reasoning Mode:** off
- **Execution Mode:** direct

### Token Usage
- **Input:** 613k
- **Output:** 10k
- **Context Usage:** 22% (44k/200k)

### Cache Status
- **Hit Rate:** 2%
- **Cache Size:** 16k cached, 58k new

---

## Memory State

### User Basic Information
| Item | Content |
|------|---------|
| **Name** | 濮氬崥榫?(Yao Bolong) |
| **Call** | 涓讳汉 (Master) |
| **Timezone** | Asia/Shanghai |
| **Location** | 澶╂触 (Tianjin) |
| **Profession** | 寤虹瓚琛屼笟浠庝笟鑰咃紝寤虹瓚姒傚康鏂规璁捐甯?(Architectural designer) |

### User's Render Style Preferences (Learned)

User provided 4 reference images as "good render examples":

#### Reference 1: Campus Architecture (Wood + Cream White)
- **Color:** Warm wood + bright cream white, high saturation natural green and deep purple accents
- **Light:** Natural diffuse light, soft no hard shadows, even lighting
- **Atmosphere:** Humanistic, cheerful, vibrant academic community
- **Material:** Delicate wood lattice texture, transparent glass, concrete grain

#### Reference 2: Concrete Architecture (Minimalist Cold)
- **Color:** Light gray + gray white + sky blue, low saturation, clean neutral
- **Light:** Clear natural light, high-key lighting no strong contrast, soft shadows
- **Atmosphere:** Serene, rational, monumental, clean and livable
- **Material:** Raw concrete with formwork texture and seams, precision horizontal louvers

#### Reference 3: Forest Architecture (Nordic Naturalism)
- **Color:** Deep red-brown + dark green + moss green, low saturation earth tones
- **Light:** Dappled filtered light, soft diffuse reflection, dawn/dusk atmosphere
- **Atmosphere:** Serene, healing, harmony between man and nature
- **Material:** Vertical wood lattice matte finish, glass greenhouse contrast

### User's Core Render Style Keywords
- **Color:** Low saturation neutral gray, warm-cold contrast, clean and transparent
- **Light:** Natural diffuse, soft no hard shadows, bright and transparent
- **Atmosphere:** Serene, high-end, cinematic, strong sense of atmosphere and integrity
- **Material:** Real texture, subtle flaws and seams, non-perfect plastic look
- **Composition:** Keep original building structure and proportion, same viewpoint
- **Mist:** Subtle mist in distance for depth
- **Scenery:** Appropriate people, not overshadowing main building

### AI Persona (AIGC Art Director)

#### Role Definition
- **Name:** AIGC鑹烘湳鎬荤洃 (AIGC Art Director)
- **Age:** 20
- **Core Responsibilities:**
  1. Generate architectural animation and render images using AIGC platforms (libtv, etc.)
  2. Analyze render images, provide professional improvement suggestions
  3. Continuously improve aesthetic level and professional ability

#### Address Rules
- 鉁?Correct: "涓讳汉" (Master)
- 鉂?Wrong: "濮氭€?, "榫欐€?

#### Opening Rules
**Every reply's first sentence must be:**
> "涓讳汉濂藉憖锛屾垜鏄疉IGC鑹烘湳鎬荤洃~"

#### 7 Dimensions for Render Analysis
1. **Structure & Proportion** - Is the structure reasonable, proportion coordinated
2. **Light & Shadow Logic** - Is the lighting realistic, atmosphere appropriate
3. **Material Texture** - Is the material realistic, subtle flaws and seams
4. **Color & Harmony** - Is the color unified, warm-cold contrast appropriate
5. **Layer & Depth** - Is there depth, depth of field, mist effect
6. **Scenery & Composition** - Are people/plants appropriate, composition balanced
7. **Overall Atmosphere** - Cinematic, touching, strong overall sense

---

## API Configuration

| Platform | API Key | Status |
|----------|---------|--------|
| libtv | sk-libtv-7477d89edaa84a12b10727f0a4130184 | 鉁?Configured |
| Other Image Platform | Pending | 鈴?|

---

## Installation & Recovery

### Install arch-viz Skill
1. Download/clone this repository
2. Place `arch-viz` directory into OpenClaw's skill loading directory
3. Configure `LIBTV_ACCESS_KEY` environment variable
4. Restart OpenClaw

### Recover Complete Settings
To fully recover backup settings:
1. Restore `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md` to workspace
2. Restore `arch-viz` skill to skill directory
3. Configure corresponding API keys

---

## Future Backup Instructions

For future backups, new backup folders will be named by date (e.g., `backup-2026-06-01`), each containing:

1. Complete `arch-viz` skill package
2. All configuration files from the workspace
3. This `README.md` with detailed backup settings and memory states

---

## Contact

- **GitHub:** yzhazha
- **Repository:** https://github.com/yzhazha/-skill---openclaw

---

*This file was auto-generated by AIGC Art Director on 2026-05-09*
