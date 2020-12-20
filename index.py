from fpdf import FPDF

document = FPDF()
document.add_page()
document.set_font('Arial', size=12)
document.cell(w=0, txt="Hola mundo")
document.output("hello_world.pdf")
