import streamlit as st
from ultralytics import YOLO
from PIL import Image
import collections

st.set_page_config(
    page_title="Elevate Vision | Bahulika",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }
    section[data-testid="stSidebar"] .stElementContainer {
        margin-bottom: 0.3rem; 
    }
    section[data-testid="stSidebar"] h2 {
        padding-top: 0.5rem;
        margin-bottom: 0.2rem;
        font-size: 1.1rem;
    }
    
    .main-header {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        color: white; 
        font-family: sans-serif;
        font-weight: 700;
        margin: 0;
        font-size: 2.5rem;
    }
    .main-header p {
        color: #e0e0e0;
        font-size: 1.1rem;
        margin-top: 10px;
    }
    
    .info-box {
        background-color: #e3f2fd;
        border-left: 5px solid #2196f3;
        padding: 15px;
        border-radius: 5px;
        color: #0d47a1;
        font-weight: 500;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ AI Configuration")
    st.info("Adjust settings to customize detection levels.")

    st.subheader("1. Intelligence Level")
    model_choice = st.selectbox(
        "Choose Model Size:",
        ["Nano (Fast & Lightweight)", "Medium (Balanced)", "Large (High Accuracy)"],
        index=1
    )
    
    if "Nano" in model_choice: model_file = 'yolov8n.pt'
    elif "Medium" in model_choice: model_file = 'yolov8m.pt'
    else: model_file = 'yolov8l.pt'

    st.markdown("<hr style='margin: 10px 0; opacity: 0.3;'>", unsafe_allow_html=True)

    st.subheader("2. AI Object Detection Strictness")
    st.caption("Lower = Detects everything.\n Higher = Only definite matches.")
    
    conf_threshold = st.slider(
        "Strictness:", 
        min_value=0.0, max_value=1.0, value=0.45, step=0.05
    )
    
    if conf_threshold < 0.3:
        st.warning("⚠️ Loose: Might see false objects.")
    elif conf_threshold > 0.7:
        st.warning("🛡️ Strict: Might miss small objects.")
    else:
        st.success("✅ Balanced")

with st.sidebar:
    st.markdown("<hr style='margin: 10px 0; opacity: 0.3;'>", unsafe_allow_html=True)
    st.markdown("### 👩🏻‍💻 Created by **Bahulika**")
    st.caption("Microsoft Elevate Project | 2026")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/j-bahulika-8b8237207/")
    with col_b:
        st.link_button("GitHub", "https://github.com/JBahulika")

@st.cache_resource
def load_model(path):
    return YOLO(path)

st.markdown("""
    <div class="main-header">
        <h1>Elevate Vision</h1>
        <p>Advanced Object Detection & Inventory System</p>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="info-box">
        👋 <b>Hi!</b> This tool uses neural networks <b>YOLOv8</b> to perform object detection inside images.
        Upload a photo below to detect objects, count inventory, and analyze scenes instantly.
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Drop your image here to begin...", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    try:
        model = load_model(model_file)
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("### 🖼️ Original Photo")
            st.image(image, use_column_width=True, caption="Source Upload")
            
        with col2:
            st.markdown("### 🔎 Object detection")
            
            with st.spinner("⚡ Running AI Detection..."):
                
                results = model.predict(image, conf=conf_threshold)
                
                res_plotted = results[0].plot()
                st.image(res_plotted, use_column_width=True, caption=f"Real-time Detection ({model_choice})")
                
                class_ids = results[0].boxes.cls.cpu().numpy().astype(int)
                names = [model.names[i] for i in class_ids]
                counts = collections.Counter(names)
                
                st.success("✅ Analysis Complete!")
                with st.container():
                    st.markdown("#### 📊 Inventory Report")
                    if counts:
                        for name, count in counts.items():
                            st.markdown(f"- **{count}** {name.capitalize()}")
                    else:
                        st.warning("No objects found. Try lowering the 'Strictness' in the sidebar.")
    except Exception as e:
        st.error(f"System Error: {e}")

st.markdown("---")
st.markdown("<center style='color: #888;'>Designed & Developed by <b>Bahulika</b> for Microsoft Elevate.</center>", unsafe_allow_html=True)