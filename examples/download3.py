"""
Simple example script demonstrating downloading search results
Requires an EDL token, see: https://urs.earthdata.nasa.gov/user_tokens
"""

import asf_search as asf

if __name__ == '__main__':
    session = asf.get_session_token('EDL token')
    path = '/path/to/project'
    wkt = 'POLYGON((-151.6 61.2,-143.9 61.2,-143.9 63.7,-151.6 63.7,-151.6 61.2))'
    print('Searching...')
    results = asf.geo_search(
        platform=[asf.PLATFORM.SENTINEL1],
        processingLevel=[asf.PRODUCT_TYPE.METADATA_SLC],
        intersectsWith=wkt,
        maxResults=200)
    print('Downloading...')
    results.download(path=path, session=session, processes=10)
    print('Done.')