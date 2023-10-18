from PyPDF2 import PdfFileMerger
pdf_merger = PdfFileMerger()
from pathlib import Path
reports_dir = (
    Path.home() /
    "OneDrive" /
    "Рабочий стол" /
    "expense-reports"
)
##for path in reports_dir.glob("*.pdf"):
##    print(path.name)

expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()

##for path in expense_reports:
##    print(path.name)

#Concatenating PDFs into one file

for path in expense_reports:
    pdf_merger.append(str(path))

with Path("expense_reports.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)


