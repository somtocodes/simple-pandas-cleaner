import pandas
import streamlit as st
from cleaner import auto_clean

st.set_page_config(page_title="Web Data Cleaner", layout = "centered")
st.title("Data Cleaner")
st.write("Upload a messy CSV or Excel file, and i'll clean it for you automatically")

uploaded_file = st.file_uploader("Upload a .csv or .xlsx file", type=['csv', 'xlsx'])

if uploaded_file is not None:
  try:
    if uploaded_file.name.endswith('.csv'):
      df = pandas.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
      df = pandas.read_excel(uploaded_file)
    else:
      st.error('Please upload a valid CSV or Excel file')
      st.stop()
  except Exception as e:
    st.error(f'Something went wrong while reading the file. Is it corrupted? Error: {e}')
    st.stop()
    
  st.subheader('Original Data')
  st.dataframe(df)
  
    
  if st.button('Clean data'):
    cleaned_df, report = auto_clean(df)
    st.success("Cleaning complete")
    st.subheader("Cleaned Data")
    st.dataframe(cleaned_df)
    csv = cleaned_df.to_csv(index=False).encode('utf-8')
    st.download_button(label='Download clean data',data=csv, file_name="Cleaned_data.csv", mime="text/csv")

      
