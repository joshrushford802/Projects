import fpdf


class shirt:

    def __init__(self, id):

        self._pdf = fpdf.FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_text_color(0, 0, 0)
        self._pdf.set_font_size(50)

        self._pdf.text(x=38, y=100, txt="{} took CS50".format(id))

    def make_shirt(self, id):
        self._pdf.output(id)


pic = shirt(input("What's your first name, friend? "))
pic.make_shirt("shirtificate.pdf")
print("Your new shirt has been created!")
