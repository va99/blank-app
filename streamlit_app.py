import streamlit as st

# Mock TPA data
tpa_data = {
    "01": "Medi Assist",
    "02": "Paramount Health Services",
    "03": "FHPL (Family Health Plan Limited)",
    "04": "Health India TPA",
    "05": "Star Health",
    "06": "Apollo Munich",
    "07": "ICICI Lombard",
    "08": "UnitedHealthcare",
    "09": "Religare Health Insurance",
    "10": "HDFC ERGO",
    "11": "Max Bupa Health Insurance",
    "12": "SBI Health Insurance",
    "13": "New India Assurance",
    "14": "Oriental Insurance",
    "15": "National Insurance",
    "16": "United India Insurance",
    "17": "IFFCO Tokio",
    "18": "Cholamandalam MS General Insurance",
    "19": "Bajaj Allianz",
    "20": "Reliance General Insurance"
}

# Mock hospital data for one hospital
hospital_data = {
    "Hospital ID": "H001",
    "Name": "Max Super Specialty Hospital, Saket",
    "City": "New Delhi",
    "State": "Delhi",
    "Empanelled Tie-Ups": [
        {"TPA": "01", "Coverage": "cashless"},
        {"TPA": "02", "Coverage": "cashless"},
        {"TPA": "03", "Coverage": "cashless"},
        {"TPA": "04", "Coverage": "cashless"},
        {"TPA": "05", "Coverage": "cashless"},
        {"TPA": "06", "Coverage": "cashless"},
        {"TPA": "07", "Coverage": "cashless"},
        {"TPA": "08", "Coverage": "cashless"},
        {"TPA": "09", "Coverage": "cashless"},
        {"TPA": "10", "Coverage": "cashless"},
        {"TPA": "11", "Coverage": "cashless"},
        {"TPA": "12", "Coverage": "cashless"},
        {"TPA": "13", "Coverage": "cashless"},
        {"TPA": "14", "Coverage": "cashless"},
        {"TPA": "15", "Coverage": "cashless"},
        {"TPA": "16", "Coverage": "cashless"},
        {"TPA": "17", "Coverage": "cashless"},
        {"TPA": "18", "Coverage": "cashless"},
        {"TPA": "19", "Coverage": "cashless"},
        {"TPA": "20", "Coverage": "cashless"}
    ]
}
{
        "Hospital ID": "H002",
        "Name": "Lilavati Hospital, Mumbai",
        "City": "Mumbai, Maharashtra",
        "State": "Maharashtra",
        "Empanelled Tie-Ups": [
            {"TPA": "03", "Coverage": "cashless"},
            {"TPA": "04", "Coverage": "cashless"},
            {"TPA": "05", "Coverage": "cashless"},
            {"TPA": "06", "Coverage": "cashless"},
            {"TPA": "07", "Coverage": "cashless"},
            {"TPA": "08", "Coverage": "cashless"},
            {"TPA": "09", "Coverage": "cashless"},
            {"TPA": "10", "Coverage": "cashless"},
            {"TPA": "11", "Coverage": "cashless"},
            {"TPA": "12", "Coverage": "cashless"},
            {"TPA": "13", "Coverage": "cashless"},
            {"TPA": "14", "Coverage": "cashless"},
            {"TPA": "15", "Coverage": "cashless"},
            {"TPA": "16", "Coverage": "cashless"},
            {"TPA": "17", "Coverage": "cashless"},
            {"TPA": "18", "Coverage": "cashless"},
            {"TPA": "19", "Coverage": "cashless"},
            {"TPA": "20", "Coverage": "cashless"},
            {"TPA": "21", "Coverage": "cashless"},
            {"TPA": "22", "Coverage": "cashless"}

     ]
}
{
        "Hospital ID": "H003",
        "Name": "Narayana Health, Bengaluru",
        "City": "Bengaluru",
        “State": "Karnataka"
        "Empanelled Tie-Ups": [
            {"TPA": "05", "Coverage": "cashless"},
            {"TPA": "06", "Coverage": "cashless"},
            {"TPA": "07", "Coverage": "cashless"},
            {"TPA": "08", "Coverage": "cashless"},
            {"TPA": "09", "Coverage": "cashless"},
            {"TPA": "10", "Coverage": "cashless"},
            {"TPA": "11", "Coverage": "cashless"},
            {"TPA": "12", "Coverage": "cashless"},
            {"TPA": "13", "Coverage": "cashless"},
            {"TPA": "14", "Coverage": "cashless"},
            {"TPA": "15", "Coverage": "cashless"},
            {"TPA": "16", "Coverage": "cashless"},
            {"TPA": "17", "Coverage": "cashless"},
            {"TPA": "18", "Coverage": "cashless"},
            {"TPA": "19", "Coverage": "cashless"},
            {"TPA": "20", "Coverage": "cashless"},
            {"TPA": "21", "Coverage": "cashless"},
            {"TPA": "22", "Coverage": "cashless"},
            {"TPA": "23", "Coverage": "cashless"},
            {"TPA": "24", "Coverage": "cashless"}
        ]
    },
    {
        "Hospital ID": "H004",
        "Name": "Medanta - The Medicity",
        "City": "Gurgaon",
        "State": "Haryana",
        "Empanelled Tie-Ups": [
            {"TPA": "07", "Coverage": "cashless"},
            {"TPA": "08", "Coverage": "cashless"},
            {"TPA": "09", "Coverage": "cashless"},
            {"TPA": "10", "Coverage": "cashless"},
            {"TPA": "11", "Coverage": "cashless"},
            {"TPA": "12", "Coverage": "cashless"},
            {"TPA": "13", "Coverage": "cashless"},
            {"TPA": "14", "Coverage": "cashless"},
            {"TPA": "15", "Coverage": "cashless"},
            {"TPA": "16", "Coverage": "cashless"},
            {"TPA": "17", "Coverage": "cashless"},
            {"TPA": "18", "Coverage": "cashless"},
            {"TPA": "19", "Coverage": "cashless"},
            {"TPA": "20", "Coverage": "cashless"},
            {"TPA": "21", "Coverage": "cashless"},
            {"TPA": "22", "Coverage": "cashless"},
            {"TPA": "23", "Coverage": "cashless"},
            {"TPA": "24", "Coverage": "cashless"},
            {"TPA": "25", "Coverage": "cashless"},
            {"TPA": "26", "Coverage": "cashless"}
        ]
    },
    {
        "Hospital ID": "H005",
        "Name": "Bansal Hospital",
        "City": "Bhopal",
        "State": "Madhya Pradesh",
        "Empanelled Tie-Ups": [
            {"TPA": "03", "Coverage": "cashless"},
            {"TPA": "04", "Coverage": "cashless"},
            {"TPA": "19", "Coverage": "cashless"},
            {"TPA": "33", "Coverage": "cashless"},
            {"TPA": "34", "Coverage": "cashless"},
            {"TPA": "35", "Coverage": "cashless"},
            {"TPA": "11", "Coverage": "cashless"},
            {"TPA": "27", "Coverage": "cashless"},
            {"TPA": "09", "Coverage": "cashless"},
            {"TPA": "15", "Coverage": "cashless"}
        ]
    },
}


