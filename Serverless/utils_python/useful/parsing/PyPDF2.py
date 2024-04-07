
from PyPDF2 import PdfReader

pdf_reader = PdfReader("sample.pdf")
print(pdf_reader.numPages)
# pdf_reader.getPage(0)

for page in pdf_reader.pages:
    print(page.extract.text())
    



