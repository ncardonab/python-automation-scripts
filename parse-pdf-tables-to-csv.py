import os
import requests
import io
from pdf2image import convert_from_path
# import pytesseract

# Set the API endpoint for OCR conversion
API_ENDPOINT = 'https://api.ocr.space/parse/image'

# Set your API key for OCR conversion
API_KEY = 'K88462704288957'

# Set the path to your PDF file
PDF_FILE = '/Users/ncardona/Desktop/workbook-de-ia-en-el-dia-a-dia.pdf'

# Set the output directory for the CSV files
OUTPUT_DIR = '/Users/ncardona/Desktop/'

# Convert each page of the PDF file to an image and process it with OCR
pages = convert_from_path(PDF_FILE, dpi=300)
for i, page in enumerate(pages):
    # Save the page image to a byte stream
    img_byte_arr = io.BytesIO()
    page.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Use the OCR API to extract the text from the image
    payload = {
        'apikey': API_KEY,
        'language': 'eng',
        'isOverlayRequired': False,
        'filetype': 'PNG'
    }
    files = {
        'image': ('image.png', img_byte_arr)
    }
    response = requests.post(API_ENDPOINT, data=payload, files=files)
    response_data = response.json()

    # Extract the text from the response and write it to a CSV file
    if response_data['OCRExitCode'] == 1:
        csv_filename = os.path.join(OUTPUT_DIR, f'page_{i+1}.csv')
        text = response_data['ParsedResults'][0]['ParsedText']
        with open(csv_filename, 'w') as f:
            f.write(text)
    else:
        print(f'Error processing page {i+1}: {response_data["ErrorMessage"]}')
