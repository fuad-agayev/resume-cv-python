from docx import Document
import comtypes.client
import os

def create_cover_letter():
    # Tam cover letter metni
    cover_letter_text = (
        "Dear Hiring\n\n"
        "I am writing to express my interest in the Frontend Developer position at your company. "
        "Based in Baku, Azerbaijan, I bring over 3 years of hands-on experience in building modern, scalable, "
        "and SEO-optimized web applications using Vue.js 3 and Nuxt.js 3.\n\n"
        "I’m especially impressed by your focus on open-source innovation and scalable platforms, and I believe my experience "
        "with SSR/CSR, Tailwind, and TypeScript aligns well with your technical stack. My recent projects, including an SEO-optimized "
        "movie streaming platform and a modern e-commerce SPA, reflect my dedication to performance, accessibility, and clean architecture.\n\n"
        "I’m excited about the opportunity to contribute to your team and bring my enthusiasm and skills to your projects.\n\n"
        "Best regards,\n"
        "Fuad Aghayev\n"
        "Baku, Azerbaijan\n"
        "fuad0000010@gmail.com\n"
        "https://fuad-foliou.netlify.app/"
    )

    # .docx oluşturma
    doc = Document()
    for paragraph in cover_letter_text.split('\n\n'):
        doc.add_paragraph(paragraph)
    
    filename = "Fuad_Aghayev_CoverLetter.docx"
    doc.save(filename)
    print(f"DOCX dosyası oluşturuldu: {filename}")
    return filename

def convert_docx_to_pdf(docx_path):
    pdf_path = docx_path.replace(".docx", ".pdf")
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False
    doc = word.Documents.Open(docx_path)
    doc.SaveAs(pdf_path, FileFormat=17)  # 17 = wdFormatPDF
    doc.Close()
    word.Quit()
    print(f"PDF dosyası oluşturuldu: {pdf_path}")
    return pdf_path

def get_comment_version():
    comment = (
        "Hello, I’m Fuad Aghayev, a frontend developer from Baku with 3+ years of experience using Nuxt.js and Vue.js. "
        "I’m excited to apply for the Frontend Developer role at WiseTech Global — your open-source approach and focus on scalable "
        "web products really resonate with me. I’d love the opportunity to contribute with my skills in SEO, SSR, and performance-focused UI development."
    )
    print("\nComment alanına yapıştırmak için kısa versiyon:\n")
    print(comment)
    return comment

if __name__ == "__main__":
    docx_file = create_cover_letter()
    convert_docx_to_pdf(os.path.abspath(docx_file))
    get_comment_version()
