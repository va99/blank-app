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

#Mock Hospital Data
hospital_data = {
    "H001": {
        "Name": "Max Super Specialty Hospital, Saket",
        "Location": {
            "City": "New Delhi",
            "State": "Delhi"
        },
        "Empanelled Tie-Ups": {
            "cashless": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", 
                         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        }
    },
    "H002": {
        "Name": "Lilavati Hospital, Mumbai",
        "Location": {
            "City": "Mumbai",
            "State": "Maharashtra"
        },
        "Empanelled Tie-Ups": {
            "cashless": ["03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
                         "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
        }
    },
    "H004": {
        "Name": "Medanta - The Medicity",
        "Location": {
            "City": "Gurgaon",
            "State": "Haryana"
        },
        "Empanelled Tie-Ups": {
            "cashless": ["07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
                         "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
        }
    },
    "H005": {
        "Name": "Bansal Hospital",
        "Location": {
            "City": "Bhopal",
            "State": "Madhya Pradesh"
        },
        "Empanelled Tie-Ups": {
            "cashless": ["03", "04", "19", "33", "34", "35", "11", "27", "09", "15"]
        }
    }
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