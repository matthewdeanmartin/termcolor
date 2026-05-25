# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.3] - 2023-05-29
### Changed
- Add devcontainer, GitHub Actions CI workflow, Makefile, and tox configuration
- Add module-level docstrings and a pylint disable comment to `__main__.py`
- Modernize test suite to use double-quoted string literals throughout

## [1.1.2] - 2021-12-04
### Changed
- Verify wheel build is functional and update build script

## [1.1.1] - 2021-12-04
### Fixed
- Dead link

## [1.1.0] - 2021-12-04
### Added
- Fork of termcolor packaged as `termcolor-whl` with pyproject.toml-based build
- CLI demo module (`__main__.py`) for interactive color testing
- Initial test suite covering `colored`, `cprint`, and the demo function

[1.1.3]: https://github.com/matthewdeanmartin/termcolor/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/matthewdeanmartin/termcolor/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/matthewdeanmartin/termcolor/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/matthewdeanmartin/termcolor/releases/tag/v1.1.0
