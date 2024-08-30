import streamlit as st

# Mock TPA data
tpa_data = {
    "01": "Medi Assist",
    "02": "Paramount Health Services",
    "03": "FHPL (Family Health Plan Limited",
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

# Mock Hospital Data
hospital_data = {
    "H001": {
        "Name": "Max Super Specialty Hospital",
        "Location": {
            "City": "New Delhi",
            "State": "Delhi"
        },
        "Rating": 4.5,
        "Empanelled Tie-Ups": {
            "cashless": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", 
                         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        },
        "Description": "A leading multi-specialty hospital with cutting-edge technology and a team of experienced doctors."
    },
    "H002": {
        "Name": "Lilavati Hospital",
        "Location": {
            "City": "Mumbai",
            "State": "Maharashtra"
        },
        "Rating": 4.3,
        "Empanelled Tie-Ups": {
            "cashless": ["03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
                         "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
        },
        "Description": "A well-known hospital offering comprehensive healthcare services in Mumbai."
    },
    "H004": {
        "Name": "Medanta - The Medicity",
        "Location": {
            "City": "Gurgaon",
            "State": "Haryana"
        },
        "Rating": 4.7,
        "Empanelled Tie-Ups": {
            "cashless": ["07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
                         "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
        },
        "Description": "A super-specialty hospital known for world-class treatment and modern facilities."
    },
    "H005": {
        "Name": "Bansal Hospital",
        "Location": {
            "City": "Bhopal",
            "State": "Madhya Pradesh"
        },
        "Rating": 4.1,
        "Empanelled Tie-Ups": {
            "cashless": ["03", "04", "19", "33", "34", "35", "11", "27", "09", "15"]
        },
        "Description": "A reliable healthcare provider in Bhopal with a focus on patient care and satisfaction."
    }
}

# Streamlit app
st.title("MedLeads")

# Doctor Registration Form
if 'doctor_name' not in st.session_state:
    st.subheader("Doctor Registration Form")
    with st.form("doctor_registration"):
        doctor_name = st.text_input("Doctor Name")
        email = st.text_input("Email")
        mobile_number = st.text_input("Mobile Number")
        license_id = st.text_input("License ID")
        specialty = st.text_input("Specialty")
        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            st.session_state.doctor_name = doctor_name
            st.session_state.email = email
            st.session_state.mobile_number = mobile_number
            st.session_state.license_id = license_id
            st.session_state.specialty = specialty
            st.experimental_rerun()
else:
    st.header(f"Hello {st.session_state.doctor_name}")

    # Sidebar for selecting city and TPA
    with st.sidebar:
        city_selected = st.selectbox(
            "Select a City",
            ["New Delhi", "Mumbai", "Gurgaon", "Bhopal"]
        )
        
        # Filter TPAs based on hospitals in the selected city
        available_tpas = set()
        for hospital in hospital_data.values():
            if hospital["Location"]["City"] == city_selected:
                available_tpas.update(hospital["Empanelled Tie-Ups"]["cashless"])
        
        selected_tpa = st.selectbox(
            "Select a TPA",
            list(available_tpas),
            format_func=lambda x: tpa_data.get(x, "Unknown TPA")
        )

    # Switch-type toggle for coverage type
    coverage_type = st.checkbox("Cashless Coverage", value=True)

    # Display hospital information based on city and TPA selection
    for hospital_id, hospital in hospital_data.items():
        if hospital["Location"]["City"] == city_selected:
            # Creating a placeholder with hospital name and rating
            with st.expander(f"{hospital['Name']} - {hospital['Rating']}⭐"):
                st.write(f"Location: {hospital['Location']['City']}, {hospital['Location']['State']}")
                
                selected_coverage = "cashless" if coverage_type else "non-cashless"
                
                if selected_coverage in hospital["Empanelled Tie-Ups"] and selected_tpa in hospital["Empanelled Tie-Ups"][selected_coverage]:
                    st.write(hospital["Description"])
                    if st.button(f"Refer Patient to {hospital['Name']}", key=hospital_id):
                        # When Refer Patient is clicked, show the patient info form
                        with st.form(f"patient_form_{hospital_id}", clear_on_submit=True):
                            st.write("### Patient Information")
                            patient_name = st.text_input("Patient Name")
                            patient_age = st.number_input("Age", min_value=0, max_value=120)
                            patient_mobile = st.text_input("Mobile Number")
                            insurance_partner = st.selectbox(
                                "Insurance Partner", 
                                [tpa_data.get(tpa) for tpa in hospital["Empanelled Tie-Ups"][selected_coverage]],
                                index=[tpa_data.get(tpa) for tpa in hospital["Empanelled Tie-Ups"][selected_coverage]].index(tpa_data.get(selected_tpa))
                            )
                            referred_by = f"Referred By: {st.session_state.doctor_name}"
                            st.write(referred_by)
                            submit_button = st.form_submit_button(label="Submit")
                            if submit_button:
                                st.success("Patient referral submitted successfully.")
                else:
                    st.write(f"This hospital does not offer {selected_coverage.replace('-', ' ')} coverage with {tpa_data[selected_tpa]}.")
                    # Provide a "Refer Patient" button even for non-cashless coverage
                    if st.button(f"Refer Patient to {hospital['Name']}", key=f"non_{hospital_id}"):
                        # Show the patient info form for non-cashless with "Payment Mode: CASH"
                        with st.form(f"patient_form_non_{hospital_id}", clear_on_submit=True):
                            st.write("### Patient Information")
                            patient_name = st.text_input("Patient Name")
                            patient_age = st.number_input("Age", min_value=0, max_value=120)
                            patient_mobile = st.text_input("Mobile Number")
                            payment_mode = "CASH"  # Payment mode is pre-set to "CASH" for non-cashless
                            st.write(f"Payment Mode: {payment_mode}")
                            referred_by = f"Referred By: {st.session_state.doctor_name}"
                            st.write(referred_by)
                            submit_button = st.form_submit_button(label="Submit")
                            if submit_button:
                                st.success("Patient referral submitted successfully.")