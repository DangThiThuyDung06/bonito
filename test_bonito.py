import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)  # Open the PDF file
    text = ""
    for page in doc:  # Iterate through each page
        text += page.get_text()  # Extract text and append it to the text variable
    return text

pdf_path = 'TamCam (1).pdf'  # Specify the path to your PDF document
text = extract_text_from_pdf(pdf_path)
print(text)