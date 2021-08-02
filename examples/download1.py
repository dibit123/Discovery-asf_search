"""
Simple example script demonstrating product download across various datasets in parallel
Expects EDL username and password as command line args
"""

import sys
import asf_search as asf


if __name__ == '__main__':
    results = asf.product_search([
        'S1B_IW_SLC__1SDV_20210416T101049_20210416T101110_026490_0329A8_B8B5-METADATA_SLC',     # Sentinel-1
        'ALPSRP279071390-KMZ',                                                                 # ALOS PALSAR
        'ALPSRP279121600-L2.2',                                                                 # ALOS PALSAR L2.2
        'ALAV2A279162300',                                                                      # ALOS AVNIR
        'SIRC2_16_SLC_ALL_175_040_036_19941011T045929_19941011T045941-METADATA',                # SIR-C
        #'S1-GUNW-D-R-115-tops-20210708_20200701-141630-38575N_36603N-PP-07a6-v2_0_4',          # GRFN
        'SP_33149_D_007-L1A_Radar_RO_ISO_XML',                                                 # SMAP
        'UA_atchaf_06309_21024_020_210401_L090_CX_01-METADATA',                                # UAVSAR
        'R1_65205_ST6_F143-L1',                                                                # RADARSAT-1
        'E2_84699_STD_F309-L1',                                                                # ERS-2
        'J1_36439_STD_F268-L1',                                                                # JERS-1
        'ts1884-LTIF',                                                                         # AIRSAR
        'SS_01502_STD_F2394-GEOTIFF'                                                           # SEASAT
    ])
    results.download(
        path='/path/to/project',
        session=asf.ASFSession().auth_with_creds(sys.argv[1], sys.argv[2]),
        processes=4
    )
