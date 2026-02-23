#！/bin/bash
ls -R
MDBOOK_VERSION="0.5.2"
curl -sSL https://github.com/rust-lang/mdBook/releases/download/v$MDBOOK_VERSION/mdbook-v$MDBOOK_VERSION-x86_64-unknown-linux-gnu.tar.gz | tar -xz
./mdbook build
