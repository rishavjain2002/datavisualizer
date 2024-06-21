import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title= " Data Visualiser" ,
                   layout= "centered",
                   page_icon= "📊"
                   )


st.title("📊  Data Visualiser")

df = st.file_uploader(label= 'Upload your dataset: ')

if df:
    df = pd.read_csv(df)
    
    feature_columns = df.columns.tolist()

    st.write("")
    st.write(df.head())
    
    object_type = df.select_dtypes(include = ['object']).columns.tolist()
    numeric_type = df.select_dtypes(include= ['int64','int32']).columns.tolist()
    
    st.write("---")
    with st.container():
        st.markdown("<h2 style='text-align: center'>Feature Types</h2>", unsafe_allow_html=True)
    
    # Nested container for the columns
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Categorical Feature")
            for col in object_type:
                st.write(f"- {col}")

        with col2:
            st.subheader("Numerical Feature")
            for col in numeric_type:
                    st.write(f"- {col}")
            
    
    
    st.write("---")
    
    x_axis = st.selectbox("Select the X_axis", options = feature_columns + ["None"], index = None)
    y_axis = st.selectbox("Select the Y_axis", options = feature_columns + ["None"], index = None)
        
    plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot", "Count Plot"]
    plot = st.selectbox("Select a Visualisation" , options= plot_list, index= None)
    
    
    
    
    
    
    
    if st.button("Generate Plot"):
        fig, ax = plt.subplots(figsize =(6,4))
        
        if plot == "Line PLot":
            sns.lineplot(x = df[x_axis], y = df[y_axis], ax = ax)
        elif plot == "Bar Chart":
            sns.barplot(x = df[x_axis], y = df[y_axis], ax = ax)
        elif plot == "Scatter Plot":
            sns.scatterplot(x = df[x_axis], y = df[y_axis], ax = ax)
        elif plot == "Distribution Plot":
            sns.histplot(x = df[x_axis],kde= True ,ax = ax)
        elif plot == "Count Plot":
            sns.countplot(x = df[x_axis],ax = ax)
            
        
        st.pyplot(fig)
            
        
    # st.write(df['Units Sold'].groupby(df['Product Category']).value_counts().reset_index())