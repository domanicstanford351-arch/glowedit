
import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="GlowEdit Pro AI", page_icon="✨", layout="centered")
st.title("✨ GlowEdit Pro AI")
st.write("Remove BG + AI Background Generator")

if 'uses' not in st.session_state:
    st.session_state.uses = 0
FREE_LIMIT = 3

# --- YOUR PAY LINKS ---
PAYPAL_LINK = "https://www.paypal.com/paypalme/TironSmith458/4.99"
BUYMEACOFFEE_LINK = "https://www.buymeacoffee.com/TironSmith458"

st.markdown("---")
col1, col2 = st.columns(2)
col1.metric("Free Left", f"{max(0, FREE_LIMIT - st.session_state.uses)}/{FREE_LIMIT}")
col2.metric("Price", "$4.99")

st.subheader("🔓 Unlock Unlimited Pro - $4.99")
st.write("Free: 3 images/day. Pro: Unlimited + HD + No Watermark")

st.link_button("💳 Unlock Pro - Pay $4.99 with PayPal", PAYPAL_LINK, use_container_width=True, type="primary")
st.link_button("☕ Or Pay with Card", BUYMEACOFFEE_LINK, use_container_width=True)
st.markdown("---")

uploaded_file = st.file_uploader("Upload your image", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original", use_container_width=True)
    
    if st.session_state.uses >= FREE_LIMIT:
        st.error(f"⚠️ Free limit reached! You used {FREE_LIMIT} edits.")
        st.write("Unlock Pro to continue - money goes to Tiron Smith PayPal!")
        st.link_button("💵 Pay $4.99 to Unlock - PayPal", PAYPAL_LINK, use_container_width=True, type="primary")
    else:
        if st.button("✨ Remove Background (FREE)", use_container_width=True, type="primary"):
            st.session_state.uses += 1
            st.success(f"✅ Done! {FREE_LIMIT - st.session_state.uses} free left")
            st.image(image, use_container_width=True)
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            st.download_button("⬇️ Download Result", buf.getvalue(), "result.png", "image/png", use_container_width=True)
            if st.session_state.uses >= 2:
                st.info("Love it? Unlock Unlimited for $4.99 👆")

st.info("📲 iPhone: Safari -> Share -> Add to Home Screen")
st.caption("Secure payments by PayPal • Support: @TironSmith458")
