# Migrating from Adobe Photoshop to GIMP

Switching from Adobe Photoshop to [GIMP](https://www.gimp.org/) is straightforward for web graphics, photo retouching, screenshots, and social assets. Print production teams that depend on native CMYK editing, Smart Objects, or Linked Adobe Creative Cloud Libraries will hit real workflow gaps and should pair GIMP with Darktable (for RAW photos) or Scribus (for CMYK print layout).

[Back to main catalog](../README.md) | [Design & Graphics category](../categories/design.md)

## Expected difficulty

Medium. Most users need 3 to 7 days to adjust to GIMP's menu structure, keyboard shortcuts, and export model.

## Workflow differences to know upfront

- Saving vs. exporting: In GIMP, `File -> Save` always writes the native `.xcf` project format. To produce a `.png`, `.jpg`, or `.webp` file, use `File -> Export As` (`Ctrl+Shift+E` / `Cmd+Shift+E`).
- Non-destructive filters: GIMP 3.0 introduced non-destructive layer filters, closing a long-standing gap with Photoshop, though complex Photoshop Smart Objects still flatten on import.
- RAW files: GIMP does not open camera RAW files on its own. Install [Darktable](https://www.darktable.org/) or [RawTherapee](https://www.rawtherapee.com/), and GIMP will invoke it automatically when you open a `.CR2`, `.NEF`, or `.ARW` file.
- Selection and transform behavior: Moving or pasting content creates a floating selection in older workflows; anchor it to the current layer or convert it to a new layer before applying other tools.

## Step 1: Audit and convert existing PSD files

GIMP opens standard `.psd` files with layers, masks, and basic blending modes intact. Before cancelling Photoshop, check critical `.psd` templates for:

1. Editable text layers with proprietary Adobe Fonts (replace with open-license fonts or keep an exported high-resolution PNG fallback).
2. Smart Objects and complex layer styles (rasterize or flatten copies if exact visual fidelity matters).
3. CMYK color profiles (convert to sRGB if the files are only for web, or move print masters to Scribus).

Save working copies as `.xcf` once verified in GIMP.

## Step 2: Configure GIMP to feel familiar

Spend ten minutes on initial preferences before doing real work:

1. Ensure Single-Window Mode is enabled under `Windows -> Single-Window Mode`.
2. Set icon theme and dark UI in `Edit -> Preferences -> Interface`.
3. Remap high-frequency shortcuts under `Edit -> Keyboard Shortcuts` (for example, Free Transform, Duplicate Layer, and Export) to match your Photoshop muscle memory.
4. Increase undo memory and tile cache size under `Edit -> Preferences -> System Resources` if you work on large multi-layer canvases.

## Step 3: Fill remaining Creative Cloud gaps with companion OSS tools

Photoshop often gets used for tasks that belong in separate tools:

- RAW photo cataloging and color grading: Darktable
- Vector logos, icons, and SVG assets: Inkscape
- Digital illustration and tablet painting: Krita
- Multi-page print layout with CMYK PDF export: Scribus
