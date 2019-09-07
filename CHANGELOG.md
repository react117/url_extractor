# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.3] - 2019-09-08

### Fixed

- The known issue of the extractor getting into an infinite loop and resulting in duplicate urls in the csv has been fixed with a patch.

### Changed

- Removed known issue from README after it has been fixed with a patch.

## [0.0.2] - 2019-09-04

### Added

- This spider can accept multiple comma-separated links as an argument.
- This spider now can extract the list of URLs from multiple websites at one go.
- Added changelog to maintain the updates.
- Old spider code of [0.0.1] is now deprecated. You can find it [here](https://github.com/react117/url_extractor/blob/master/url_extractor/spiders/__urlextractor_depricated.py).

### Changed

- Updated README now contains general instructions regarding multiple web acceptance at one go.
- README now contains information about the changelog.

## [0.0.1] - 2019-09-03

### Added

- Scrapy Spider which can extract all possible valid URLs from a website given the base-path/domain.
- Support for Link Extractor objects.
- README now contains general instructions regarding this spider and it's usage.

[0.0.3]: https://github.com/react117/url_extractor/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/react117/url_extractor/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/react117/url_extractor/releases/tag/v0.0.1
