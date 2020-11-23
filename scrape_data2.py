# __________________________
#          PyPDF2
# __________________________

import PyPDF2

mypdf = open(r'E:\\SimplifyCV\\Resume Parser\\PDF Miner\\samples\\ARUN KUMAR Y.S.pdf', mode='rb')
pdf_document = PyPDF2.PdfFileReader(mypdf)

def print_data(s):
    f = open("Abhinav Singla__SCRAPE2.txt", "a")
    f.write(s)
    f.close()

s=""
for i in range(pdf_document.numPages):
    page_to_print = pdf_document.getPage(i)
    print(page_to_print.extractText())
    s = s + page_to_print.extractText()

print_data(s)

