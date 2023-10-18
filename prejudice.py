from PyPDF2 import PdfFileReader

from pathlib import Path
pdf_path = (
    Path.home() /
    'OneDrive' /
    'Рабочий стол' /
    'Code' /
    'Python PDF' /
    'Pride_and_Prejudice.pdf'
)
    
pdf = PdfReader(str(pdf_path))
