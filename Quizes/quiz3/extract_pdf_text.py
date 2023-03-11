import pdfminer.high_level

# Open the PDF file in read-binary mode
with open('quiz_3.pdf', 'rb') as pdf_file:

    # Extract the text from the PDF file
    text = pdfminer.high_level.extract_text(pdf_file, laparams=None)

    # Print the extracted text
    print(text)
