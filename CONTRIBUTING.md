# Contributing

Issues and pull requests are welcome. If you report a layout problem, a screenshot and the smallest `.tex` file that shows it will save us both time.

## Adding a library

A library is just a package called `colorbeamlib-<name>.sty` that is loaded after the theme. Start from `colorbeamlib-programming.sty`: define your `listings` language and style, then wrap them in a `\newtcblisting` that uses `codebox style`. If you write one for another field and want to share it, open a pull request.

## Before you open a pull request

CI compiles `colorbeam-template.tex` with XeLaTeX, twice, on every pull request, so check that it still compiles after your change. If you touch the packaging, see [`packaging/`](packaging/).
