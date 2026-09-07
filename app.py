
import streamlit as st
from rembg import remove
from PIL import Image
import io
import requests

st.set_page_config(page_title="GlowEdit Pro AI", page_icon="✨", layout="centered")

st.markdown("<h1 style='text-align:center;'>GlowEdit Pro AI ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Remove BG + AI Background Generator</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your image", type=["png","jpg","jpeg"])

if uploaded_file:
    input_img = Image.open(uploaded_file).convert("RGBA")
    st.image(input_img, caption="Original", use_container_width=True)
    
    if st.button("🪄 Remove Background - HD", use_container_width=True, type="primary"):
        with st.spinner("Making it glow..."):
            output = remove(input_img)
            st.session_state['cutout'] = output
            st.image(output, caption="Cutout - Transparent", use_container_width=True)
            
            buf = io.BytesIO()
            output.save(buf, format="PNG")
            buf.seek(0)
            st.download_button("⬇️ Download Transparent PNG", buf, "glowedit_hd.png", "image/png", use_container_width=True)

if 'cutout' in st.session_state:
    st.markdown("---")
    st.markdown("### 🤖 AI Background Generator - PRO")
    prompt = st.text_input("Describe your new background:", placeholder="e.g. luxury office, beach sunset, neon city, white studio")
    
    if st.button("✨ Generate AI Background", use_container_width=True):
        if prompt:
            with st.spinner(f"AI generating: {prompt}..."):
                try:
                    # Free AI image gen
                    url = f"https://image.pollinations.ai/prompt/{prompt}?width=1024&height=1024&nologo=true"
                    resp = requests.get(url, timeout=30)
                    bg = Image.open(io.BytesIO(resp.content)).convert("RGBA").resize(st.session_state['cutout'].size)
                    fg = st.session_state['cutout']
                    final = Image.alpha_composite(bg, fg)
                    st.image(final, caption=f"AI Background: {prompt}", use_container_width=True)
                    buf2 = io.BytesIO()
                    final.save(buf2, format="PNG")
                    buf2.seek(0)
                    st.download_button("⬇️ Download AI Background HD", buf2, "glowedit_ai_bg.png", "image/png", use_container_width=True, type="primary")
                except Exception as e:
                    st.error(f"AI error: {e} - try again")
        else:
            st.warning("Type a background description first!")

st.markdown("---")
st.markdown("### Want Unlimited HD + AI? 💎")
st.link_button("🔓 Unlock PRO - $4.99 One Time", "https://paypal.me/TironSmith458/4.99CAD", use_container_width=True, type="primary")
st.caption("Pay once, get unlimited HD + AI Generator - money to Tiron Smith")
st.caption("Built in Welland, Ontario 🇨🇦 | GlowEdit Pro V2")
