from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 50, 36, 110)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 25)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 shirtificate", align="C")
        # Performing a line break:
        self.ln(20)




pdf = PDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Times", "B", size=22)
pdf.set_text_color(255, 255, 255)

# Add text to PDF
name = input('enter name:' )
pdf.cell(0, 90, f"{name} took cs50", align='C')

pdf.output("shirtificate.pdf")

