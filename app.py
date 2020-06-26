### create venv
# python -m venv venv
# venv\Scripts\activate.bat

### install depend
# pip install streamlit
# pip install streamlit opencv-python
# pip install pillow
# pip install numpy

### create reqs.txt
# pip freeze > requirements.txt

### Core Pkgs
import streamlit as st 
import cv2 as cv
from PIL import Image,ImageEnhance
import numpy as np 
import os

### Main Webapp page
def main():
    # header and sidebar
    # streamlit title
    st.title("Photo Enhancer")
    # streamlit dexcription under title
    st.text("Upload any photo below, and check enhancers to the left")
    # init things you can with streamlit app
    activities = ("Enhance", "About")
    # create sidebar with these 2 activities
    choice = st.sidebar.selectbox("Select", activities)

    # Setting up function that creates action when user clicks activity
    # if user wants to use detection
    if choice == 'Enhance':
        # create spot to upload file
        image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])
        
        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Image")
            # st.write(type(our_image))
            st.image(our_image)
        
            # Image enhancement features
            enhance_type = st.sidebar.radio("Enhancement Type",["Original","Grayscale","Contrast","Brightness","Blur","Cartoon","Outline"])
            # feature for grayscale
            if enhance_type == 'Grayscale':
                new_img = np.array(our_image.convert('RGB'))
                # using cv to cvt color of image to grayscale (1)
                img = cv.cvtColor(new_img,1)
                gray = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)
                # st.write(new_img)
                st.text("Grayscale Image")
                st.image(gray)
            # feature for contrast
            elif enhance_type == 'Contrast':
                # create sliderbar to pick contrast rate
                c_rate = st.sidebar.slider("Contrast",0.5,3.5)
                # init enhancer from PIL pack
                enhancer = ImageEnhance.Contrast(our_image)
                # apply enhancer with sliderbar
                img_output = enhancer.enhance(c_rate)
                # allow enhancer to apply to image in streamlt app
                st.text("Contrast Image")
                st.image(img_output)
            # feature for brightness
            elif enhance_type == 'Brightness':
                # create sliderbar to pick contrast rate
                c_rate = st.sidebar.slider("Brightness",0.5,3.5)
                # init enhancer from PIL pack
                enhancer = ImageEnhance.Brightness(our_image)
                # apply enhancer with sliderbar
                img_output = enhancer.enhance(c_rate)
                # allow enhancer to apply to image in streamlt app
                st.text("Brightened Image")
                st.image(img_output)
            # feature for grayscale
            elif enhance_type == 'Blur':
                # create an array of RGB numbers from image
                new_img = np.array(our_image.convert('RGB'))
                # create sliderbar to pick blur rate
                blur_rate = st.sidebar.slider("Brightness",0.5,3.5)
                # using cv to cvt color of image to blur
                img = cv.cvtColor(new_img,1)
                blur_img = cv.GaussianBlur(img,(11,11), blur_rate)
                # st.write(new_img)
                st.text("Blurred Image")
                st.image(blur_img)
            # cartoonize image
            elif enhance_type == 'Cartoon':
                new_img = np.array(our_image.convert('RGB'))
                img = cv.cvtColor(new_img,1)
                gray = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)
                # Edges
                gray = cv.medianBlur(gray, 5)
                edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
                #Color
                color = cv.bilateralFilter(img, 9, 300, 300)
                #Cartoon
                cartoon = cv.bitwise_and(color, color, mask=edges)
                st.text("Cartoon Image")
                st.image(cartoon)
            # outline
            elif enhance_type == 'Outline':
                new_img = np.array(our_image.convert('RGB'))
                img = cv.cvtColor(new_img,1)
                img = cv.GaussianBlur(img, (11, 11), 0)
                canny = cv.Canny(img, 100, 150)
                st.text("Outline Image")
                st.image(canny)

    # if user selects about
    elif choice == 'About':
        # show subheading
        st.subheader("About Photo Enhancer")
        st.markdown("Built with Streamlit, OpenCV, Numpy, and PIL")
        st.text("Thanks to @JCharisTech")
        st.success("By Sam Perlmutter")

### init streamlit app
if __name__ == '__main__':
    main()	

### test app locally
# streamlit run app.py

### deploy to azure app service