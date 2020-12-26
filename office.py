'''
createPDF()
docx to pdf(docx)
docx to txt(docx)
txt to pdf(txt)
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

def createPDF(pdfFileName):
    # pdfFileName is the name in which the user would like to have the PDF file created. 
    from fpdf import FPDF
    # import the FPDF function 
    pdf = FPDF()
    # for convinience purposes 
    pdf.add_page()
    # add a page to the PDF 
    pdf.set_font('Arial', size = 15)
    # setting font and font size 
    textToBeEntered = input("Enter the Text: ") 
    # This is the text which we would get from the GUI box. 
    pdf.cell(200, 10, txt = textToBeEntered, align = 'C')
    # Add the text to the PDF by adding the cell. 
    pdf.output(f"{pdfFileName}.pdf")
    # output the PDF with the fileName provided by the user with the PDF extension

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

def docxToPDF(docxFileName):
    from docx2pdf import convert
    if '/' in docxFileName:
        convert(f"{docxFileName}")
        # if the given name is a folder name, then it would contain a /. Hence, we use the convert method used for folder. 
        # this function will convert all the docx files inside the folder into PDF and store them again inside the same folder. 
    else:
        convert(f"{docxFileName}.docx", f"{docxFileName}.pdf")
        # if the given name is a file name, then it will not contain a / and hence, we use the convert method used for files. 







