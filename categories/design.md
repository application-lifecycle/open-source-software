# Open source design and graphics software

Open-source creative tools cover raster editing, SVG vector design, digital painting, RAW photography, print layout, and browser-based UI prototyping without recurring creative suite subscriptions.

[Back to main catalog](../README.md)

## Comparison table

<!-- START:CATEGORY_TABLE -->
| Software | Alternative to | Platform | License | Stars | Last release | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [GIMP](https://www.gimp.org/) | Adobe Photoshop | Win, Mac, Linux | GPL-3.0 | - | - | Active | Medium | Raster photo editing and image manipulation |
| [Inkscape](https://inkscape.org/) | Adobe Illustrator | Win, Mac, Linux | GPL-2.0 | - | - | Active | Low | SVG vector illustration and logo design |
| [Krita](https://krita.org/) | Corel Painter, Clip Studio Paint | Win, Mac, Linux, Android | GPL-3.0 | 10.8k | 2026-11-25 | Active | Low | Digital painting, concept art, and 2D animation |
| [Penpot](https://penpot.app/) | Figma | Web | MPL-2.0 | 62.7k | 2026-11-24 | Active | Medium | Collaborative UI/UX design with native CSS Grid and Flexbox |
| [Darktable](https://www.darktable.org/) | Adobe Lightroom | Win, Mac, Linux | GPL-3.0 | 13.5k | 2026-10-04 | Active | Medium | Non-destructive RAW photography workflow |
| [Scribus](https://www.scribus.net/) | Adobe InDesign | Win, Mac, Linux | GPL-2.0 | 659 | 2026-11-23 | Active | High | Print page layout, CMYK brochures, and PDF publishing |
| [RawTherapee](https://www.rawtherapee.com/) | Adobe Camera Raw | Win, Mac, Linux | GPL-3.0 | 4.3k | 2026-07-26 | Active | Medium | Detailed RAW color grading and lens correction |
| [Excalidraw](https://excalidraw.com/) | Miro, Lucidchart | Web | MIT * | 136.3k | 2026-04-21 | Active | Low | Hand-drawn style architecture diagrams and whiteboarding |
<!-- END:CATEGORY_TABLE -->

## Workflow notes

- Penpot runs in the browser, exports standard SVG, and models layouts with native CSS Flexbox and Grid, which reduces handoff friction with frontend engineers.
- Use Darktable or RawTherapee for non-destructive RAW catalog processing, then hand finished exports to GIMP for retouching or compositing.
- Inkscape handles clean SVG vector art and logos, while Krita provides brush engines and tablet pressure support suited to illustration and comics.
- Scribus supports CMYK color separation and PDF/X export for print shops, though teams coming from InDesign should expect a steeper learning curve.

## Related migration guide

- [Migrating from Adobe Photoshop to GIMP](../migration-guides/photoshop-to-gimp.md)
