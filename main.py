from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Set line width
pdf.set_line_width(0.2)

# Set line color
pdf.set_draw_color(0, 0, 0)  # Black

# Draw lines


for index, row, in df.iterrows():
   
    pdf.add_page()
    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=10, h=12, ln=1, txt=row["Topic"], align="L")
 
    # set the footer
    pdf.ln(265)
    pdf.set_font("Times", style="B", size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    for y in range(20, 280, 10):  # Start at 20mm, end at 280mm, 10mm spacing
        pdf.line(10, y, 200, y)  # Draw line across the page 

    for i in range(int(row["Pages"]) -1):
        # add more pages and footer
        pdf.add_page()   

        pdf.ln(277)
        pdf.set_font("Times", style="B", size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R") 
        for y in range(20, 280, 10):  # Start at 20mm, end at 280mm, 10mm spacing
           pdf.line(10, y, 200, y)  # Draw line across the page
      
             

pdf.output("output.pdf")        