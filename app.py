import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration (MUST BE FIRST)
st.set_page_config(page_title="CSV Data Doctor", page_icon="🩺", layout="wide")

# 2. Custom CSS for a beautiful background and styling
st.markdown("""
    <style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    /* Style the headers */
    h1, h2, h3 {
        color: #2c3e50;
    }
    /* Style the upload box */
    .stFileUploader {
        border: 2px dashed #4CAF50;
        border-radius: 10px;
        padding: 20px;
        background-color: white;
    }
    /* Style the primary buttons */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Section
st.title("🩺 CSV Data Doctor")
st.markdown("### *Your automated data cleaning assistant*")
st.write("Upload a messy CSV file, and I will clean it, profile it, and give it back to you in seconds. **No coding required.**")
st.divider()

# 4. File Uploader
uploaded_file = st.file_uploader("📂 Drop your messy CSV file here", type=["csv"])

if uploaded_file is not None:
    # 5. Load Data
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # 6. Data Health Dashboard (Using Columns for a clean look)
    st.subheader("📊 Data Health Report")
    col1, col2, col3 = st.columns(3)
    
    # Calculate metrics
    total_rows = len(df)
    total_cols = len(df.columns)
    total_missing = df.isnull().sum().sum()
    
    # Display metrics with nice styling
    col1.metric("Total Rows", f"{total_rows:,}")
    col2.metric("Total Columns", f"{total_cols:,}")
    col3.metric("Missing Values", f"{total_missing:,}", delta=f"-{total_missing}" if total_missing > 0 else "0", delta_color="inverse")

    with st.expander("🔍 View Raw Data Preview"):
        st.dataframe(df.head(10), use_container_width=True)

    st.divider()

    # 7. Cleaning Section
    st.subheader("🧹 Clean Your Data")
    
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        clean_duplicates = st.checkbox("✨ Remove duplicate rows", value=True)
    with col_opt2:
        clean_missing = st.checkbox("🩹 Fill missing values (Numbers=0, Text=Unknown)", value=True)
    
    if st.button("🚀 Clean My Data Now!"):
        cleaned_df = df.copy()
        
        # Execute Cleaning
        if clean_duplicates:
            cleaned_df = cleaned_df.drop_duplicates()
        
        if clean_missing:
            numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
            text_cols = cleaned_df.select_dtypes(exclude=[np.number]).columns
            cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(0)
            cleaned_df[text_cols] = cleaned_df[text_cols].fillna("Unknown")

        # MAGIC HAPPENS HERE: CELEBRATION!
        st.balloons()
        st.success("🎉 Data cleaned successfully! Your dataset is now healthy.")
        
        # Show Cleaned Data
        st.subheader("✨ Cleaned Data Preview")
        st.dataframe(cleaned_df.head(10), use_container_width=True)
        
        # Download Button
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv,
            file_name='cleaned_data.csv',
            mime='text/csv',
        )

# 8. Footer
st.markdown("---")
st.caption("Built with ❤️ using Python, Pandas, and Streamlit by Ampurira Nicodemus.")
