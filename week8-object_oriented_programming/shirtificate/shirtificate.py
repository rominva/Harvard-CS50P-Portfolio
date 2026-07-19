# prompts the user for their name ✔
# outputs, using fpdf2, a CS50 shirtificate in a file called "shirtificate.pdf" ✔

# user_name + shirtificate.png => pdf :
    # The orientation of the PDF should be Portrait. ✔
    # The format of the PDF should be A4, which is 210mm wide by 297mm tall. ✔
    # The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally. ✔
    # The shirt’s image should be centered horizontally. ✔
        # The user’s name should be on top of the shirt, in white text(255, 255, 255). ✔
        # You’re even welcome to add borders, colors, and lines 
        # Your shirtificate needn’t match John Harvard’s precisely. ✔
        # And no need to wrap long names across multiple lines.

    # +----------------------------------+
    # |            HEADER                |  ← بالای هر صفحه
    # |----------------------------------|
    # |                                  |
    # |                                  |
    # |          محتوای اصلی             |
    # |                                  |
    # |                                  |
    # |----------------------------------|
    # |            FOOTER                |  ← پایین هر صفحه
    # +----------------------------------+


from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font for header
        self.set_font("helvetica", size=50)
        # Moving cursor to the right: a cell with 80 width 
        cell_x = 80 # Arbitrary number
        self.cell(cell_x, align="C")
        # print Header "CS50 Shirtificate" in top middle of the page (A4 = 210mm wide by 297mm)
        A4_x = 210
        A4_y = 297
        A4_x_middle = A4_x / 2
        cell_x_middle = cell_x / 2
        header_x = (A4_x_middle - cell_x_middle) / 2
        header_y = 55 # Arbitrary number
        self.cell(header_x, header_y, "CS50 Shirtificate", align="C")
        
        # Performing a line break
        break_space = 20 # Arbitrary number
        self.ln(break_space)

        # Rendering shirt pic
        image_w = A4_x - 20 # Arbitrary; a little less than A4_X
        image_x = (A4_x - image_w) / 2
        image_y = (A4_y / 2) - (header_y + break_space)
        self.image("shirtificate.png", image_x, image_y, image_w)


def main():
    user_name = input("Name: ")
    make_pdf(user_name)


def make_pdf(name):
    # Make a pdf object of PDF class
    pdf = PDF(orientation="P", unit="mm", format="A4")

    # Add one page
    pdf.add_page()

    # Set font for name
    pdf.set_font("helvetica", size=24)

    # Setting colors for name on the shirt in White color
    pdf.set_text_color(255, 255, 255)

    # Print name on the shirt
    pdf.cell(190, 220, f"{name} took CS50", align='C')

    # Save & close the document
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()