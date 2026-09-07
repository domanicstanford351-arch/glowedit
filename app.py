
import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="GlowEdit Pro AI", page_icon="✨", layout="centered")

st.markdown("<h1 style='text-align: center;'>✨ GlowEdit Pro AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Remove BG + AI Background Generator</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your image", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original", use_container_width=True)
    
    if st.button("✨ Remove Background"):
        st.success("Background removed! (Add rembg later)")
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        st.download_button("Download", buf.getvalue(), "result.png", "image/png")

st.markdown("---")
st.info("📲 On iPhone: Tap Share → Add to Home Screen to make it an App!")
