import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import io

st.title("Interactive Image Filter App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_column_width=True)

  
    st.sidebar.title("Filter Options")

    filter_option = st.sidebar.selectbox(
        'Select a filter to apply:',
        ('None', 'Grayscale', 'Sepia', 'Blur', 'Contour', 'Enhance Contrast')
    )

 
    if filter_option == 'Grayscale':
        image = ImageOps.grayscale(image)
    elif filter_option == 'Sepia':
        sepia_image = ImageOps.colorize(ImageOps.grayscale(image), '#704214', '#C0C0C0')
        image = sepia_image
    elif filter_option == 'Blur':
        image = image.filter(ImageFilter.BLUR)
    elif filter_option == 'Contour':
        image = image.filter(ImageFilter.CONTOUR)
    elif filter_option == 'Enhance Contrast':
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)

   
    st.image(image, caption='Filtered Image', use_column_width=True)

 
    img_buffer = io.BytesIO()
    image.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    st.sidebar.download_button(
        label="Download Image",
        data=img_buffer,
        file_name="filtered_image.png",
        mime="image/png"
    )

else:
    st.write("Please upload an image to apply filters.")

