# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# st.set_page_config(page_config="Data Sweppar",layout="wide")


# st.markdown(
#     """
# <style>
# .stApp{
# background-color:black;
# color:white;
# text-align:center;
# justify-text:center;
# font-size:20px;
# color:white;
# font-family: 'Times New Roman', Times, serif;

# }
# </style>k
# """,unsafe_allow_html=True
# )

# # title and description
# st.title("Data Sweppar Striling Growth Intigration by Saad Qureshi") 
# st.write("Transform manage clean and re use your Visualization Perfectly")


# # upload files

# uploaded_files = st.file_uploader('📂 Upload your files (CSV or Excel):' ,type=["cvs","xlxs"],accept_multiple_files=(True))

# if uploaded_files :
#     for file in uploaded_files :
#         file_ext=os.path.splitext(file.name)[-1].lower()
#         if file_ext==".csv":
#             df=pd.read_csv(file)
#         elif file_ext==".xlxs":
#             df=pd.read_excel(file)
#         else:
#             st.error(f"Please Upload the correct file type {file_ext}")
#             continue


# # files details

# st.write("Preview Files On The Head Of Data-Frames")
# st.dataframe(df.head())


# # Data Cleaning Methods

# st.subheader("Data Cleaning Methods")
# if st.checkbox(f"Clean Data for {file.name}"):
#     col1 , col2 = st.columns(2)

#     with col1:
#         if st.button(f"Remove Duplicates From : {file.name}"):
#             df=df.drop_duplicates(inplace=(True))
#             st.write("Duplicates Removed ")

#     with col2:(f"Fill Missing Values:{file.name}")
#     numeric_cols = df.select_dtypes(include=['number']).columns
#     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#     st.write("Missing Values Has Been Filled")




# st.subheader("Select Columns To Keep Visualize")
# columns =st.multiselect(f"Choose Column For :{file.name}",df.columns,default=df.columns)
# df=df[columns]



# # data Visulize


# st.subheader("📈 Data Visualization")

# if st.checkbox("Data Visualization for :{file.name}"):
#     st.bar_chart(df.select_dtypes(include=['number']).iloc[:, :2])



# # conversion Options


# st.subheader("�� Conversion Options")
# conversion_type = st.radio(f"Convert {file.name} to :",["Cvs"  , "Excel"],key=file.name)

# if st.button(f"Convert {file.name}"):
#     buffer = BytesIO()
#     if conversion_type == "Cvs":
#         df.to_csv(buffer, index=False)
#         file_name = file.name.replace(file_ext , ".csv")
#         mime_type = "text/csv"

#     elif conversion_type == "Excel":
#         df.to.to_excel(buffer , index=False)
#         file_name = file.name.replace(file_ext , ".xlxs")
#         mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         buffer.seek(0)


#         st.download_button(
#             label=(f"Download {file.name} as {conversion_type}"),
#             data = buffer,
#             file_name=file_name,
#             mime=mime_type
#         )



import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweppar", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: white;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title and Description
st.title("📊 Data Sweppar - Streamlined Data Processing")
st.write("Effortlessly clean, transform, and visualize your data.")

# Upload Files
uploaded_files = st.file_uploader("📂 Upload your CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

dataframes = {}
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Invalid file type: {file_ext}")
            continue
        dataframes[file.name] = df

# Display Data Preview
if dataframes:
    st.subheader("📄 Data Preview")
    selected_file = st.selectbox("Choose a file to preview:", list(dataframes.keys()))
    st.dataframe(dataframes[selected_file].head())

    # Data Cleaning Options
    st.subheader("🛠 Data Cleaning")
    df = dataframes[selected_file]
    
    if st.button("Remove Duplicates"):
        df.drop_duplicates(inplace=True)
        st.success("✅ Duplicates removed!")

    if st.button("Fill Missing Values"):
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        st.success("✅ Missing values filled!")
    
    # Column Selection
    st.subheader("📌 Select Columns to Visualize")
    selected_columns = st.multiselect("Choose columns:", df.columns, default=df.columns)
    df = df[selected_columns]

    # Data Visualization
    st.subheader("📈 Data Visualization")
    if st.checkbox("Show Bar Chart"):
        st.bar_chart(df.select_dtypes(include=['number']))

    # File Conversion
    st.subheader("🔄 Convert & Download Data")
    conversion_type = st.radio("Convert file to:", ["CSV", "Excel"], key=selected_file)
    if st.button("Download File"):
        buffer = BytesIO()
        if conversion_type == "CSV":
            df.to_csv(buffer, index=False)
            file_name = selected_file.replace(file_ext, ".csv")
            mime_type = "text/csv"
        elif conversion_type == "Excel":
            df.to_excel(buffer, index=False)
            file_name = selected_file.replace(file_ext, ".xlsx")
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        buffer.seek(0)
        st.download_button(
            label=f"Download {conversion_type}",
            data=buffer,
            file_name=file_name,
            mime=mime_type
        )
        st.success("All files downloaded successfully")