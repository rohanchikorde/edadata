import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load your dataset
df = pd.read_csv('data1.csv')

# Sidebar section for selecting the visualization and analysis
st.sidebar.title('Select Visualization and Analysis')
visualization = st.sidebar.selectbox('Choose a visualization', ('Histogram', 'Boxplot'))
analysis = st.sidebar.selectbox('Choose an analysis', ('Summary Statistics', 'Value Counts'))

# Main section for displaying the selected visualization and analysis
st.title('Data Analysis and Visualization')

if visualization == 'Histogram':
    # Display a histogram
    st.header('Histogram')
    column_to_plot = st.selectbox('Select a column for the histogram', df.columns)
    
    # Calculate descriptive statistics
    column_stats = df[column_to_plot].describe()
    st.subheader('Descriptive Statistics')
    st.write(column_stats)
    
    # Plot histogram
    plt.hist(df[column_to_plot])
    plt.xlabel(column_to_plot)
    plt.ylabel('Frequency')
    st.pyplot()

elif visualization == 'Boxplot':
    # Display a boxplot
    st.header('Boxplot')
    column_to_plot = st.selectbox('Select a column for the boxplot', df.columns)
    
    # Calculate descriptive statistics
    column_stats = df[column_to_plot].describe()
    st.subheader('Descriptive Statistics')
    st.write(column_stats)
    
    # Plot boxplot
    sns.boxplot(data=df[column_to_plot])
    plt.xlabel(column_to_plot)
    plt.ylabel('Value')
    st.pyplot()

if analysis == 'Summary Statistics':
    # Display summary statistics
    st.header('Summary Statistics')
    summary_stats = df.describe()
    st.write(summary_stats)

elif analysis == 'Value Counts':
    # Display value counts for a column
    st.header('Value Counts')
    column_to_analyze = st.selectbox('Select a column for value counts', df.columns)
    value_counts = df[column_to_analyze].value_counts()
    st.write(value_counts)
