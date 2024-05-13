from PIL import Image
import streamlit as st

st.title("Chettanahalli Village Tourism Promotion")
st.write("Welcome to the virtual tour of Chettanahalli, K R Pete, Mandya.")
st.write("Explore the beauty of Chettanahalli, a serene village nestled in the heart of K R Pete, Mandya. "
         "Immerse yourself in the rich culture, heritage, and natural landscapes that define this picturesque "
         "village. Whether it's the lush green fields, ancient temples, or vibrant community life, Chettanahalli "
         "offers an unforgettable experience for travelers seeking tranquility and authenticity.")    

# Image URLs
image1 = "./image1.jpg"
image2 = "./image2.jpg"
image3 = "./image3.jpg"
image4 = "./image4.jpg"
image5 = "./image5.jpg"
image6 = "./image6.jpg"
image7 = "./image7.jpg"
image8 = "./image8.jpg"

# Resize images to a larger size
def resize_image(image_path, output_size=(600, 450)):
    image = Image.open(image_path)
    image = image.resize(output_size)
    return image

# Display Images
col1, col2 = st.columns(2)
with col1:
    st.image(resize_image(image1), caption='A farmer using a Tractor for Ploughing a land field for planting the coconut plant', use_column_width=True)
    st.image(resize_image(image3), caption='A Beautiful Lake near K R Pete', use_column_width=True)
    st.image(resize_image(image5), caption='A Beautiful scenery taken when it was raining and a rainbow was appearing', use_column_width=True)
    st.image(resize_image(image7), caption='An Old ancient Hanuman Temple in the Chettenahalli Village', use_column_width=True)

with col2:
    st.image(resize_image(image2), caption='Image of my Grandfather who planted the Cocunut Plant', use_column_width=True)
    st.image(resize_image(image4), caption=' Paddy cultivation at my grandpa Land', use_column_width=True)
    st.image(resize_image(image6), caption='Cocunut Trees of my Grandpa Land with grass filled around ', use_column_width=True)
    st.image(resize_image(image8), caption='Hanuman Temple with ancient building and an statue outside', use_column_width=True)

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    .st-cc img {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .st-cc > div {
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
