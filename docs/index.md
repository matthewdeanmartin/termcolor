# termcolor-whl

`termcolor-whl` is a wheel-packaged fork of `termcolor` for adding ANSI color to Python console output. It provides two functions: `colored()` returns a string, while `cprint()` prints it.

Use [Installation](installation.md) to add the package, then [Usage](usage.md) for colors, highlights, attributes, and the built-in demo. The historical [changes](CHANGES.MD) and [source repository](https://github.com/matthewdeanmartin/termcolor) are also available.

This fork does not handle nested color tokens. The colors and attributes a user sees depend on their terminal's ANSI support.
