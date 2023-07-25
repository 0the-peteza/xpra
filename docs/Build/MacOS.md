# ![MacOS](../images/icons/osx.png) Building MacOS Binaries

## Setup
Install [XCode](https://developer.apple.com/xcode/) and its command line tools.

<details>
  <summary>Workaround curl certificate issue</summary>

This step is optional and only needed if curl fails to validate SSL connections.
```shell
curl -k -sSL http://curl.haxx.se/ca/cacert.pem >> cacert.pem
export CURL_CA_BUNDLE=`pwd`/cacert.pem
export SSL_CERT_FILE=`pwd`/cacert.pem
```
On some older versions of MacOS, you may also need:
```shell
git config --global http.sslverify "false"
```
At least initially.
</details>

<details>
  <summary>Setup gtk-osx</summary>

Download the latest version of the [gtk-osx](https://wiki.gnome.org/Projects/GTK/OSX/Building) setup script and run it:
```shell
curl -o ~/gtk-osx-setup.sh \
     https://raw.githubusercontent.com/Xpra-org/gtk-osx-build/master/gtk-osx-setup.sh
sh gtk-osx-setup.sh
```
This will have installed `jhbuild` in `~/.new_local/bin`, so let's add this to our `$PATH`:
```shell
export PATH=$PATH:~/.new_local/bin/
```
</details>
<details>
  <summary>Configure `jhbuild` to use our modules</summary>

```shell
curl -o ~/.config/jhbuildrc-custom \
     https://raw.githubusercontent.com/Xpra-org/gtk-osx-build/master/jhbuildrc-custom-xpra
```
</details>

Bootstrap:
```shell
jhbuild bootstrap
jhbuild update
jhbuild bootstrap-gtk-osx
```

Optional: install [pandoc](https://pandoc.org/installing.html#macos)

## Build all the libraries
```shell
jhbuild build
#some python libraries have to be installed via pip in a jhbuild shell:
jhbuild shell
pip3 install --prefix $JHBUILD_PREFIX packaging
pip3 install --prefix $JHBUILD_PREFIX parsing
pip3 install --prefix $JHBUILD_PREFIX typing_extensions
```
(building from the 3.1.x branch also requires `lz4` and `numpy`)

## Build and Package Xpra
```shell
git clone https://github.com/Xpra-org/xpra
cd xpra/packaging/MacOS/
sh ./make-app.sh
sh ./make-DMG.sh
```
Signing the resulting `.app`, `DMG` and `PKG` images requires setting up certificates.
