from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
# from io import StringIO
from io import BytesIO
import os

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = BytesIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # path = 'D:\\OneDrive\\OneDrive - UDESC Universidade do Estado de Santa Catarina\\doutorado\\artigos\\sbse\\ssbse\\SSBSE\\ssbse2009\\Session 3- Software Evolution\\A Study of the Multi-objective Next Release Problem.pdf'
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
    # print text
    return text

paths = 'D:\\OneDrive\\OneDrive - UDESC Universidade do Estado de Santa Catarina\\doutorado\\artigos\\sbse\\ssbse\\SSBSE\\ssbse2009\\Session 3- Software Evolution\\'
results = []
for root, dirs, files in os.walk(paths):

     for file in files:
        # with open(os.path.join(root, file), "r") as auto:

        res = convert_pdf_to_txt(os.path.join(root, file)).decode('unicode-escape')
        title = ''
        authors = []
        abstract = ''
        found_authors = False
        found_abstract = False
        for l in res.split('\n'):
            if not l.__contains__('Symposium on Search Based Software Engineering'):
                # print l
                if title == '':
                    title = l
                elif l != 'Abstract' and not found_authors:
                    authors.append(l)
                elif l != 'Introduction' and not found_abstract:
                    found_authors = True
                    abstract += l
                else:
                    found_abstract = True

        # print 'title: ' + title
        # print 'authors: ' + str(authors)
        # print 'abstract: ' + abstract
        res = [title, authors, abstract]
        results.append(res)

for result in results:
    print '-----'
    for r in result:
        print r
