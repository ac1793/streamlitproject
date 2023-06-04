import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write('reading file as bytes')

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write('Converting to a string based IO')

    # To read file as string:
    string_data = stringio.read()
    st.write("reading file as string")

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write('Thanks for the dataframe!')

    option = st.selectbox(
    'How would you like to be contacted?',
    dataframe.columns)

    st.write('You selected:', option)

    if dataframe[option].dtype == 'object':
        proportions = dataframe[option].value_counts(normalize=True) * 100
        formatted_proportions = proportions.apply(lambda x: '{:.2f}%'.format(x))

        st.write(formatted_proportions)
        fig, ax = plt.subplots()
        ax.bar(proportions.index, proportions.values)
        ax.set_xlabel(option)
        ax.set_ylabel('Proportions')
        ax.set_title('Proportions of Categories')
        st.pyplot(fig)

    else:
        st.write(dataframe[option].describe())
        
        fig, ax = plt.subplots()
        sns.histplot(dataframe[option], ax=ax, kde=True)
        ax.set_xlabel('Value')
        ax.set_ylabel('Density')
        ax.set_title('Distribution Plot')
        st.pyplot(fig)