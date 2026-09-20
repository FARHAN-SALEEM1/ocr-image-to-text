"""
ocr_utils.py
Yeh file OCR (text extraction) ka core logic rakhti hai.
Streamlit app isi file se function import kar ke use karegi.
"""

import easyocr

reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    """
    Image path leta hai, us mein se detected text lines ki list return karta hai.
    Agar koi error aaye (jaise corrupt file), khaali list return karta hai.
    """
    try:
        result = reader.readtext(image_path)
    except Exception as e:
        print("Error during OCR:", e)
        return []
    
    extracted_texts = []
    for detection in result:
        text = detection[1]
        extracted_texts.append(text)
    
    return extracted_texts


if __name__ == "__main__":
    texts = extract_text_from_image('test.png')
    print("Total lines detected:", len(texts))
    for line in texts:
        print(line)