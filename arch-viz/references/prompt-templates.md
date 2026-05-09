# Prompt Template Library

Successful prompt templates for architectural render image-to-image tasks.

## General Template Structure

```
Reference image: <base-image-OSS-URL>

[Important] Please strictly generate an image according to the following requirements:

[Model Selection]
- Model: Lib Nano pro

[Image Parameters]
- Aspect ratio: 16:9
- Resolution: 2K
- Count: Generate only 1 image

[Base Image Reference]
- Must use provided reference image as base
- Strictly maintain the main structure, proportion, and viewpoint of the building in reference image
- Only perform style transfer and material rendering, do not change building form

[Style Transfer Requirements]
Convert the base image SU model to MIR international competition style architectural bird's-eye render

[Image Requirements]
- Daytime scene
- Strong overall feeling and atmosphere
- Building facade: glass curtain wall and metal lattice materials
- Subtle mist in the distance
- Appropriate people in the scene
- Trees and plants on both sides of the image
- Professional architectural photography lighting effect
- Ultra high resolution image details

[Color and Tone]
- High-key white and light gray as base, local color accents
- Bright and pure overall tone, highlighting the visual center of the building
- Modern, vibrant, and fresh color perception

[Expression and Style]
- Commercial realistic rendering style
- Emphasize clarity of architectural geometric forms
- Rich people and scene materials with life atmosphere
- Enhance scene immersion and social participation through human viewpoint composition

[Environment and Scenery]
- Delicate urban plaza environment
- Foreground opens up spatial layers with realistic stone paving
- Mid-ground with green plants and public facilities
- Create a prosperous, pleasant, and open community commercial atmosphere

[Weather and Time]
- Simulate bright, transparent sunny environment
- Large area of white sky, presenting a near-overexposed highlight feeling
- Soft light and shadow relationship, transparent shadows without heaviness
- Sufficient natural daylight effect

[Key Reminder]
This is an image-to-image task, must use the building model in reference image as base,
building main structure, proportion, and viewpoint must be exactly the same as reference image, cannot change building form.
```

---

## MIR Competition Style Template

Applicable: Competition renders, bidding documents, high-end presentations

```
Reference image: <OSS-URL>

[Important] Please strictly generate an image according to the following requirements:

[Model Selection]
- Model: Lib Nano pro
- Style preset: MIR International Competition Style

[Image Parameters]
- Aspect ratio: 16:9
- Resolution: 2K
- Count: 1 image

[Base Image Reference]
Strictly maintain the main structure, proportion, and viewpoint of the building in reference image unchanged

[MIR Competition Style Requirements]
- High-key white light gray base, bright and pure
- Serene, high-end, cinematic atmosphere
- Soft diffuse light, no hard shadows
- Subtle mist in distance for depth
- Professional architectural photography lighting
- Emphasize clarity of architectural geometric forms

[Color]
- Low saturation neutral gray
- Appropriate warm-cold contrast
- Local accent colors

[Material]
- Real texture, subtle seams
- Non-perfect plastic look
- Glass curtain wall, metal lattice, wood lattice each with different texture

[Scenery]
- Appropriate people, not overshadowing main building
- Green plants, trees for vitality
- Foreground stone paving for layer

[Key Reminder]
Image-to-image task, must use reference image as base, building form cannot be changed.
```

---

## Commercial Realistic Style Template

Applicable: Real estate displays, commercial projects, promotional materials

```
Reference image: <OSS-URL>

[Important] Please strictly generate an image according to the following requirements:

[Model Selection]
- Model: Lib Nano pro
- Style: Commercial Realistic Rendering

[Image Parameters]
- Aspect ratio: 16:9
- Resolution: 2K
- Count: 1 image

[Base Image Reference]
Strictly maintain the main structure, proportion, and viewpoint of the building in reference image unchanged

[Commercial Realistic Requirements]
- Rich people and scene materials with life atmosphere
- Prosperous, pleasant community commercial atmosphere
- Urban plaza environment
- Foreground realistic stone paving
- Mid-ground green plants and public facilities

[Color]
- Bright and pure, high-key lighting
- Modern, vibrant, and fresh
- White and light gray as main base

[Light and Shadow]
- Soft shadows, transparent without heaviness
- Sufficient natural daylight
- Bright and transparent sunny environment

[Key Reminder]
Image-to-image task, must use reference image as base.
```

---

## Nordic Natural Style Template

Applicable: Residential, forest architecture, nature-proximity projects

```
Reference image: <OSS-URL>

[Important] Please strictly generate an image according to the following requirements:

[Model Selection]
- Model: Lib Nano pro

[Image Parameters]
- Aspect ratio: 16:9
- Resolution: 2K
- Count: 1 image

[Base Image Reference]
Strictly maintain the main structure, proportion, and viewpoint of the building in reference image unchanged

[Nordic Natural Style Requirements]
- Low saturation earth tones (deep red-brown, dark green, moss green)
- Serene, healing, harmony between man and nature
- Dappled filtered light, soft diffuse reflection
- Dawn/dusk atmosphere

[Material]
- Vertical wood lattice matte finish
- Glass greenhouse contrast
- Natural materials mainly

[Environment]
- Harmony between man and nature
- Surrounded by forest/green space
- Subtle mist

[Key Reminder]
Image-to-image task, must use reference image as base.
```

---

## Prompt Building Checklist

Before sending prompt, verify:

- [ ] Base image URL at prompt beginning, format: `Reference image: <URL>`
- [ ] [Base Image Reference] requirements marked: keep building structure proportion viewpoint unchanged
- [ ] [Key Reminder] emphasized: This is an image-to-image task
- [ ] All push info extracted from current generation result, not from history
- [ ] No self-invented style descriptions in prompt (like "ultra realistic, 8K" etc.)
