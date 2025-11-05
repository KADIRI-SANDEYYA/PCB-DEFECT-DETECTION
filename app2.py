import streamlit as st
from PIL import Image
from ultralytics import YOLO
import tempfile
import numpy as np

# Load the YOLO model
model = YOLO("best.pt")

st.title("PCB Defect Detection")
st.write("Upload an image to find the defect in your PCB.")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open the uploaded image
    uploaded_image = Image.open(uploaded_file)
    
    # Convert image to a format YOLO can process
    img_array = np.array(uploaded_image)

    # Perform prediction directly on the image
    st.subheader("Prediction")
    results = model.predict(source=img_array, conf=0.1)

    # Get the output image with predictions
    result_img = results[0].plot()  # This generates an annotated image as a NumPy array
    
    # Convert NumPy array back to PIL Image
    result_pil = Image.fromarray(result_img)

    # Display images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_image, caption="Original Image")
    with col2:
        st.image(result_pil, caption="Predicted Image")

    st.success("Prediction complete!")
