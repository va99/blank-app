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

# Mock hospital data
hospital_data = [
    {
        "hospital_name": "Paras Hospitals",
        "city": "Gurgaon",
        "address": "C-1, Sushant Lok-1, Sector-43, Phase-I, Gurgaon, Haryana - 122002",
        "contact_number": "+91 124 458 5555",
        "email": "info@parashospitals.com",
        "TPAs": ["09", "10", "11", "12", "13", "14", "15", "16", "17", "18"]
    },
    {
        "hospital_name": "Columbia Asia Hospital",
        "city": "Gurgaon",
        "address": "Block F, Sector 23A, Palam Vihar, Gurgaon, Haryana - 122017",
        "contact_number": "+91 124 616 5666",
        "email": "info@columbiaasia.com",
        "TPAs": ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
    },
    {
        "hospital_name": "Max Super Speciality Hospital",
        "city": "Gurgaon",
        "address": "B Block, Sushant Lok I, Sector 43, Gurgaon, Haryana - 122001",
        "contact_number": "+91 124 662 3000",
        "email": "info@maxhealthcare.com",
        "TPAs": ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    },
    {
        "hospital_name": "Apollo Hospitals",
        "city": "Chennai",
        "address": "21, Greams Lane, Off Greams Road, Chennai - 600006",
        "contact_number": "+91 44 2829 0200",
        "email": "info@apollohospitals.com",
        "TPAs": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
    },
    {
        "hospital_name": "Fortis Malar Hospital",
        "city": "Chennai",
        "address": "52, 1st Main Road, Gandhi Nagar, Adyar, Chennai - 600020",
        "contact_number": "+91 44 4289 2222",
        "email": "info@fortishealthcare.com",
        "TPAs": ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
    },
    {
        "hospital_name": "MIOT International",
        "city": "Chennai",
        "address": "4/112, Mount Poonamalle High Road, Manapakkam, Chennai - 600089",
        "contact_number": "+91 44 4200 2288",
        "email": "info@miothospitals.com",
        "TPAs": ["03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    },
    {
        "hospital_name": "Sri Ramachandra Medical Centre",
        "city": "Chennai",
        "address": "No.1 Ramachandra Nagar, Porur, Chennai - 600116",
        "contact_number": "+91 44 4592 8500",
        "email": "info@sriramachandra.edu.in",
        "TPAs": ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
    },
    {
        "hospital_name": "Dr. Rela Institute & Medical Centre",
        "city": "Chennai",
        "address": "7, CLC Works Road, Chromepet, Chennai - 600044",
        "contact_number": "+91 44 6666 7777",
        "email": "info@relainstitute.com",
        "TPAs": ["05", "06", "07", "08", "09", "10", "11", "12", "13", "14"]
    },
    {
        "hospital_name": "SIMS Hospital",
        "city": "Chennai",
        "address": "No.1, Jawaharlal Nehru Salai, 100 Feet Road, Vadapalani, Chennai - 600026",
        "contact_number": "+91 44 2000 2001",
        "email": "info@simshospitals.com",
        "TPAs": ["06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]
    },
    {
        "hospital_name": "Global Hospitals",
        "city": "Chennai",
        "address": "439, Cheran Nagar, Perumbakkam, Chennai - 600100",
        "contact_number": "+91 44 4477 7000",
        "email": "info@gleneaglesglobalhospitals.com",
        "TPAs": ["07", "08", "09", "10", "11", "12", "13", "14", "15", "16"]
    }
]

# Streamlit app
st.title("MedLeads")
st.header("Welcome to MedLeads")

# Sidebar for selecting city and TPA
city_selected = st.sidebar.selectbox(
    "Select a City",
    sorted(set(hospital['city'] for hospital in hospital_data))
)

# Filter TPAs based on hospitals in the selected city
available_tpas = set()
for hospital in hospital_data:
    if hospital["city"] == city_selected:
        available_tpas.update(hospital["TPAs"])

selected_tpa = st.sidebar.selectbox(
    "Select a TPA",
    sorted(available_tpas),
    format_func=lambda x: tpa_data.get(x, "Unknown TPA")
)

# Switch-type toggle for coverage type
coverage_type = st.checkbox("Cashless Coverage", value=True)

# Display hospital information based on city and TPA selection
for hospital in hospital_data:
    if hospital["city"] == city_selected:
        # Placeholder for hospital name and rating
        placeholder = st.expander(f"{hospital['hospital_name']} - Rating: {hospital['rating']}/5")
        with placeholder:
            st.write(f"Location: {hospital['city']}, {hospital['address']}")
            st.write(f"Contact: {hospital['contact_number']} | Email: {hospital['email']}")

            if coverage_type:
                if selected_tpa in hospital["TPAs"]:
                    st.write(f"TPA: {tpa_data[selected_tpa]} is available for Cashless Coverage.")
                else:
                    st.warning(f"{tpa_data[selected_tpa]} is not available for Cashless Coverage at this hospital.")
            else:
                st.write("Payment Method: CASH (Non-Cashless)")

            # Patient referral button
            if st.button(f"Refer Patient to {hospital['hospital_name']}", key=hospital['hospital_name']):
                with st.form(f"patient_form_{hospital['hospital_name']}", clear_on_submit=True):
                    st.write("### Patient Information")
                    patient_name = st.text_input("Patient Name")
                    patient_age = st.number_input("Age", min_value=0, max_value=120)
                    patient_mobile = st.text_input("Mobile Number")
                    policy_selected = st.selectbox("Select Policy", [selected_tpa], index=0)
                    submit_button = st.form_submit_button(label="Submit")
                    if submit_button:
                        st.success(f"Patient referral to {hospital['hospital_name']} submitted successfully with policy {policy_selected}.")