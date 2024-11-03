import cv2
import gradio as gr
import pytesseract
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def recognize_text_in_frame(frame, langs='eng+kan'):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang=langs)
    try:
        language = detect(text)
    except LangDetectException:
        language = "Detection failed"
    return text, language

def real_time_camera():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        text, language = recognize_text_in_frame(frame)
    cap.release()
    return text, language

# Gradio interface for real-time camera recognition
gr_camera_rec = gr.Interface(fn=real_time_camera, inputs=None, outputs=["text", "text"], title="Real-time Camera Text Recognition")
