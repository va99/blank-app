import streamlit as st
import pandas as pd

# Mock-up data
data = {
    'Hospital Name': ['City Hospital', 'Central Clinic', 'Wellness Center', 'Care Hospital', 'Metro Medical'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Empanelled TPAs': ['TPA A, TPA B, TPA C', 'TPA B, TPA D', 'TPA A, TPA C', 'TPA B, TPA C, TPA D', 'TPA A, TPA D'],
    'PPN': [True, True, False, True, False],
    'NON-PPN': [False, True, True, False, True]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Doctor Admin Dashboard')

# Search form
st.sidebar.header('Search Criteria')
city = st.sidebar.selectbox('Select City', options=[''] + list(df['City'].unique()))
tpa = st.sidebar.selectbox('Select Insurance TPA', options=[''] + list(set(','.join(df['Empanelled TPAs']).replace(' ', '').split(','))))

# PPN Toggle
ppn_status = st.sidebar.toggle('PPN Coverage', value=True)

# Filter data based on user input
if city:
    df = df[df['City'] == city]
if tpa:
    df = df[df['Empanelled TPAs'].str.contains(tpa)]
if ppn_status:
    df = df[df['PPN'] == True]
else:
    df = df[df['NON-PPN'] == True]

# Display the filtered results
st.subheader(f"HOSPITALS IN {city or 'ALL CITIES'} WHO HAVE EMPANELLED {tpa or 'ANY TPA'}")
st.subheader(f"THROUGH {'PPN' if ppn_status else 'NON-PPN'} COVERAGE")

if not df.empty:
    for _, row in df.iterrows():
        st.write(f"**Hospital Name:** {row['Hospital Name']}")
        st.write(f"**City:** {row['City']}")
        st.write(f"**Empanelled TPAs:** {row['Empanelled TPAs']}")
        st.write(f"**Coverage:** {'PPN' if ppn_status else 'NON-PPN'}")
        st.write("---")
else:
    st.write('No hospitals found matching the criteria.')

# Display the full dataset (optional, for demonstration purposes)
st.sidebar.subheader("Full Dataset (for reference)")
st.sidebar.dataframe(data)