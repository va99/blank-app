import streamlit as st
import pandas as pd

# Sample data
data = {
    'Facility Name': ['Facility A', 'Facility B', 'Facility C', 'Facility D'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Insurance Policy': ['Policy X', 'Policy Y', 'Policy X', 'Policy Z'],
    'Em-panelled TPAs': ['TPA 1, TPA 2', 'TPA 3', 'TPA 1, TPA 4', 'TPA 2, TPA 5']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Doctor Admin Dashboard')
# Search form
st.sidebar.header('Search Criteria')
city = st.sidebar.selectbox('Select City', options=df['City'].unique())
policy = st.sidebar.selectbox('Select Insurance Policy', options=df['Insurance Policy'].unique())

# Filter data based on user input
filtered_df = df[(df['City'] == city) & (df['Insurance Policy'] == policy)]

# Display the filtered results
st.write(f'Search Results for City: {city} and Insurance Policy: {policy}')
st.dataframe(filtered_df)

# Display details of em-panelled TPAs
if not filtered_df.empty:
    st.write('Em-panelled TPAs at the selected facility:')
    for index, row in filtered_df.iterrows():
        st.write(f"**Facility Name:** {row['Facility Name']}")
        st.write(f"**Em-panelled TPAs:** {row['Em-panelled TPAs']}")
else:
    st.write('No facilities found matching the criteria.')