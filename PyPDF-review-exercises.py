#1.

from pathlib import Path
from PyPDF2 import PdfFileMerger

pdf_merger = PdfFileMerger()

merges_dir = (
    Path.home() /
    "OneDrive" /
    "Рабочий стол" /
    "PyPDF-review-exercises"
)

merge_files = merges_dir / "merge1.pdf", merges_dir / "merge2.pdf"

for path in merge_files:
    pdf_merger.append(str(path))

with Path("concatenated.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)

#2.
pdf_merger = PdfFileMerger()
pdf_merger.append(str(Path("concatenated.pdf")))
merge3_path = merges_dir / "merge3.pdf"
pdf_merger.merge(1, str(merge3_path))

with Path("merged.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)


