from reportlab.pdfgen.canvas import Canvas
canvas = Canvas("hello.pdf")
canvas.drawString(72, 72, "Hello World")
canvas.save()

# Setting The Page Size

canvas = Canvas("hello.pdf", pagesize=(612.0, 729.0))

from reportlab.lib.units import inch, cm

print(cm)
print(inch)

canvas = Canvas("hello.pdf", pagesize=(8.5 * inch, 11 * inch))

from reportlab.lib.pagesizes import LETTER
print(LETTER)

# Setting Font Properties (font, size, color etc.)

canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas.save()

# Setting the color

from reportlab.lib.colors import blue

canvas = Canvas("font-colors.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 12)
canvas.setFillColor("blue")
canvas.drawString(1*inch, 10*inch, "Blue text")
canvas.save()