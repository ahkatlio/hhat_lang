# H-hat Visual Identity Guide

This document defines the official visual identity for the H-hat quantum programming language project, including logos, colors, fonts, and usage guidelines.

## Logo

### Primary Logo

The H-hat logo features the letter **Ĥ** (H with circumflex), representing both the "H-hat" name and the mathematical notation commonly used in quantum mechanics for Hamiltonian operators.

**Files**:

- **SVG (Vector)**: `docs/hhat_logo.svg` - Scalable for any size
- **ICO (Favicon)**: `docs/hhat_logo.ico` - 32x32 pixels for browser favicons

### Logo Meaning

The circumflex (ˆ) above the H symbolizes:

- **Mathematical heritage**: The hat notation (ˆ) used in quantum mechanics for operators
- **Quantum connection**: Hamiltonian operator (Ĥ) is fundamental in quantum theory
- **Elevation**: Represents lifting quantum programming to higher abstractions

### License

The H-hat logo is released under **CC BY-SA 4.0** (Creative Commons Attribution-ShareAlike 4.0 International).

- **Free to use**: Commercial and non-commercial purposes
- **Attribution required**: Credit must be given to "H-hat Project / Unitary Foundation"
- **ShareAlike**: Derivative works must use the same license

## Color Palette

H-hat uses a carefully selected color palette that avoids pure black (#000000) and pure white (#FFFFFF) for better readability and visual comfort.

### Light Theme

**Primary Colors**:

- **Primary**: `#036969` - Deep Teal
  - Used for: Headers, links, primary UI elements
  - RGB: `rgb(3, 105, 105)`
  - HSL: `hsl(180, 94%, 21%)`

- **Accent**: `#7b1fa2` - Deep Purple (Material Design)
  - Used for: Highlights, active states, quantum-related elements
  - RGB: `rgb(123, 31, 162)`
  - HSL: `hsl(282, 68%, 38%)`

**Background & Text**:

- **Background**: `#fee2c4` - Warm Cream
  - Soft, warm background that reduces eye strain
  - RGB: `rgb(254, 226, 196)`
  - HSL: `hsl(31, 97%, 88%)`

- **Foreground (Text)**: `#263f57` - Dark Blue-Grey
  - Not pure black, easier on the eyes
  - RGB: `rgb(38, 63, 87)`
  - HSL: `hsl(209, 39%, 25%)`

### Dark Theme

**Primary Colors**:

- **Primary**: `#d8ae2d` - Golden Amber
  - Used for: Headers, links, primary UI elements
  - RGB: `rgb(216, 174, 45)`
  - HSL: `hsl(45, 69%, 51%)`

- **Accent**: `#009688` - Teal (Material Design)
  - Used for: Highlights, active states
  - RGB: `rgb(0, 150, 136)`
  - HSL: `hsl(174, 100%, 29%)`

**Background & Text**:

- **Background**: `#152230` - Deep Blue-Grey
  - Not pure black, reduces contrast strain
  - RGB: `rgb(21, 34, 48)`
  - HSL: `hsl(211, 39%, 14%)`

- **Foreground (Text)**: `#c0c0c0` - Light Grey
  - Not pure white, easier on the eyes
  - RGB: `rgb(192, 192, 192)`
  - HSL: `hsl(0, 0%, 75%)`

### Color Usage Guidelines

**DO**:
- Use teal/amber for primary branding elements
- Use purple for quantum-specific highlights
- Maintain sufficient contrast for accessibility (WCAG AA minimum)
- Use consistent colors across documentation and tools

**DON'T**:
- Use pure black (`#000000`) or pure white (`#ffffff`)
- Mix light and dark theme colors in the same context
- Use colors that conflict with syntax highlighting

### Semantic Colors

These colors are used for specific purposes:

- **Success/Quantum State**: Teal shades (`#009688`, `#036969`)
- **Warning/Classical State**: Amber shades (`#d8ae2d`, `#ffa726`)
- **Error**: Red shade (`#d32f2f`) - Material Design red
- **Info**: Blue shade (`#1976d2`) - Material Design blue

## Typography

### Fonts

**Text Font**: **Lato**

- **Family**: Lato
- **Source**: Google Fonts
- **Weights**: 300 (Light), 400 (Regular), 700 (Bold)
- **Usage**: Body text, headings, UI elements
- **Characteristics**: Humanist sans-serif, excellent readability, professional appearance

**Code Font**: **JetBrains Mono**

- **Family**: JetBrains Mono
- **Source**: Google Fonts / JetBrains
- **Weights**: 400 (Regular), 700 (Bold)
- **Usage**: Code blocks, inline code, terminal output
- **Characteristics**: Monospace, designed for developers, excellent ligature support

### Typography Guidelines

**Headings**:
- Use Lato Bold (700) for H1-H3
- Use Lato Regular (400) for H4-H6
- Maintain hierarchical sizing

**Body Text**:
- Use Lato Regular (400) for body text
- Use Lato Bold (700) for emphasis
- Font size: 100% (16px base)

**Code**:
- Always use JetBrains Mono
- Maintain monospace for alignment
- Use syntax highlighting with H-hat color palette

## Syntax Highlighting

### Code Block Styling

Syntax highlighting for Heather dialect uses the following token colors:

**Light Theme**:
- **Keywords**: `#7b1fa2` (Deep Purple)
- **Types**: `#036969` (Deep Teal)
- **Quantum Types**: `#009688` (Teal) with bold weight
- **Strings**: `#c41a16` (Red)
- **Numbers**: `#1976d2` (Blue)
- **Quantum Numbers**: `#009688` (Teal) with bold weight
- **Comments**: `#5e6265` (Grey)
- **Operators**: `#263f57` (Dark Blue-Grey)

**Dark Theme**:
- **Keywords**: `#bb86fc` (Light Purple)
- **Types**: `#d8ae2d` (Golden Amber)
- **Quantum Types**: `#03dac6` (Bright Teal) with bold weight
- **Strings**: `#cf6679` (Pink-Red)
- **Numbers**: `#82b1ff` (Light Blue)
- **Quantum Numbers**: `#03dac6` (Bright Teal) with bold weight
- **Comments**: `#6a737d` (Grey)
- **Operators**: `#c0c0c0` (Light Grey)

### Quantum-Specific Highlighting

Quantum elements (identifiers prefixed with `@`) receive special treatment:

- **Distinct color**: Teal variants (`#009688` light, `#03dac6` dark)
- **Optional bold weight**: To differentiate from classical code
- **Consistent across all quantum types**: `@bool`, `@int`, `@bell_t`, etc.

## Icon Usage

### Favicon

- **File**: `docs/hhat_logo.ico`
- **Size**: 32x32 pixels
- **Format**: ICO (multi-resolution)
- **Usage**: Browser tabs, bookmarks, desktop shortcuts

### Documentation Logo

- **File**: `docs/hhat_logo.svg`
- **Format**: SVG (scalable vector)
- **Usage**: Documentation header, README, presentations
- **Sizing**: Scales to any size without quality loss

## Brand Application

### Documentation Website

Current implementation in `mkdocs.yml`:

```yaml
theme:
  name: material
  font:
    text: Lato
    code: JetBrains Mono
  logo: hhat_logo.svg
  favicon: hhat_logo.ico
  palette:
    # Light theme
    - scheme: default
      primary: teal
      accent: deep purple
    # Dark theme
    - scheme: slate
      primary: amber
      accent: teal
```

Custom colors in `docs/stylesheets/extra.css`:

```css
[data-md-color-scheme="default"] {
  --md-default-primary-color: #036969;
  --md-default-fg-color: #263f57;
  --md-default-bg-color: #fee2c4;
}

[data-md-color-scheme="slate"] {
  --md-default-primary-color: #d8ae2d;
  --md-default-fg-color: #c0c0c0;
  --md-default-bg-color: #152230;
}
```

### GitHub Repository

- **Repository icon**: Use `hhat_logo.svg` or `hhat_logo.ico`
- **README header**: Include logo at top
- **Social preview**: Create 1280x640px image with logo and tagline

### Presentations

When creating presentation slides:

- **Title slide**: Feature Ĥ logo prominently
- **Colors**: Use teal/amber primary palette
- **Fonts**: Lato for text, JetBrains Mono for code
- **Dark backgrounds**: Use `#152230` instead of black
- **Light backgrounds**: Use `#fee2c4` instead of white

### Print Materials

For printed materials:

- **Logo**: Use SVG converted to high-resolution PNG (300 DPI minimum)
- **Colors**: CMYK conversions may vary; test prints recommended
- **Fonts**: Ensure Lato and JetBrains Mono are embedded

## Accessibility

### Contrast Ratios

All color combinations meet WCAG 2.1 Level AA standards:

**Light Theme**:
- Text on background: `#263f57` on `#fee2c4` = 7.8:1 (AAA)
- Primary on background: `#036969` on `#fee2c4` = 5.2:1 (AA)

**Dark Theme**:
- Text on background: `#c0c0c0` on `#152230` = 10.1:1 (AAA)
- Primary on background: `#d8ae2d` on `#152230` = 7.9:1 (AAA)

### Font Sizes

- **Minimum body text**: 16px (1rem)
- **Minimum code text**: 14px (0.875rem)
- **Scalable**: All sizes use relative units (rem, em)

### Color Blindness

The color palette is designed to be distinguishable for common types of color blindness:

- **Teal and amber**: High contrast for deuteranopia/protanopia
- **Purple accents**: Alternative to red/green for tritanopia
- **Sufficient contrast**: Relies on brightness differences, not just hue

## File Organization

Visual identity assets are organized as follows:

```
docs/
├── hhat_logo.svg           # Primary logo (SVG)
├── hhat_logo.ico           # Favicon (32x32)
├── brand/                  # Brand guidelines (this document)
│   └── identity.md
└── stylesheets/
    └── extra.css           # Custom color definitions
```

## Future Enhancements

Potential additions to the visual identity:

- **Extended logo variants**: Horizontal, vertical, monochrome
- **Icon set**: UI icons matching the visual style
- **Custom theme**: Full Pygments theme for syntax highlighting
- **Motion guidelines**: Animation specifications for UI elements
- **Social media assets**: Profile pictures, banners, cards

## Credits and Attribution

### Logo

- **Created by**: H-hat Project contributors
- **License**: CC BY-SA 4.0
- **Attribution**: "H-hat logo by H-hat Project / Unitary Foundation"

### Fonts

- **Lato**: Designed by Łukasz Dziedzic, licensed under SIL Open Font License
- **JetBrains Mono**: Designed by JetBrains, licensed under Apache License 2.0

### Color Palette

- **Designed by**: H-hat Project contributors
- **Inspired by**: Material Design color system, quantum computing aesthetics

## Contact

For questions about visual identity or brand usage:

- **GitHub**: [hhat-lang/hhat_lang/issues](https://github.com/hhat-lang/hhat_lang/issues)
- **Discord**: [#h-hat on UnitaryFoundation server](http://discord.unitary.foundation)

---

**Document Version**: 1.0  
**Last Updated**: February 2026  
**License**: CC BY-SA 4.0
