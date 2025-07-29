import streamlit as st
import os
from file_parser import parse_structure
from file_creator import create_structure

st.set_page_config(page_title="AutoStruct AI", layout="centered")
st.title("📁 AutoStruct AI — Folder Structure Generator")

# Upload .txt file
uploaded_file = st.file_uploader("Upload Structure .txt File", type=["txt"])

# Drive and folder input
drive_letter = st.selectbox("Select Drive Letter", ["C", "D", "E"])
root_folder = st.text_input("Enter Root Folder Name", "prompt_to_planet")

if st.button("🚀 Generate Structure"):
    if uploaded_file and root_folder:
        # Read file
        raw_text = uploaded_file.read().decode("utf-8")
        structure_paths = parse_structure(raw_text)

        # Create base path
        base_path = os.path.join(f"{drive_letter}:/", root_folder)
        try:
            create_structure(base_path, structure_paths)
            st.success(f"✅ Structure created at {base_path}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please upload a file and enter root folder name.")







# .venv\Scripts\activate
# streamlit run streamlit_app.py