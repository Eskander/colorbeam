Name:           colorbeam
Version:        0
Release:        1%{?dist}
Summary:        Beamer theme for university lectures and lab sessions
License:        LPPL-1.3c
URL:            https://github.com/Eskander/colorbeam
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make

Requires:       texlive-xetex
Requires:       texlive-beamer
Requires:       texlive-fontspec
Requires:       texlive-etoolbox
Requires:       texlive-pgf
Requires:       texlive-pgfplots
Requires:       texlive-tcolorbox
Requires:       texlive-listings
Requires:       texlive-colortbl
Requires:       texlive-circuitikz
Requires:       texlive-polyglossia
Requires:       font(carlito)
Requires:       font(jetbrainsmono)

%description
Colorbeam is a Beamer theme with a multi-color section system, callout
boxes, code blocks, numbered steps and TikZ helpers. Optional libraries
add support for programming and electronics lectures.

%prep
%autosetup

%build
# Nothing to build.

%install
make -f packaging/Makefile install \
    DESTDIR=%{buildroot} TEXMFDIR=%{_datadir}/texmf

%post
mktexlsr %{_datadir}/texmf >/dev/null 2>&1 || :

%postun
mktexlsr %{_datadir}/texmf >/dev/null 2>&1 || :

%files
%license LICENSE
%doc README.md docs/DOCS.md colorbeam-template.tex
%{_datadir}/texmf/tex/latex/colorbeam/

%changelog
* Fri Nov 13 2026 Eskander Bejaoui <mail@eskander.tn> - 1.2-1
- Package the colorbeam theme
