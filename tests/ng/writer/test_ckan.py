import os

import pytest

from mdingestion.ng.community import DarusDatacite
from mdingestion.ng.community import Herbadrop
from mdingestion.ng.writer import CKANWriter

from tests.common import TESTDATA_DIR


def test_darus_oai_datacite():
    xmlfile = os.path.join(TESTDATA_DIR, 'darus-oai_datacite', 'SET_1', 'xml', '02baec53-8e79-5611-981e-11df59b824e4.xml')  # noqa
    doc = DarusDatacite(
        xmlfile, url='https://darus.uni-stuttgart.de/oai', community='darus', mdprefix='oai_datacite')
    writer = CKANWriter()
    result = writer.json(doc)
    assert 'Deep enzymology data' in result['title'][0]
    assert '02baec53-8e79-5611-981e-11df59b824e4' == result['name']
    assert 'darus' == result['group']
    assert 'darus' == result['groups'][0]['name']
    assert 'active' == result['state']
    assert '2020-07-01T11:59:59Z' == result['PublicationTimestamp']
    assert 'Deep enzymology data' in result['fulltext']


def test_herbdrop_json():
    jsonfile = os.path.join(TESTDATA_DIR, 'herbadrop-hjson', 'SET_1', 'hjson', '0d9e8478-3d92-5a5f-92cb-eb678e8e48dd.json')  # noqa
    doc = Herbadrop(jsonfile)
    writer = CKANWriter()
    result = writer.json(doc)
    assert 'Gentiana ×marcailhouana Rouy' in result['fulltext']
    assert 'StillImage|PRESERVED_SPECIMEN' in result['fulltext']
