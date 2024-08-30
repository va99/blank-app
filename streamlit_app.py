import streamlit as st
import pandas as pd

# Sample facility data with hospitals and their empanelled TPAs
facility_data = {
    'Facility Name': ['Facility A', 'Facility B', 'Facility C', 'Facility D'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Empanelled TPAs': [
        ['01', '02', '03'],  # Facility A
        ['04', '05'],         # Facility B
        ['06', '07', '08'],   # Facility C
        ['09', '10']          # Facility D
    ]
}

# TPA data
tpa_data = {
    "Empanelled Tie-Ups": [
        {"ID": "01", "Name": "Alankit Healthcare TPA Limited"},
        {"ID": "02", "Name": "Apollo Munich Health Insurance Co. Ltd."},
        {"ID": "03", "Name": "Aditya Birla Health Insurance company Ltd."},
        {"ID": "04", "Name": "Bajaj Allianz General Insurance Company Ltd."},
        {"ID": "05", "Name": "Chola Mandalam MS General Insurance Co. Ltd."},
        {"ID": "06", "Name": "East West Assist Private Limited"},
        {"ID": "07", "Name": "Ericson TPA Healthcare Pvt. Ltd."},
        {"ID": "08", "Name": "Family Health Plan (TPA) Ltd."},
        {"ID": "09", "Name": "Future Generali India Insurance Co. Ltd."},
        {"ID": "10", "Name": "Genins India TPA Limited"},
        {"ID": "11", "Name": "Good Health TPA Services Ltd."},
        {"ID": "12", "Name": "HDFC Ergo General Insurance Co. Ltd."},
        {"ID": "13", "Name": "Health India TPA Services Pvt. Ltd."},
        {"ID": "14", "Name": "Heritage Health TPA Pvt. Ltd."},
        {"ID": "15", "Name": "ICICI Lombard General Insurance Co. Ltd."},
        {"ID": "16", "Name": "ICICI Prudential Life Insurance Co. Ltd."},
        {"ID": "17", "Name": "IFFCO Tokio General Insurance Co. Ltd."},
        {"ID": "18", "Name": "MAGMA HDI General Insurance Company Limited"},
        {"ID": "19", "Name": "Manipal Cigna Health Insurance Co. Ltd."},
        {"ID": "20", "Name": "Max Bupa Health Insurance Company Ltd."},
        {"ID": "21", "Name": "MD India Healthcare Services (TPA) Pvt. Ltd."},
        {"ID": "22", "Name": "Medi Assist India TPA Pvt. Ltd."},
        {"ID": "23", "Name": "Medsave Healthcare TPA Ltd."},
        {"ID": "24", "Name": "Paramount Health Services (TPA) Pvt. Ltd."},
        {"ID": "25", "Name": "Park Mediclaim TPA Pvt. Ltd."},
        {"ID": "26", "Name": "Raksha TPA Pvt. Ltd."},
        {"ID": "27", "Name": "Reliance General Insurance Co. Ltd."},
        {"ID": "28", "Name": "Religare Health Insurance Co. Ltd."},
        {"ID": "29", "Name": "Safeway TPA Services Pvt. Ltd."},
        {"ID": "30", "Name": "Star Health & Allied Insurance Co. Ltd."},
        {"ID": "31", "Name": "Tata AIG General Insurance Company"},
        {"ID": "32", "Name": "United Healthcare Parekh TPA Pvt. Ltd."},
        {"ID": "33", "Name": "Universal Sompo General Insurance Co. Ltd."},
        {"ID": "34", "Name": "Vidal Health TPA Pvt. Ltd."},
        {"ID": "35", "Name": "Vipul Medcorp TPA Pvt. Ltd."},
        {"ID": "36", "Name": "Health Insurance TPA of India Limited"}
    ]
}

# Convert facility data to DataFrame
df = pd.DataFrame(facility_data)

# Convert TPA data to DataFrame
tpa_df = pd.DataFrame(tpa_data['Empanelled Tie-Ups'])

# Function to get TPA names based on IDs
def get_tpa_name_by_id(tpa_id):
    return tpa_df[tpa_df['ID'] == tpa_id]['Name'].values[0]

# Streamlit app
st.title('Doctor Admin Dashboard')

# Search form
st.sidebar.header('Search Criteria')
city = st.sidebar.selectbox('Select City', options=df['City'].unique())
tpa_name = st.sidebar.selectbox('Select TPA', options=tpa_df['Name'])

# Get TPA ID based on selected TPA Name
selected_tpa_id = tpa_df[tpa_df['Name'] == tpa_name]['ID'].values[0]

# Filter data based on user input
filtered_df = df[(df['City'] == city) & (df['Empanelled TPAs'].apply(lambda x: selected_tpa_id in x))]

# Display the filtered results
st.write(f'Search Results for City: {city} and TPA: {tpa_name}')
if not filtered_df.empty:
    st.dataframe(filtered_df[['Facility Name', 'City']])
    st.write('Facilities with the selected TPA:')
    for index, row in filtered_df.iterrows():
        st.write(f"**Facility Name:** {row['Facility Name']}")
        empanelled_tpas = [get_tpa_name_by_id(tpa_id) for tpa_id in row['Empanelled TPAs']]
        st.write(f"**Empanelled TPAs:** {', '.join(empanelled_tpas)}")
else:
    st.write('No facilities found matching the criteria.')