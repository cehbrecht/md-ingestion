from ..reader import DublinCoreReader
from ..sniffer import OAISniffer


class SLKSDublinCore(DublinCoreReader):
    NAME = 'slks-oai_dc'
    SNIFFER = OAISniffer

    def update(self, doc):
        # doc.open_access = True
        record_id = self.find('header.identifier')[0]
        # print(record_id)
        record_id = record_id.split('/')
        # print(record_id)
        record_id = record_id[-2]
        # print(record_id)
        oai_id = f'urn:repox.www.kulturarv.dkSites:http://www.kulturarv.dk/fundogfortidsminder/site/{record_id}'
        # print(oai_id)
        doc.metadata_access = f'http://www.kulturarv.dk/ffrepox/OAIHandler?verb=GetRecord&metadataPrefix=ff&identifier={oai_id}'
        doc.discipline = 'Archaeology'
        doc.publication_year = self.find('header.datestamp')
        doc.description = 'This record describes ancient sites and monuments as well as archaeological excavations undertaken by Danish museums.'
        doc.publisher = 'Slots- og Kulturstyrelsen'
        doc.rights = 'For scientific use'
        doc.contact = 'post@slks.dk'
        # doc.language = 'Danish'
        keywords = doc.keywords
        keywords.append('EOSC Nordic')
        keywords.append('Viking Age')
        doc.temporal_coverage = self.temporal_coverage(doc)

    def temporal_coverage(self, doc):
        temporal = self.find('temporal')
        period = temporal[0]
        year = temporal[1]
        from_year = int(year.split(',')[0])
        doc.temporal_coverage_begin_date = f"{from_year}"
        if from_year < 0:
            from_year = f"{abs(from_year)} BC"
        else:
            from_year = f"{from_year} AD"
        to_year = int(year.split(',')[1])
        doc.temporal_coverage_end_date = f"{to_year}"
        if to_year < 0:
            to_year = f"{abs(to_year)} BC"
        else:
            to_year = f"{to_year} AD"
        if len(temporal) >= 3:
            main_period = temporal[2]
            coverage = f"{from_year} - {to_year}; {period}; {main_period}"
        else:
            coverage = f"{from_year} - {to_year}; {period}"
        return coverage