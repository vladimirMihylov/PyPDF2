from pathlib import Path
from PyPDF2 import PdfFileMerger

report_dir = (
    Path.home() /
    "OneDrive" /
    "Рабочий стол" /
    "quarterly_report"
)

report_path = report_dir / "report.pdf"
toc_path = report_dir / "toc.pdf"

pdf_merger = PdfFileMerger()
pdf_merger.append(str(report_path))

pdf_merger.merge(1, str(toc_path))

with Path("full_report.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
    

