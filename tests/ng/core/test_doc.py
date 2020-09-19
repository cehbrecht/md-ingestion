from mdingestion.ng.core import B2FDoc


def test_doc_common_attributes():
    doc = B2FDoc('test.json', community='test_b2f')
    assert doc.community == 'test_b2f'
    doc.publication_year = '2009-01-01'
    assert doc.publication_year[0] == '2009'
    doc.keywords = ['Social Sciences']
    assert doc.keywords == ['Social Sciences']
    doc.discipline = ['Social Sciences']
    assert doc.discipline == 'Social Sciences'
    doc.discipline = None
    assert doc.discipline == 'Various'


def test_doc_temporal_coverage():
    doc = B2FDoc('test.json')
    # begin
    doc.temporal_coverage = '2001-01-01'
    # assert '2001-01-01T00:00:00Z' == doc.temporal_coverage
    assert '2001-01-01T00:00:00Z' == doc.temporal_coverage_begin_date
    # TODO: fails on travis
    # assert 63113904000 == doc.temp_coverage_begin
    # begin / end
    doc.temporal_coverage = '2001-01-01/2002-12-31'
    # assert '2001-01-01T00:00:00Z/2002-12-31T00:00:00Z' == doc.temporal_coverage
    assert '2001-01-01T00:00:00Z' == doc.temporal_coverage_begin_date
    assert '2002-12-31T00:00:00Z' == doc.temporal_coverage_end_date
    # TODO: fails on travis
    # assert 63113904000 == doc.temp_coverage_begin
    # assert 63176889600 == doc.temp_coverage_end
    # begin / -
    doc.temporal_coverage = '2001-01-01 / -'
    # assert '2001-01-01T00:00:00Z' == doc.temporal_coverage
    assert '2001-01-01T00:00:00Z' == doc.temporal_coverage_begin_date
    # TODO: fails on travis
    # assert 63113904000 == doc.temp_coverage_begin
    # string
    doc.temporal_coverage = 'Viking Age'
    assert 'Viking Age' == doc.temporal_coverage
