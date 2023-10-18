from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.home() /
    "OneDrive" / 
    "Рабочий стол" /
    "Code" /
    "Python PDF" /
    "newsletter.pdf"
) 

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()
pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_pwd="SuperSecret", owner_pwd="ReallySuperSecret")

with Path("newsletter-protected.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
