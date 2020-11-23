# __________________________
#        PDF Miner
# __________________________

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import sys
import codecs
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


def print_data(pdf_document):
    f = open("Abhinav Singla__SCRAPE1.txt", "a")
    f.write(pdf_document)
    f.close()

pdf_document =convert_pdf_to_txt("E:\\SimplifyCV\\Resume Parser\\PDF Miner\\samples\\AbhinavSingla.pdf")
print(pdf_document)
data = pdf_document.decode('utf-8').encode('uf0b7','replace').decode('uf0b7')
print_data(data)