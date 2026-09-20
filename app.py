import streamlit as st
from ocr_utils import extract_text_from_image

st.set_page_config(page_title="OCR - Image to Text", page_icon="📝")

st.title("📝 OCR - Image to Text")
st.write("Koi image upload karen, aur uska text nikal ke yahan dekhen.")

uploaded_file = st.file_uploader("Image upload karen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_path = uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    col1, col2 = st.columns(2)

    with col1:
        st.image(file_path, caption="Uploaded Image", use_container_width=True)

    with col2:
        with st.spinner("Text detect ho raha hai..."):
            texts = extract_text_from_image(file_path)

        if len(texts) == 0:
            st.warning("Is image mein koi text detect nahi hua. Koi aur image try karen.")
        else:
            st.subheader("Detected Text:")
            full_text = "\n".join(texts)
            st.text_area("Result", full_text, height=250)

            st.download_button(
                label="⬇️ Text Download Karen",
                data=full_text,
                file_name="detected_text.txt",
                mime="text/plain"
            )
else:
    st.info("Upar image upload karen shuru karne ke liye.")