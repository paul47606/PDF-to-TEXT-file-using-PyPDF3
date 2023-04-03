import PyPDF2
from PyPDF2 import PdfReader

# give the path of the particular file
a = PdfReader("")

# to find the total number of pages in the given PDF
number_of_pages = len(a.pages)
print(number_of_pages)
# PDF info
print(a.metadata)

# get the PDF data to text output.. and you must give the range of pages
b = a.pages[0-5]
c = b.extract_text()
print(" look: ", c)

# for pasting the output data on to a text file, instead of pl.txt u can give your own name
with open("pl.txt", 'wt') as f:
    print(f"See {c}", file=f)

