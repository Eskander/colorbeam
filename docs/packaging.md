# Packaging

Recipes for the Linux packages published with each release.

| Format | Recipe | Target |
| --- | --- | --- |
| `.deb` | `debian/` | Debian, Ubuntu |
| `.rpm` | `rpm/colorbeam.spec` | Fedora and other RPM distributions that use the Fedora TeX Live and font names |
| `.pkg.tar.zst` | `arch/PKGBUILD` | Arch Linux |

All three install the theme into `/usr/share/texmf/tex/latex/colorbeam/`, which is on the default TeX search path of these distributions, and depend on XeLaTeX, the TeX packages the theme loads, Carlito and JetBrains Mono.

The file layout is defined once, in `Makefile`. Each recipe calls it, so a change to what gets installed is a one-place edit.

## Building locally

From a clean checkout:

```bash
V=1.2   # the version to build
git archive --format=tar.gz --prefix="colorbeam-$V/" -o "colorbeam-$V.tar.gz" HEAD
```

Debian, with `debhelper` installed:

```bash
tar xzf "colorbeam-$V.tar.gz" && cd "colorbeam-$V"
cp -r packaging/debian debian
sed -e "s/@VERSION@/$V/g" -e "s/@DATE@/$(date -R)/" debian/changelog.in > debian/changelog
rm debian/changelog.in
dpkg-buildpackage -b -us -uc
```

Fedora, with `rpm-build` installed:

```bash
mkdir -p ~/rpmbuild/SOURCES && cp "colorbeam-$V.tar.gz" ~/rpmbuild/SOURCES/
sed "s/^Version:.*/Version:        $V/" packaging/rpm/colorbeam.spec > colorbeam.spec
rpmbuild -bb colorbeam.spec
```

Arch Linux:

```bash
mkdir build && cp "colorbeam-$V.tar.gz" build/
sed "s/^pkgver=.*/pkgver=$V/" packaging/arch/PKGBUILD > build/PKGBUILD
cd build && makepkg -s
```
