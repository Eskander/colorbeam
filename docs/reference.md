## Getting started

Copy `colorbeam-template.tex` and edit it, or start from this minimal example:

```latex
\documentclass[aspectratio=169,12pt,t]{beamer}
\usetheme{colorbeam}
\usecolorbeamlibrary{programming}   % optional, comma-separated list

\lecturefooter{Introduction to programming, Session 3}

\begin{document}

\titleslide{COURSE NAME}{Lecture title}{A subtitle}{}{Your Name, University, 2026}

\partslide{1}{mint}{First part}{what we cover}

\begin{frame}[fragile]{A slide}
  \begin{pycode}[title={hello.py}]
print("Bullets, titles and boxes all use the mint of this part.")
  \end{pycode}
\end{frame}

\end{document}
```

Compile with `xelatex` or `lualatex`, and run it twice. The title bar, footer and divider slides are TikZ overlays positioned relative to the page, and TikZ only learns where the page is after the first run.

`\usecolorbeamlibrary` has to come after `\usetheme{colorbeam}`. The libraries stop with a clear error message if the theme is not loaded.

## Customizing

**Main color.** `\setmaincolor{plum}` changes the color of the title slide, the introduction and everything after `\resetpart`. The palette names are `grape`, `sky`, `mint`, `leaf`, `sun`, `clay`, `coral`, `rose`, `plum` and `slate`. You can define your own with `\definecolor` and use it anywhere a palette color is accepted.

**Fonts.** Define the macros before loading the theme:

```latex
\def\colorbeamFont{Source Sans 3}
\def\colorbeamMono{Fira Code}
\usetheme{colorbeam}
```

**Language.** The word in "Part 1" is `\partlabel`. For a French deck, load `polyglossia` with `\setmainlanguage{french}` and add `\renewcommand{\partlabel}{Partie}`.

**Your own library.** A library is just a package called `colorbeamlib-<name>.sty` that is loaded after the theme. Start from `colorbeamlib-programming.sty`: define your `listings` language and style, then wrap them in a `\newtcblisting` that uses `codebox style`. If you write one for another field and want to share it, open a pull request.

## Command reference

### Core

| Command or environment | What it does |
| --- | --- |
| `\titleslide[color]{kicker}{title}{sub 1}{sub 2}{note}` | Full-color title slide |
| `\partslide{n}{color}{title}{subtitle}` | Section divider, sets the color for the slides that follow |
| `\setpart{color}{label}`, `\resetpart` | Change or reset the section color without a divider slide |
| `\setmaincolor{color}` | Re-color the whole deck |
| `\lecturefooter{text}` | Text at the bottom left of every slide |
| `\usecolorbeamlibrary{names}` | Load optional libraries |
| `card`, `tip`, `infobox`, `warnbox`, `okbox`, `darkbox` | Callout boxes |
| `colorcard[opts]{color}` | Callout box in any palette color |
| `\step{color}{n}{width}...\estep` | Numbered step, empty color means section color |
| `\num[color]{n}`, `\pill{color}{text}` | Numbered circle, small label |
| `\numrow{color}{n}{title}{text}` | One-line framed row with a number |
| `\helprow{color}{problem}{fix}` | Two-column row for troubleshooting lists |
| `\questionmark` | Large faded question mark for discussion slides |
| `codebox` | Dark code block, any `listings` language |
| `\codefont{size}{leading}` | Set the code font size, used in `listing options` |
| `flowbox`, `tile`, `stagebox`, `ar` | TikZ styles for boxes and arrows |

### Programming library

| Command or environment | What it does |
| --- | --- |
| `pycode`, `jscode`, `ccode`, `cppcode`, `ino` | Code blocks for Python, JavaScript, C, C++ and Arduino |
| listing styles `py`, `js`, `c`, `cpp`, `ino` | The same styles for use with `codebox` |

### Electronics library

| Command or environment | What it does |
| --- | --- |
| `circuitikz` | CircuiTikZ, European symbols |
| `\ohm` | The ohm sign, for use in math or text |
| `wire`, `board`, `pinc`, `pinl` | TikZ styles for wires, boards, pins and pin labels |

## Known limitations

* The theme is built for 16:9. Other aspect ratios will mostly work, but several helpers use fixed widths in centimeters and were not designed for 4:3.
* Frame titles are drawn in a TikZ overlay, so very long titles are not wrapped. Keep them to one line.
* `\numrow` and `\helprow` have fixed widths and heights. They are meant for short one-line content.
