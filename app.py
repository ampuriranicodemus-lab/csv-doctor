import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="CSV Data Doctor", page_icon="🩺")
st.title("🩺 CSV Data Doctor")
st.write("Upload a messy CSV file, and I will clean it and give you a quick summary!")

# File Uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # 1. Load Data
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # 2. Show Raw Data
    st.subheader("1. Raw Data Preview (First 5 rows)")
    st.dataframe(df.head())

    # 3. Data Profiling (The "Summary")
    st.subheader("2. Data Health Report")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", len(df))
    col2.metric("Total Columns", len(df.columns))
    
    # Count missing values
    total_missing = df.isnull().sum().sum()
    col3.metric("Missing Values", total_missing)

    with st.expander("View Missing Values by Column"):
        st.write(df.isnull().sum())

    # 4. Cleaning Options
    st.subheader("3. Cleaning Steps")
    
    clean_duplicates = st.checkbox("Remove duplicate rows", value=True)
    clean_missing = st.checkbox("Fill missing values (or drop rows)", value=True)
    
    if st.button("Clean My Data!"):
        cleaned_df = df.copy()
        
        # Execute Cleaning
        if clean_duplicates:
            cleaned_df = cleaned_df.drop_duplicates()
        
        if clean_missing:
            # For this free tool, we fill numbers with 0 and text with "Unknown"
            numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
            text_cols = cleaned_df.select_dtypes(exclude=[np.number]).columns
            
            cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(0)
            cleaned_df[text_cols] = cleaned_df[text_cols].fillna("Unknown")

        st.success("Data cleaned successfully!")
        
        # 5. Show Cleaned Data
        st.subheader("4. Cleaned Data Preview")
        st.dataframe(cleaned_df.head())
        
        # 6. Download Button
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv,
            file_name='cleaned_data.csv',
            mime='text/csv',
        )
