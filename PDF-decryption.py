from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.home() /
    "OneDrive" / 
    "Рабочий стол" /
    "Code" /
    "Python PDF" /
    "newsletter-protected.pdf"
) 
pdf_reader = PdfFileReader(str(pdf_path))
# print(pdf_reader.getPage(0))
print(pdf_reader.decrypt(password="SuperSecret"))
print(pdf_reader.getPage(0))

# Review Exercises
# 1. 

pdf_path = Path("top_secret.pdf")
pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()
pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_pwd="Unguessable")
with Path("top_secret_encrypted.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# 2. 

pdf_path = Path("top_secret_encrypted.pdf")
pdf_reader = PdfFileReader(str(pdf_path))
pdf_reader.decrypt(password="Unguessable")
first_page = pdf_reader.getPage(0)
print(first_page.extractText())