import streamlit as st
from PIL import Image
import numpy as np
from image_processing import *

def main():
    st.title("Image Processing App")
    
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        image_array = np.array(image)
        
        processing_options = ["Original", "Grayscale", "Blur", "Edge Detection", "Sharpen", "Rotate", "Color Adjustment", "Threshold"]
        choice = st.selectbox("Select an option:", processing_options)
        
        if choice == "Grayscale":
            processed_image = apply_grayscale(image_array)
        elif choice == "Blur":
            processed_image = apply_blur(image_array)
        elif choice == "Edge Detection":
            processed_image = apply_edge_detection(image_array)
        elif choice == "Sharpen":
            processed_image = apply_sharpen(image_array)
        elif choice == "Rotate":
            angle = st.slider("Select rotation angle:", -180, 180, 0)
            processed_image = apply_rotation(image_array, angle)
        elif choice == "Color Adjustment":
            brightness = st.slider("Brightness", -100, 100, 0)
            contrast = st.slider("Contrast", 0.1, 3.0, 1.0)
            saturation = st.slider("Saturation", 0.1, 3.0, 1.0)
            processed_image = apply_color_adjustment(image_array, brightness, contrast, saturation)
        elif choice == "Threshold":
            threshold_value = st.slider("Threshold Value", 0, 255, 128)
            processed_image = apply_threshold(image_array, threshold_value)
    
        else:
            processed_image = image_array
        
        st.image(processed_image, use_column_width=True)

if __name__ == "__main__":
    main()