# Streamlit app
st.title("Hospital TPA Information")

# Sidebar for selecting city and TPA
with st.sidebar:
    city_selected = st.selectbox("Select a City", ["New Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Pune", "Ahemdabad", "Jaipur", "Lucknow", "Bhopal", "Indore", "Nagpur", "Kochi"])
    tpa_ids = [tie_up['TPA'] for tie_up in hospital_data["Empanelled Tie-Ups"]]
    selected_tpa = st.selectbox("Select a TPA", tpa_ids, format_func=lambda x: tpa_data[x])

# Toggle switch for coverage type
coverage_type = st.radio("Coverage Type", options=["Cashless", "Non-Cashless"], index=0, horizontal=True)

# Display hospital information if the city matches
if hospital_data["City"] == city_selected:
    st.header(hospital_data["Name"])
    st.subheader(f"Location: {hospital_data['City']}, {hospital_data['State']}")
    
    # Filter based on the coverage type
    selected_coverage = "cashless" if coverage_type == "Cashless" else "non-cashless"
    tie_up = next((tie_up for tie_up in hospital_data["Empanelled Tie-Ups"] if tie_up["TPA"] == selected_tpa and tie_up["Coverage"] == selected_coverage), None)
    
    if tie_up:
        st.subheader("Empanelled TPA Details")
        st.write(f"TPA: {tpa_data[selected_tpa]}")
    else:
        st.write(f"This hospital does not offer {coverage_type.lower()} coverage with {tpa_data[selected_tpa]}.")