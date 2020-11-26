# Author: Randolph Sapp
# Info: Tool to generate transcripts from PDFs

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer

X_RES = 10
Y_RES = 1

class parser:
    def __init__(self, doc):
        parser = PDFParser(doc)
        document = PDFDocument(parser)
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        self.device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        self.interpreter = PDFPageInterpreter(rsrcmgr, self.device)
        self.pages = list(PDFPage.create_pages(document))
        self.characters = []
        self.pdict = {}

    def readPage(self, ipage):
        self.interpreter.process_page(self.pages[ipage])
        layout = self.device.get_result()
        _, _, self.width, self.height = self.pages[ipage].mediabox
        self.parse_obj(layout._objs)
        self.genDict()

    def parse_obj(self, lt_objs):
        for obj in lt_objs:
            if isinstance(obj, pdfminer.layout.LTChar):
                self.characters.append(obj)
            if isinstance(obj, pdfminer.layout.LTAnno):
                self.characters.append(obj)
            # if it's a container, recurse
            elif hasattr(obj, '_objs'):
                self.parse_obj(obj._objs)

    def genDict(self):
        for i, obj in enumerate(self.characters):
            if isinstance(obj, pdfminer.layout.LTChar):
                x1, y1, x2, y2 = obj.bbox
                rowpos = int((y1+y2)/2 * Y_RES)
                colpos = int((x1+x2)/2 * X_RES)
                rdict = self.pdict.get(rowpos, {})
                text = obj.get_text()
                if i < len(self.characters)-1:
                    nextobj = self.characters[i+1]
                    if isinstance(nextobj, pdfminer.layout.LTAnno):
                        text += ' '
                rdict[colpos] = text
                self.pdict[rowpos] = rdict

    def getTextInPercentArea(self, x1, y1, x2, y2):
        output = ""
        for key in sorted(self.pdict.keys()):
            vpercent = 1-(key/self.height)
            if y1 < vpercent < y2:
                rowdict = self.pdict[key]
                for pos in sorted(rowdict.keys()):
                    xpercent = (pos/X_RES)/self.width
                    if x1 < xpercent < x2:
                        output += rowdict[pos]
        return output.strip()

