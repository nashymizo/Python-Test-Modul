from fpdf import FPDF


class MyPdf(FPDF):



    def create_title(self, title=""):
        #
        width = self.w - (self.l_margin + self.r_margin)

        #
        self.set_font("helvetica", style="", size=16)
        self.set_text_color(30, 60, 100)
        self.multi_cell(w=width, h=16, text=title, border=0, align='C')
        self.set_x(pdf.l_margin)

    def create_headline(self, text, level=1):
        """Überschrift H1 bis H5."""

        sizes = {
            1: 18,
            2: 16,
            3: 14,
            4: 12,
            5: 11,
        }

        self.set_font("Helvetica", "B", sizes[level])
        self.set_text_color(30, 30, 30)

        self.multi_cell(0, 8, text)
        self.ln(2)


    def create_paragraph(self, text):
        """Normaler Absatz."""
        self.set_font("Helvetica", "", 11)
        self.set_text_color(40, 40, 40)

        width = self.w - (self.l_margin + self.r_margin)
        self.multi_cell(width,6,text,align="J")
        self.ln(4)

    def bullet_list(self, items):
        """Aufzählung mit Punkten."""

        self.set_font("Helvetica", "", 11)

        for item in items:
            self.cell(8, 5, "-")
            self.multi_cell(0, 5, item)
            self.set_x(self.l_margin)

        self.ln(3)





pdf = MyPdf(orientation="P", unit="mm", format="A4")
pdf.add_page()


pdf.create_title("Hallo Mein Titel")

# ==================================================
# HEADLINE 1
# ==================================================
pdf.create_headline("1. Überschrift Ebene 1", 1)
pdf.create_paragraph(
    "Dies ist ein normaler Absatz. FPDF kann Text umbrechen, Absätze darstellen und verschiedene Schriftarten und Schriftgrößen verwenden. Mit multi_cell() lassen sich auch längere Texte problemlos ausgeben."
)
# ==================================================
# HEADLINE 2
# ==================================================
pdf.create_headline("1.1 Überschrift Ebene 2", 2)
pdf.create_paragraph(
    "Eine Überschrift der zweiten Ebene eignet sich beispielsweise "
    "für Unterkapitel eines Dokuments."
)


# ==================================================
# HEADLINE 3
# ==================================================
pdf.create_headline("1.1.1 Überschrift Ebene 3", 3)
pdf.create_paragraph(
    "Die dritte Ebene kann für weitere Unterteilungen verwendet werden."
)

# ==================================================
# AUFZÄHLUNG
# ==================================================
pdf.create_headline("2. Aufzählung", 1)
pdf.bullet_list([
    "Python",
    "Java",
    "C#",
    "JavaScript",
    "PHP"
])


# PDF speichern
pdf_path = "kitchensink.pdf"
pdf.output(pdf_path)
