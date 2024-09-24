import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() or ''  # Handle cases where extract_text() might return None
    return text

# Example usage
pdf_path = 'C:\\Users\\Asus\\Downloads\\Gen AI Hackathon Study Material .pdf'
text = extract_text_from_pdf(pdf_path)
print(text)
