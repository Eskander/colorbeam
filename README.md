# Colorbeam

A Modern, Colorful Beamer theme for university lectures and lab sessions. It started as the slide style for my own embedded systems course, where I needed something that handles circuit diagrams, code listings and a lot of step-by-step instructions, but more importantly, didn't look from the _90s_.

[![CI](https://github.com/Eskander/colorbeam/actions/workflows/ci.yaml/badge.svg?event=push)](https://github.com/Eskander/colorbeam/actions/workflows/ci.yaml)
[![CD](https://github.com/Eskander/colorbeam/actions/workflows/cd.yaml/badge.svg?event=push)](https://github.com/Eskander/colorbeam/actions/workflows/cd.yaml)

---

The idea is simple: each part of a lecture gets its own color, and everything on the slides (title bar, bullets, boxes, code frames) follows it.

<p align="center">
  <img src="assets/images/title.png" alt="Title slide" width="50%">
</p>

The theme is split in two layers. The core is subject-neutral and is all you need for most lectures. On top of it there are optional libraries for specific fields, currently `programming` and `electronics`. You load only the ones you use, so a history or chemistry lecture does not need CircuiTikZ installed.

## Install

The theme needs XeLaTeX or LuaLaTeX. Each [release](https://github.com/Eskander/colorbeam/releases/latest) ships Linux packages (`.deb`, `.rpm` and `.pkg.tar.zst`), or you can copy the `.sty` files next to your `.tex` file. [Install and get started](docs/install.md) covers requirements, fonts and a minimal example, and the [reference](docs/reference.md) lists every command.


## What you get

### Core

**Sections with a color of their own.** `\partslide{2}{sky}{Tables and structure}{tables, pipelines and tiles}` draws a full-bleed divider and switches every following slide to that color until the next one. There are ten colors in the palette, picked to stay readable when projected in a bright room (so nothing too neon).

<p align="center" >
  <img src="assets/images/part.png" alt="Part divider" width="49%">
  <img src="assets/images/sections.png" alt="Section colors" width="49%">
</p>

<p align="center">
  <img src="assets/images/palette.png" alt="The palette" width="49%">
  <img src="assets/images/title-colors.png" alt="Title slide in four main colors" width="49%">
</p>

`\setmaincolor{plum}` re-colors the title slide, the introduction and everything after `\resetpart` with one line.

**Callout boxes.** `card`, `tip`, `infobox`, `warnbox`, `okbox`, `darkbox`, and `colorcard` if you want any palette color.

<p align="center">
  <img src="assets/images/callouts.png" alt="Callout boxes" width="49%">
  <img src="assets/images/colorcards.png" alt="Colorcards" width="49%">
</p>

**Steps, rows and pills.** Numbered steps (`\step`), small colored labels (`\pill`), one-line framed rows (`\numrow`, `\helprow`), and a big faded question mark for discussion slides (`\questionmark`).

<p align="center">
  <img src="assets/images/steps.png" alt="Steps and pills" width="49%">
  <img src="assets/images/rows.png" alt="Rows" width="49%">
</p>

<p align="center">
  <img src="assets/images/outline.png" alt="Outline" width="49%">
  <img src="assets/images/question.png" alt="Question" width="49%">
</p>

**Tables and layout.** Tables follow the section color, and a few TikZ styles (`flowbox`, `tile`, `stagebox`, `ar`) cover boxes-and-arrows diagrams.

<p align="center">
  <img src="assets/images/table.png" alt="Table" width="49%">
  <img src="assets/images/summary.png" alt="Summary" width="49%">
</p>

<p align="center">
  <img src="assets/images/pipeline.png" alt="Pipeline" width="49%">
  <img src="assets/images/tiles.png" alt="Tiles" width="49%">
</p>

**Formulas and plots.** TikZ and pgfplots are loaded and set up with the theme colors.

<p align="center">
  <img src="assets/images/flowbox.png" alt="Flowbox" width="49%">
  <img src="assets/images/plot.png" alt="Plot" width="49%">
</p>

<p align="center">
  <img src="assets/images/bars.png" alt="Bar chart" width="49%">
  <img src="assets/images/codebox.png" alt="Codebox" width="49%">
</p>

`codebox` is a generic dark code block for any language known to `listings`.

### Library: programming

Load it with `\usecolorbeamlibrary{programming}`. It adds highlighting styles tuned for the palette and a code block environment for each language:

| Environment | Language |
| --- | --- |
| `pycode` | Python |
| `jscode` | JavaScript |
| `ccode` | C |
| `cppcode` | C++ |
| `ino` | Arduino (C++ with the Arduino API highlighted) |

Each one takes the same options as `codebox`, for example `\begin{pycode}[title={main.py}]`. Accented letters in comments and strings work, which matters if you teach in French or Spanish. Frames that contain code must be marked `[fragile]`.

<p align="center">
  <img src="assets/images/programming.png" alt="Programming library" width="49%">
  <img src="assets/images/c-cpp.png" alt="C and C++" width="49%">
</p>

<p align="center">
  <img src="assets/images/arduino.png" alt="Arduino" width="49%">
</p>

### Library: electronics

Load it with `\usecolorbeamlibrary{electronics}`. It loads CircuiTikZ in its European style, defines `\ohm`, and adds TikZ styles for wiring diagrams: `wire`, `board` (a dark module such as an ESP32 or an Arduino), `pinc` (a pin) and `pinl` (a pin label). The styles also work in plain TikZ pictures.

<p align="center">
  <img src="assets/images/electronics.png" alt="Electronics library" width="49%">
  <img src="assets/images/wiring.png" alt="Wiring diagram" width="49%">
</p>

<p align="center">
  <img src="assets/images/rc.png" alt="RC circuit" width="49%">
</p>

`colorbeam-template.tex` is a short lecture in five parts, one palette color each, and it uses everything above, so it doubles as the reference. It loads both libraries, so delete the ones you do not need.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to report problems and add libraries.
