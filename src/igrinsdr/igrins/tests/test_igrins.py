import pytest
from igrins_instruments import igrins
import astrodata
import os


test_path = './test_data'

def test_fixIgrinsHeader():
    test_input = 'igrins_header_testdata.fits'
    ad = astrodata.open(os.path.join(test_path, test_input))
    test_tags = set(['IGRINS','FLAT','LAMPOFF'])
    assert test_tags.issubset(ad.tags)
    assert ad.gain() == ad.hdr['GAIN']

