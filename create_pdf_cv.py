from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Fuad Agayev - Nuxt.js Developer", ln=True, align="C")
pdf.cell(200, 10, txt="Baku, Azerbaijan | fuad0000010@gmail.com", ln=True, align="C")
pdf.ln(10)
pdf.multi_cell(0, 10, "Summary:\nFrontend developer skilled in Vue.js and Nuxt.js 3...")

# PDF dosyasını oluştur
file_name = "Fuad_Agayev_pdf_CV.pdf"
#* oldugumuz klasorde acar bu OUTPUT pdf.output
#*pdf.output("C:/Users/acer/Desktop/Fuad_Agayev_CV.pdf")  boylede direkt yonun da gostere bilirin bilgisyarda 
pdf.output(file_name)
print(f"PDF başarıyla oluşturuldu: {file_name}")

#* Windows'ta otomatik aç  Laptop da pdf dosyasini acir
os.startfile(file_name)
#! PDF formatında oluşturmak daha fazla manuel hizalama ve stil ayarı ister
#! .docx gibi otomatik başlık stilleri, kolay düzenleme avantajları yok