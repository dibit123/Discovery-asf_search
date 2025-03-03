# Changelog

## [3.0.3](https://github.com/asfadmin/Discovery-asf_search/compare/v3.0.2...v3.0.3)
### Fixed
- Replace `ASFProduct.centroid()` calculation with shapely-based calculation
  - See: https://github.com/asfadmin/Discovery-asf_search/pull/53
  - Removes numpy requirement
  - Adds shapely requirement

## [3.0.2](https://github.com/asfadmin/Discovery-asf_search/compare/v3.0.0...v3.0.2)
### Added
- Feature and Bug Report github issue templates

### Fixed
- Fix download authentication header issue during direct-to-S3 redirects
- Fix Sentinel-1 stacking to include both A and B in stacks

## [3.0.0](https://github.com/asfadmin/Discovery-asf_search/compare/v2.0.2...v3.0.0)
### Added
- Auth support for username/password and cookiejars, in addition to the previously available token-based approach. Create a session, authenticate it with the method of choice, then pass the session to whichever download method is being used.
    - Sessions can be created using the `ASFSession` class, a subclass of `requests.Session`
    - Once a session is created, call one of its authentication methods:
      - `auth_with_creds('user', 'pass)`
      - `auth_with_token(`EDL token`)
      - `auth_with_cookiejar(http.cookiejar)`
    - If you were previously using the `token` argument, such as:
      - `results.download(path='...', token='EDL token')`
    - Updating can be as simple as:
      - `results.download(path='...', session=ASFSession().auth_with_token('EDL token'))`
    - Sessions can be re-used and are thread-safe

### Changed
- `download_url()`, `download_urls()`, `ASFProduct.download()` and `ASFSearchResults.download()` now expect a `session` argument instead of `token`
- Send auth headers to every step along a download redirect chain (including final AWS S3 buckets)

## [2.0.2](https://github.com/asfadmin/Discovery-asf_search/compare/v2.0.1...v2.0.2)
### Added
- INSTRUMENT constants for C-SAR, PALSAR, and ANVIR-2

## [2.0.1](https://github.com/asfadmin/Discovery-asf_search/compare/v2.0.0...v2.0.1)
### Fixed
- Versioning workflow corrected for proper versioning, stop bumping major instead of patch!

## [2.0.0](https://github.com/asfadmin/Discovery-asf_search/compare/v1.1.0...v2.0.0)
### Fixed
- Fixed import order of operations bug
- Updated ASFProduct and ASFSearchResults to use path arg in download methods

## [1.1.0](https://github.com/asfadmin/Discovery-asf_search/compare/v0.4.0...v1.1.0)
### Added
- Parallel downloads now supported by ASFSearchResults. Defaults to 1 (sequential download)
- For `search()`-based functions that take an argument as a list, single values are now also allowed

### Changed
- Import download functionality in asf_search (for `download_url()` and `download_urls()`)
- "parallel" is now "processes" in download functionality

### Fixed
- Fixed ASFProduct import in search.py
- importlib metadata fix for python <3.8

## [0.4.0](https://github.com/asfadmin/Discovery-asf_search/compare/v0.3.0...v0.4.0)
### Added
- ASFSearchResults now has a geojson() method which returns a data structure that matches the geojson specification
- ASFProduct now has a geojson() method that produces a data structure matching a geojson feature snippet
- ASFSearchResults and ASFProduct both have a __str__() methods that serializes the output of their geojson() methods
- Added CodeFactor shield to readme
- Now calculates temporal baselines when building a stack
- New search options: 
    - min/maxDoppler
    - min/MaxFaradayRotation
    - flightLine
    - offNadirAngle
    - season

### Changed
- ASFProduct is no longer a subclass of dict. Instead, metadata has been moved to .properties and .geometry
- ASFSearchResults is now a subclass of UserList, for list-type operations
- Newly-built stacks are sorted by temporal baselines, ascending

### Fixed
- Cleaned up cruft from various refactors


## [0.3.0](https://github.com/asfadmin/Discovery-asf_search/compare/v0.2.4...v0.3.0)

### Added
- Layed out framework for INSTRUMENT constants (needs to be populated)
- Support for baseline stacking of pre-calculated datasets
- Download support for single products or entire search result sets, token-based auth only
- ASFSearchResults and ASFProduct classes
- Lower-level ASFError exception class
- ASFDownloadError exception class
- ASFBaselineError exception class
- Better path/frame/platform/product example


### Changed
- No longer uses range type for parameters that accept lists of values and/or ranges. Now expects a 2-value tuple.
- Removed DATASET constants (not searchable, use platform+instrument to identify a dataset)
- Updated hello_world.py baseline example
- Removed output options across the board, geojson only until we no longer rely on SearchAPI calls
- insarStackID now a search option (needed for baseline stacking of pre-calculated datasets)
- Flatter structure for constants
- baseline functionality moved into search group (file restructuring)

### Fixed
- Corrected handling of version number in user agent string
- unused import cleanup
- better type hinting on centroid() function

## [0.2.4](https://github.com/asfadmin/Discovery-asf_search/compare/v0.0.0...v0.2.4)

### Added
- product_search(): search using a list of Product IDs (CMR's GranuleUR)
- granule_search(): search using a list of Granule names (aka Scene names)
- geo_search(): search using a WKT string, as well as other parameters
- search(): a generic search function, allowing any combination of the above search features
- stack(): provides basic Baseline stacking functionality (does not yet provide perpendicular/temporal baseline values)
- Numerous constants available, covering common BEAMMODE, DATASET, FLIGHT_DIRECTION, PLATFORM, POLARIZATION, and PRODUCT_TYPE values
- Basic exception classes and error handling for search parameter and server errors
- Populated readme with instructions, examples, and badges

### Changed
- Improved packaging/build process
- Restructured branch layout according to https://gist.github.com/digitaljhelms/4287848

### Fixed
- Removed hard-coded version string
- Install setuptools_scm in pypi publish action
