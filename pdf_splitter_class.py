from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

class PdfFileSplitter:
    """Splits PDF into 2 files"""
    def __init__(self, pdf_path):
        self.pdf_reader = PdfFileReader(pdf_path)
        self.writer1 = None
        self.writer2 = None

    def split(self, breakpoint):
        """Split PDF into two PdfFilleWriter instances"""
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()

        for page in self.pdf_reader.pages[:breakpoint]:
            self.writer1.addPage(page)

        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.addPage(page)

    def write(self, filename):
        """Write two PDF instances to files"""

        with Path(filename + "_1.pdf").open(mode='wb') as output_file:
            self.writer1.write(output_file)

        with Path(filename + "_2.pdf").open(mode='wb') as output_file:
            self.writer2.write(output_file)

pdf_splitter = PdfFileSplitter("C:/Users/vladi/OneDrive/Рабочий стол/Code/Python PDF/Pride_and_Prejudice.pdf")
pdf_splitter.split(breakpoint=150)
pdf_splitter.write("pride_split")