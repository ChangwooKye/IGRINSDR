import os, sys
import pytest
from igrins_instruments import igrins
import astrodata
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from procedures.badpixel_mask import make_igrins_hotpixel_mask


# Temporary test data path
# TODO : How to set test data path? --> Environmental variable?
test_path = './test_data'

## Test input data
@pytest.fixture
def ad_tag_testdata():
    test_input = 'igrins_header_testdata.fits'
    ad = astrodata.open(os.path.join(test_path, test_input))
    return ad

@pytest.fixture
def ad_hotpixel_testdata():
    test_input = 'igrins_hotpixel_testdata.fits'
    ad = astrodata.open(os.path.join(test_path, test_input))
    return ad

@pytest.fixture
def hotpixel_solution():
    test_input = 'igrins_hotpixel_solution.npy'
    data = np.load(os.path.join(test_path, test_input))
    return data


## Test routines
# Tag reading test
def test_fixIgrinsHeader(ad_tag_testdata):
    test_tags = set(['IGRINS','FLAT','LAMPOFF'])
    assert test_tags.issubset(ad_tag_testdata.tags)
    assert ad_tag_testdata.gain() == ad_tag_testdata.hdr['GAIN']

# Hot-pixel mask procedure test
# TODO : Add dead-pixel mask
def test_makeIgrinsBPM(ad_hotpixel_testdata, hotpixel_solution):
    flat_off = ad_hotpixel_testdata[0].data
    bg_std, hotpixel_mask = make_igrins_hotpixel_mask(flat_off, sigma_clip1 = 100,
                                                      sigma_clip2 = 10, medfilter_size = None)
    hotpixel_arr = hotpixel_mask * 1.
    assert (hotpixel_arr == hotpixel_solution).all()
