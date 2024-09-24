import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page_number in range(len(pdf.pages)):
            page = pdf.pages[page_number]
            text += page.extract_text() or ''  # Handle cases where extract_text might return None
    return text

# Example usage
pdf_path =  'C:\\Users\\Asus\\Downloads\\Gen AI Hackathon Study Material .pdf'
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)
