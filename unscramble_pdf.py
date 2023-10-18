from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path("scrambled.pdf")
pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()


def get_page_text(page):
    return page.extractText()

pages = list(pdf_reader.pages)
pages.sort(key=get_page_text)


for page in pages:

    # if page["/Rotate"] == 90:
    #     page.rotateClockwise(-90)
    # elif page["/Rotate"] == 180:
    #     page.rotateClockwise(-180)
    # elif page["/Rotate"] == -90:
    #     page.rotateClockwise(90)
    # elif page["/Rotate"] == -180:
    #     page.rotateClockwise(180)

    rotation_degrees = page["/Rotate"]
    if rotation_degrees != 0:
        page.rotateCounterClockwise(rotation_degrees) 
    pdf_writer.addPage(page)




with Path("unscrambled.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


    







