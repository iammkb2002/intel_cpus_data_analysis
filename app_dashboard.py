import streamlit as st
import plotly.express as px
import pandas as pd
import cookbook

# Load the dataset
df = pd.read_csv('Intel_CPUs_cleaned.csv')

def dashboard_page():
    # Title
    st.title("Intel CPUs Dashboard")

    # Slider for Core Count range
    core_count_range = st.slider("Select a range for Core Count", 0, int(df['CoreCount'].max()), (0, int(df['CoreCount'].max())))

    # Filter the DataFrame based on the selected core count range
    filtered_df = df[(df['CoreCount'] >= core_count_range[0]) & (df['CoreCount'] <= core_count_range[1])]

    # Dropdown to select the chart
    selected_chart = st.selectbox("Select a Chart", ["All Charts", "Pie Chart", "Bar Chart", "Scatter Plot 1", "Scatter Plot 2", "Correlation Matrix", "Heatmap", "Box Plot"])

    # Check the selected chart and display accordingly
    if selected_chart == "All Charts" or selected_chart == "Pie Chart":
        # Create a pie chart
        desktop_count = filtered_df['Desktop'].sum()
        embedded_count = filtered_df['Embedded'].sum()
        mobile_count = filtered_df['Mobile'].sum()

        data = pd.DataFrame({
            'Type': ['Desktop', 'Embedded', 'Mobile'],
            'Count': [desktop_count, embedded_count, mobile_count]
        })

        st.plotly_chart(px.pie(data, values='Count', names='Type', title='Market Segmentation of Intel CPUs'))

    if selected_chart == "All Charts" or selected_chart == "Bar Chart":
        # Create a bar chart
        st.plotly_chart(px.histogram(filtered_df, x='CoreCount', title='Distribution of Core Counts in Intel CPUs'))

    if selected_chart == "All Charts" or selected_chart == "Scatter Plot 1":
        # Create a scatter plot
        st.plotly_chart(px.scatter(filtered_df, x='ClockSpeedMax', y='Price', title='Maximum Clock Speed vs Price'))

    if selected_chart == "All Charts" or selected_chart == "Scatter Plot 2":
        # Create another scatter plot
        st.plotly_chart(px.scatter(filtered_df, x='CoreCount', y='Price', title='Core Count vs Price'))

    if selected_chart == "All Charts" or selected_chart == "Heatmap":
        # Create a heatmap
        heatmap_data = filtered_df[['Price', 'CoreCount', 'ThreadCount']].corr()
        st.plotly_chart(px.imshow(heatmap_data, title='Heatmap of Price vs CoreCount and ThreadCount', color_continuous_scale='Viridis'))

    if selected_chart == "All Charts" or selected_chart == "Box Plot":
        # Create a box plot
        st.plotly_chart(px.box(filtered_df, x="Lithography", y="ClockSpeedMax", title='Distribution of Clock Speed Max by Lithography'))

    if st.button("Go to Cookbook"):
        st.session_state.runpage = 'cookbook'
        st.experimental_rerun()

if 'runpage' not in st.session_state:
    st.session_state.runpage = 'dashboard'

if st.session_state.runpage == 'dashboard':
    dashboard_page()
elif st.session_state.runpage == 'cookbook':
    cookbook.run()
