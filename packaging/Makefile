# Shared install logic for the deb, rpm and Arch recipes.
#
# Every recipe calls this Makefile, so the file layout is defined once:
#
#   make -f packaging/Makefile install DESTDIR=/some/root
#
# Targets:
#   install          the .sty files, into the system texmf tree
#   install-doc      README, DOCS and the template, into the doc directory
#   install-license  the LICENSE file, into the licenses directory
#
# /usr/share/texmf is on the default TeX search path of Debian, Fedora and Arch.

SRCDIR     := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))..)
prefix     ?= /usr
datadir    ?= $(prefix)/share
TEXMFDIR   ?= $(datadir)/texmf
DOCDIR     ?= $(datadir)/doc/colorbeam
LICENSEDIR ?= $(datadir)/licenses/colorbeam

STYDIR := $(DESTDIR)$(TEXMFDIR)/tex/latex/colorbeam

.PHONY: install install-doc install-license

install:
	install -d $(STYDIR)
	install -m 644 $(SRCDIR)/beamerthemecolorbeam.sty $(SRCDIR)/colorbeamlib-*.sty $(STYDIR)/

install-doc:
	install -d $(DESTDIR)$(DOCDIR)
	install -m 644 $(SRCDIR)/README.md $(SRCDIR)/docs/reference.md \
		$(SRCDIR)/colorbeam-template.tex \
		$(DESTDIR)$(DOCDIR)/

install-license:
	install -d $(DESTDIR)$(LICENSEDIR)
	install -m 644 $(SRCDIR)/LICENSE $(DESTDIR)$(LICENSEDIR)/
