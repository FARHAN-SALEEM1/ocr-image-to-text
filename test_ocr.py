"""
ocr_utils.py
Yeh file OCR (text extraction) ka core logic rakhti hai.
Streamlit app isi file se function import kar ke use karegi.
"""

import easyocr

# Reader ek dafa load hota hai - taake har call par dobara load na ho (slow process hai)
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    """
    Image path leta hai, us mein se detected text lines ki list return karta hai.
    """
    result = reader.readtext(image_path)
    
    extracted_texts = []
    for detection in result:
        text = detection[1]
        extracted_texts.append(text)
    
    return extracted_texts


# --- Testing ke liye - jab file seedha run ho ---
if __name__ == "__main__":
    texts = extract_text_from_image('test.png')
    print("Total lines detected:", len(texts))
    for line in texts:
        print(line)