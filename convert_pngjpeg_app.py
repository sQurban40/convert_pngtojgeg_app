#importing required packages
import streamlit
from PIL import Image
import io

#adding title of the streamlit app
streamlit.title('PNG to JPEG Converter')

# let user to upload multiple PNG files using File uploader
uploaded_files = streamlit.file_uploader("Choose PNG files", type="png", accept_multiple_files=True)

# initializing a dictionary to store converted images
converted_images = {}

# adding a "Convert" button
if streamlit.button('Convert'):
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # open the image file usnig Image object of PIL package
            image = Image.open(uploaded_file)

            # converting file/s to JPEG
            with io.BytesIO() as output:
                image.convert("RGB").save(output, format="JPEG")
                converted_image = output.getvalue()
            # Storing the converted image the dictionary
            converted_images[uploaded_file.name] = converted_image

        # Displaying the converted images and download buttons to allow user to download converted images
        for file_name, converted_image in converted_images.items():
            # Generate a download link
            download_link = f'<a href="data:file/jpeg;base64,{base64.b64encode(converted_image.read()).decode()}" download="{uploaded_file.name.replace(".png", ".jpeg")}">Download {uploaded_file.name.replace(".png", ".jpeg")}</a>'
            st.markdown(download_link, unsafe_allow_html=True)
            streamlit.write(f"Original file: {file_name}")
            streamlit.image(converted_image, caption='Converted JPEG image', use_column_width=True, output_format="JPEG")
            streamlit.download_button(
                label=f"Download {file_name.rsplit('.', 1)[0]}.jpeg",
                data=converted_image,
                file_name=f"{file_name.rsplit('.', 1)[0]}.jpeg", on_click=None,
                mime="image/jpeg"
            )
    else:
        streamlit.warning("Please upload a PNG file.")
