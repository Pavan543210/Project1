from PIL import Image
import streamlit as st

st.title("Chettanahalli Village Tourism Promotion")
st.write("Welcome to the virtual tour of Chettanahalli, K R Pete, Mandya.")
    
# Image URLs
image1 = "./image1.jpg"
image2 = "./image2.jpg"
image3 = "./image3.jpg"
image4 = "./image4.jpg"
image5 = "./image5.jpg"
image6 = "./image6.jpg"
image7 = "./image7.jpg"
image8 = "./image8.jpg"

# Resize images to a specific dimension (400x300 pixels)
def resize_image(image_path, output_size=(400, 300)):
    image = Image.open(image_path)
    image = image.resize(output_size)
    return image

# Display Images
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(resize_image(image1), use_column_width=True, caption='Image 1')
with col2:
    st.image(resize_image(image2), use_column_width=True, caption='Image 2')
with col3:
    st.image(resize_image(image3), use_column_width=True, caption='Image 3')
with col4:
    st.image(resize_image(image4), use_column_width=True, caption='Image 4')

col5, col6, col7, col8 = st.columns(4)
with col5:
    st.image(resize_image(image5), use_column_width=True, caption='Image 5')
with col6:
    st.image(resize_image(image6), use_column_width=True, caption='Image 6')
with col7:
    st.image(resize_image(image7), use_column_width=True, caption='Image 7')
with col8:
    st.image(resize_image(image8), use_column_width=True, caption='Image 8')
    
# Description
st.write("Explore the beauty of Chettanahalli, a serene village nestled in the heart of K R Pete, Mandya. "
         "Immerse yourself in the rich culture, heritage, and natural landscapes that define this picturesque "
         "village. Whether it's the lush green fields, ancient temples, or vibrant community life, Chettanahalli "
         "offers an unforgettable experience for travelers seeking tranquility and authenticity.")
