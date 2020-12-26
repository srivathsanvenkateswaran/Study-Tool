'''
docx to pdf(docx)
docx to txt(docx)
pdf to docx(pdf)
pdf to ppt(pdf)
pdf to txt(txt)
ppt to pdf(ppt)
csv to xlsx(csv)
xlsx to pdf(xlsx)

CompressToZip(folder)
unZip(zipFile)

imageView(img)
imageResize(width, height)
compressImage(img)

sendMail()
uploadToDrive(file)
'''

def txtToPDF(txtFileName):
    from fpdf import FPDF 
    # import the FPDF function 
    pdf = FPDF()
    # for convinience purposes 
    pdf.add_page() 
    # add a page to the PDF 
    pdf.set_font('Arial', size = 15)
    # setting font and font size 
    file = open(f"{txtFileName}.txt", r)
    # open the file in read mode 
    for x in file: 
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
    # read all the text in the file and add it in the pdf  
    pdf.output(f"{txtFileName}.pdf")
    # output the PDF with the same name and .pdf extension 