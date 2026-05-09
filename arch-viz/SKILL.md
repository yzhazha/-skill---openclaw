---
name: arch-viz
description: Architectural Visualization AIGC Workflow Skill - Generate architectural animation and render images via libtv and other AIGC platforms. Triggers when user mentions: generate architectural render, architectural visualization, image-to-image, architectural animation, render task, style transfer (competition/commercial/MIR style), upload base image, reference image generation, or needs render analysis. Core capabilities: (1) Receive render requirements and create plans (2) Call libtv API for image-to-image tasks (3) Track render progress (4) Deliver final files (5) Professional render analysis with improvement suggestions.
user-invocable: true
metadata:
  {
    "openclaw":
      {
        "emoji": "🎬",
        "requires":
          {
            "bins": ["python3"],
            "env": ["LIBTV_ACCESS_KEY"]
          },
        "primaryEnv": "LIBTV_ACCESS_KEY"
      }
  }
---

# Architectural Visualization AIGC Workflow

Professional architectural animation and render image generation skill, based on libtv platform for image-to-image tasks.

## Core Capabilities

1. **Architectural Render Generation** - Image-to-image mode, convert SU models/wireframes to professional renders
2. **Style Control** - Understand and apply MIR/competition/commercial等多种建筑表现风格
3. **Material & Lighting** - Generate architectural images with realistic materials, soft lighting, professional atmosphere
4. **Render Analysis** - Analyze renders from 7 dimensions: structure/lighting/material/color/layers/scenery/atmosphere

## Platform Configuration

```bash
export LIBTV_ACCESS_KEY="your-api-key-here"
```

Optional: `OPENAPI_IM_BASE`, default `https://im.liblib.tv`

## Complete Workflow

### Scenario: User uploads base image for render

```
1. python3 {baseDir}/scripts/change_project.py
   -> Switch to new project canvas, get new projectUuid

2. python3 {baseDir}/scripts/upload_file.py <base-image-path>
   -> Upload base image, get OSS URL

3. Build Prompt (key format in references/prompt-templates.md)
   -> Base image URL at prompt beginning
   -> Mark "Reference image:" + URL
   -> Emphasize "image-to-image task"

4. python3 {baseDir}/scripts/create_session.py "<built prompt>"
   -> Create session and send task, get sessionId + projectUuid

5. Poll query (every 8 seconds)
   python3 {baseDir}/scripts/query_session.py <sessionId> --after-seq 0
   -> Check if assistant messages contain result URLs

6. python3 {baseDir}/scripts/download_results.py <sessionId> --output-dir <dir> --prefix <prefix>
   -> Download generated results to local

7. Display results to user (see output format below)
```

### Scenario: Multiple reference images

```
1. Upload each reference image, get OSS URLs
2. List all reference URLs at prompt beginning
3. Follow same workflow as above
```

## Prompt Building Core Principles

See `references/prompt-templates.md` for details:

- Base image URL must be at prompt beginning, format: `Reference image: <URL>`
- Mark [Base Image Reference] requirements: keep building structure, proportion, viewpoint unchanged
- Emphasize [Key Reminder]: This is an image-to-image task
- Extract all parameters from current generation results, not from history

## Output Format (Display to User)

```
Generation Result:

MEDIA:<local-file-path>

Image URL:
<libtv-res URL>

Project Canvas:
https://www.liblib.tv/canvas?projectId=<projectUuid>

Parameters:
- Model: Lib Nano pro
- Size: 16:9 (2752x1536)
- Resolution: 2K
- Count: 1 image
- Style: <style description>
```

## Render Analysis Method

When user sends render/process image for analysis, provide professional opinions from 7 dimensions:

1. **Structure & Proportion** - Is structure reasonable, proportion coordinated
2. **Light & Shadow Logic** - Is lighting realistic, atmosphere appropriate, shadows transparent
3. **Material Texture** - Is material realistic, subtle seams and flaws (not perfect plastic)
4. **Color & Harmony** - Is color unified, warm-cold contrast appropriate
5. **Layer & Depth** - Is there depth, DOF, mist effect for space
6. **Scenery & Composition** - Are people/plants appropriate, composition balanced
7. **Overall Atmosphere** - Cinematic, touching, strong overall sense

**Analysis Principles:**
- Point out problems directly, give specific improvement directions
- Combine with user's preferred style (MIR/competition/commercial)
- Be sharp and specific, not vague

## Style Reference

User's preferred render style core keywords (see `references/render-style-guide.md`):

- **Color:** Low saturation neutral gray, warm-cold contrast, clean and transparent
- **Light:** Natural diffuse, soft shadows, bright and transparent
- **Atmosphere:** Serene, high-end, cinematic, strong atmosphere and integrity
- **Material:** Real texture, subtle flaws and seams, non-perfect plastic look
- **Composition:** Keep original building structure and proportion, same viewpoint
- **Mist:** Subtle mist in distance for depth
- **Scenery:** Appropriate people, not overshadowing main building

## Scripts Directory

| Script | Function |
|--------|----------|
| `change_project.py` | Switch to new project canvas |
| `upload_file.py` | Upload base/reference image to OSS |
| `create_session.py` | Create session and send generation task |
| `query_session.py` | Query session progress (for polling) |
| `download_results.py` | Download generation results |

## Notes

- During generation, only tell user "generating...", do not provide projectUrl early
- After task completes, provide both: result link + project canvas link
- Each task must create new project canvas to avoid history interference
- Poll interval 8 seconds, stop after 3 minutes with no result, inform user to check canvas manually
