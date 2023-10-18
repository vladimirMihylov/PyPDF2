# from pathlib import Path
# from PyPDF2 import PdfFileReader, PdfFileWriter

# pdf_path = (
#     Path.home() /
#     "OneDrive" / 
#     "Рабочий стол" / 
#     "ugly.pdf"
# )

# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()

# # first method to rotate, the impratical one.

# for n in range(pdf_reader.getNumPages()):
#     page = pdf_reader.getPage(n)
#     if n % 2 == 0:
#         page.rotateClockwise(90)
#     pdf_writer.addPage(page)

# with Path("ugly_rotated.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# # second approach

# pdf_reader = PdfFileReader(str(pdf_path))
# # print(pdf_reader.getPage(0)) # mixed with nonsential looking stuff there's a key called /Rotate

# # page = pdf_reader.getPage(0)
# # # print(page["/Rotate"])
# # page = pdf_reader.getPage(1)
# # #print(page["/Rotate"])

# # page = pdf_reader.getPage(0)
# # page.rotateClockwise(90)
# # print(page["/Rotate"])

# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()

# for page in pdf_reader.pages:
#     if page["/Rotate"] == -90:
#         page.rotateClockwise(90)
#     pdf_writer.addPage(page)

# with Path("ugly_rotated2.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# # Word of warning: /Rotate key may not exist


# 1.Rotating Exercise

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.home() /
    "OneDrive" / 
    "Рабочий стол" / 
    "split_and_rotate.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    if page["/Rotate"] == 90:
        page.rotateClockwise(-90)
    pdf_writer.addPage(page)

with Path("rotated.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# 2.Cropping Exercise
import copy

pdf_path = (
    Path.home() /
    "OneDrive" / 
    "Рабочий стол" /
    "Code" /
    "Python PDF" /
    "rotated.pdf"
) 

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

first_page = pdf_reader.getPage(0)
second_page = pdf_reader.getPage(1)

first_page_new = copy.deepcopy(first_page)
current_coords = first_page_new.mediaBox.upperRight
new_coords = (current_coords[0] / 2, current_coords[1])
first_page_new.mediaBox.upperRight = new_coords

second_page_new = copy.deepcopy(first_page)
second_page_new.mediaBox.upperLeft = new_coords

third_page_new = copy.deepcopy(second_page)

current_coords = third_page_new.mediaBox.upperRight
new_coords = (current_coords[0] / 2, current_coords[1])
third_page_new.mediaBox.upperRight = new_coords

forth_page_new = copy.deepcopy(second_page)
forth_page_new.mediaBox.upperLeft = new_coords

pdf_writer.addPage(first_page_new)
pdf_writer.addPage(second_page_new)
pdf_writer.addPage(third_page_new)
pdf_writer.addPage(forth_page_new)
with Path("split.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    upper_right_coords = page.mediaBox.upperRight
    center_coords = (upper_right_coords[0] / 2, upper_right_coords[1])

    left_page = copy.deepcopy(page)
    right_page = copy.deepcopy(page)

    left_page.mediaBox.upperRight = center_coords
    right_page.mediaBox.upperLeft = center_coords

    pdf_writer.addPage(left_page)
    pdf_writer.addPage(right_page)

with Path("split2.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


