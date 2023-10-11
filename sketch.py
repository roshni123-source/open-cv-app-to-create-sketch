import streamlit as st
import numpy as np
import cv2 as cv

from PIL import Image

def sketch_image(img):
    grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    invert = cv.bitwise_not(grey_img)
    blur = cv.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv.bitwise_not(blur)
    sketch = cv.divide(grey_img, invertedblur, scale=256.0)
    return sketch

upload=st.file_uploader("choose an image",type=["jpg","png","jpeg"])
if upload is not None:
    file=np.asarray(bytearray(upload.read()),dtype=np.uint8)
    img=cv.imdecode(file,1)


# display the image
st.image(img,channels="BGR",use_column_width=True)


st.header("to convert image into pencil sketch")
if st.button("image to sketch"):
    sketch_img=sketch_image(img)
    st.image(sketch_img,use_column_width=True)

def get_data():
    # Add your data retrieval logic here
    return {'message': 'Data from Streamlit backend'}

def main():
    st.title('Streamlit Backend App')
    st.write('This is the backend app powered by Streamlit.')

if __name__ == '__main__':
    main()

    
