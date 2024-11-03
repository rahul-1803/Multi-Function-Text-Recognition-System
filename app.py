import gradio as gr
from audio_rec import recognize_kannada_speech  # Import from your speech recognition script
from image_text_rec import image_text_recognition  # Import from your image text recognition script
from real_time_camera_rec import real_time_camera  # Import from your camera text recognition script

# Create Gradio interfaces for each functionality
gr_speech_rec = gr.Interface(fn=recognize_kannada_speech, inputs=None, outputs="text", title="Kannada Speech Recognition")
gr_image_rec = gr.Interface(fn=image_text_recognition, inputs="file", outputs=["text", "text"], title="Image Text Recognition")
gr_camera_rec = gr.Interface(fn=real_time_camera, inputs=None, outputs=["text", "text"], title="Real-time Camera Text Recognition")

# Create a Gradio block to combine all the interfaces
app = gr.Blocks()

with app:
    gr.Markdown("## Multi-Function Text Recognition System")
    gr_speech_rec.render()
    gr_image_rec.render()
    gr_camera_rec.render()

# Launch the Gradio app
app.launch()
