# csv-doctor
An interactive Streamlit web app that automatically cleans, profiles, and formats messy CSV datasets using Python and Pandas. Built as a zero-cost data utility tool.
# 🩺 CSV Data Doctor

**CSV Data Doctor** is a free, interactive web application built with **Python, Pandas, and Streamlit**. It solves a common problem for analysts and business owners: dealing with messy, incomplete, or unstructured CSV data.

Users can simply upload their raw dataset, and the app will instantly generate a health report, remove duplicates, handle missing values, and provide a clean file ready for analysis.

## 🚀 Live Demo
👉 **[https://csv-doctor-for-csv-files.streamlit.app/]** *(e.g., https://csv-data-doctor.streamlit.app)*

## ✨ Features

- **Instant Data Profiling:** View total rows, total columns, and the exact count of missing values across the dataset.
- **Automated Cleaning:** One-click removal of duplicate rows.
- **Smart Missing Value Handling:** Automatically fills numeric columns with `0` and text columns with `"Unknown"`.
- **Data Preview:** Side-by-side comparison of your raw data and your cleaned data.
- **Instant Download:** Export the cleaned dataset back to your computer as a fresh CSV file.

## 🛠️ Tech Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **Data Manipulation:** Pandas, NumPy
- **Hosting:** Streamlit Community Cloud

## 💻 How to Run Locally

If you want to run this project on your own machine:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/csv-data-doctor.git
