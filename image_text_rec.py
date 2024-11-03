import cv2
import gradio as gr
import pytesseract
from langdetect import detect

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def read_image_and_detect_language(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='kan')
    language = detect(text)
    return text, language

# Gradio interface for image text recognition
def image_text_recognition(image):
    image = cv2.imread(image)
    text, language = read_image_and_detect_language(image)
    return text, language

gr_image_rec = gr.Interface(fn=image_text_recognition, inputs="file", outputs=["text", "text"], title="Image Text Recognition")
