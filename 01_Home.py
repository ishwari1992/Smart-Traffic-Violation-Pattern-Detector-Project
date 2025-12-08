import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Smart Traffic Violation Detector",
    page_icon="🚦",
    layout="wide"
)

# Load image
try:
    image = Image.open('assets/T01.jpg')
except:
    image = None

# Hero Section
st.markdown(
    """
    <h1 style='text-align: center; color:#2E86C1; font-size: 45px;'>
        🚦 Smart Traffic Violation Pattern Detector
    </h1>

    <p style='text-align: center; font-size: 20px; color: #555;'>
        An intelligent, data-driven dashboard designed to uncover trends, hotspots,<br>
        and behavior patterns in traffic violations for smarter and safer cities.
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Image + Text Layout
col1, col2 = st.columns([1, 1.3])

with col1:
    if image:
        st.image(image, width="stretch")
    else:
        st.info("Add an image at: assets/T01.jpg")
with col2:
    st.markdown(
        """
        ### 🔍 What This System Does  
        This interactive platform provides:
        - 📊 **Violation analytics** based on type, location & weather  
        - 🗺️ **Hotspot detection** to identify high-risk zones  
        - 🚗 **Vehicle & driver statistics**  
        - 💳 **Fine distribution & payment behavior**  
        - ⛈ **Weather impact on violation behavior**  
        - 💳 **Average Fine Per Locations**
        """
    )
   
st.write("---")
st.success("✔ Designed using Python, Streamlit, Pandas, Matplotlib, Seaborn")