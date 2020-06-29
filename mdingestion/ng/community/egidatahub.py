from ..reader import DublinCoreReader


class EGIDatahubDublinCore(DublinCoreReader):
    def update(self, doc):
        doc.publisher = ['EGI Datahub']
        doc.doi = self.doi(doc)

    def doi(self, doc):
        dois = [id for id in self.parser.find('identifier') if id.startswith('http://hdl.handle.net')]
        if dois:
            url = dois[0]
        else:
            url = ''
        return url
