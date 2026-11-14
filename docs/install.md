# Install and get started

## Requirements

* XeLaTeX or LuaLaTeX. The theme needs `fontspec`, so plain pdfLaTeX will not work.
* The default fonts are Carlito (sans) and JetBrains Mono (monospace). Both are free and open source, and most Linux distributions package them (see below). You can use others.
* Core packages: `fontspec`, `etoolbox`, `tikz`, `pgfplots`, `tcolorbox`, `listings`, `colortbl`, `array`.
* The electronics library also needs `circuitikz`.

All of the TeX packages are part of a full TeX Live or MiKTeX install. The fonts are not, so install them separately (on Debian and Ubuntu: `fonts-jetbrains-mono` and `fonts-crosextra-carlito`).

## Installing

### From a package (Linux)

Each [release](https://github.com/Eskander/colorbeam/releases/latest) ships a `.deb`, an `.rpm` and a `.pkg.tar.zst`. They install the theme into `/usr/share/texmf/tex/latex/colorbeam/` and pull in the required TeX packages and fonts.

```bash
sudo apt install ./colorbeam_*_all.deb          # Debian, Ubuntu
sudo dnf install ./colorbeam-*.noarch.rpm       # Fedora
sudo pacman -U colorbeam-*.pkg.tar.zst          # Arch Linux
```

The packaging recipes live in [`packaging/`](../packaging/).

### Manually

Put `beamerthemecolorbeam.sty` and the library files you want (`colorbeamlib-programming.sty`, `colorbeamlib-electronics.sty`) next to your `.tex` file. To make them available everywhere, copy them into your local texmf tree, for example `~/texmf/tex/latex/colorbeam/` on Linux and macOS, then run `texhash` if your distribution needs it.

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

Next, the [reference](reference.md) lists every command and option.
