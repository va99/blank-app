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

#Mock data
hospital_data = [
    {
        "hospital_name": "Kokilaben Dhirubhai Ambani Hospital",
        "city": "Mumbai",
        "address": "Rao Saheb Achutrao Patwardhan Marg, Four Bungalows, Andheri West, Mumbai, Maharashtra 400053",
        "contact_number": "+91 22 4269 6969",
        "email": "info@kokilabenhospital.com",
        "TPAs": ["01", "02", "05", "07", "08", "10", "11"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Tata Memorial Hospital",
        "city": "Mumbai",
        "address": "Dr E Borges Road, Parel, Mumbai, Maharashtra 400012",
        "contact_number": "+91 22 2417 7000",
        "email": "info@tmc.gov.in",
        "TPAs": ["03", "04", "06", "07", "09", "10", "12"],
        "rating": "3.8"
    },
    {
        "hospital_name": "Sir Ganga Ram Hospital",
        "city": "Delhi",
        "address": "Rajinder Nagar, New Delhi – 110060, INDIA",
        "contact_number": "011 4225 4000",
        "email": "info@sgra.com",
        "TPAs": ["01", "05", "06", "08", "11", "13", "16"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Indraprastha Apollo Hospital",
        "city": "Delhi",
        "address": "Mathura Road, Delhi-110076",
        "contact_number": "1860 500 1066",
        "email": "info@apollohospitals.com",
        "TPAs": ["02", "03", "05", "07", "09", "12", "14"],
        "rating": "4.3"
    },
    {
        "hospital_name": "Manipal Hospital",
        "city": "Jaipur",
        "address": "Sector 5, Main Sikar Road, Vidhyadhar Nagar, Jaipur, Rajasthan 302023",
        "contact_number": "+91 141 404 4444",
        "email": "info@manipalhospitals.com",
        "TPAs": ["03", "05", "07", "08", "11", "14", "17"],
        "rating": "4.1"
    },
    {
        "hospital_name": "AIIMS Jodhpur",
        "city": "Jodhpur",
        "address": "Marudhar Industrial Area, 2nd Phase, M.I.A. 1st Phase, Basni, Jodhpur, Rajasthan 342005",
        "contact_number": "+91 291 2740741",
        "email": "info@aiimsjodhpur.edu.in",
        "TPAs": ["01", "05", "07", "10", "12", "14", "19"],
        "rating": "4.1"
    },
    {
        "hospital_name": "HCG Cancer Centre",
        "city": "Ahmedabad",
        "address": "Science City Rd, off Sarkhej - Gandhinagar Highway, Sola, Ahmedabad, Gujarat 380060",
        "contact_number": "+91 635 888 8814",
        "email": "info@hcgoncology.com",
        "TPAs": ["01", "03", "06", "08", "09", "13", "20"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Apollo Hospitals",
        "city": "Ahmedabad",
        "address": "Plot No, 1A, Gandhinagar - Ahmedabad Rd, GIDC Bhat, estate, Ahmedabad, Gujarat 382428",
        "contact_number": "+91 79 6670 1800",
        "email": "info@apollohospitals.com",
        "TPAs": ["02", "05", "07", "10", "12", "14", "16"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Aster RV Hospital",
        "city": "Bengaluru",
        "address": "Sardar Patel Ring Road, Thaltej, Ahmedabad, Gujarat 380054",
        "contact_number": "+91 79 6600 0000",
        "email": "info@asterdmhealthcare.com",
        "TPAs": ["03", "05", "07", "10", "12", "15", "16"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Apollo Hospitals",
        "city": "Chennai",
        "address": "21 Greams Lane, Off Greams Road, Chennai, Tamil Nadu 600006",
        "contact_number": "+91 44 2829 3333",
        "email": "info@apollohospitals.com",
        "TPAs": ["01", "02", "03", "04", "05", "06", "07"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Max Super Specialty Hospital",
        "city": "Delhi",
        "address": "Saket, New Delhi, Delhi 110017",
        "contact_number": "+91 11 2651 5050",
        "email": "info@maxhealthcare.com",
        "TPAs": ["02", "03", "04", "05", "08", "09", "10"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Shree Krishna Hospital",
        "city": "Chhattisgarh",
        "address": "Raipur, Chhattisgarh 492001",
        "contact_number": "+91 771 222 3333",
        "email": "info@shreekrishnahospital.com",
        "TPAs": ["01", "03", "05", "07", "09", "12", "14"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Paras HMRI Hospital",
        "city": "Bihar",
        "address": "Patna, Bihar 800001",
        "contact_number": "+91 612 222 4444",
        "email": "info@parashmri.com",
        "TPAs": ["02", "04", "06", "08", "11", "13", "19"],
        "rating": "4.1"
    },
    {
        "hospital_name": "Tripura Medical College & Dr. B.R.Ambedkar Memorial Teaching Hospital",
        "city": "Tripura",
        "address": "Hapania, Tripura 799014",
        "contact_number": "+91 381 222 4444",
        "email": "info@tripuramedicalcollege.com",
        "TPAs": ["02", "03", "06", "08", "11", "14", "16"],
        "rating": "4.1"
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

# Filter hospitals based on the selected city
filtered_hospitals = [hospital for hospital in hospital_data if hospital["city"] == city_selected]

# Filter TPAs based on hospitals in the selected city
available_tpas = set()
for hospital in filtered_hospitals:
    available_tpas.update(hospital["TPAs"])

selected_tpa = st.sidebar.selectbox(
    "Select a TPA",
    sorted(available_tpas),
    format_func=lambda x: tpa_data.get(x, "Unknown TPA")
)

# Switch-type toggle for coverage type
coverage_type = st.checkbox("Cashless Coverage", value=True)

# Filter hospitals based on the coverage type and selected TPA
if coverage_type:
    filtered_hospitals = [hospital for hospital in filtered_hospitals if selected_tpa in hospital["TPAs"]]
else:
    # No additional filter needed for non-cashless
    pass

# Display hospital information in a collapsible layout
for hospital in filtered_hospitals:
    with st.expander(f"{hospital['hospital_name']} ({hospital['rating']}⭐️)", expanded=False):
        st.write(f"**Location:** {hospital['city']}, {hospital['address']}")
        st.write(f"**Contact:** {hospital['contact_number']} | **Email:** {hospital['email']}")

        if coverage_type:
            st.write(f"**TPA:** {tpa_data[selected_tpa]} is available for Cashless Coverage.")
        else:
            st.write("**Payment Method:** CASH (Non-Cashless)")

        with st.form(f"patient_form_{hospital['hospital_name']}", clear_on_submit=True):
            st.write("### Patient Information")
            patient_name = st.text_input("Patient Name")
            patient_age = st.number_input("Age", min_value=0, max_value=120)
            patient_mobile = st.text_input("Mobile Number")
            selected_policy = st.selectbox(
                "Select Policy",
                options=[tpa_data[selected_tpa]] if coverage_type else ["CASH"],
                index=0
            )
            submit_button = st.form_submit_button(label="Refer Patient")
            if submit_button:
                st.success(f"Patient referral to {hospital['hospital_name']} submitted successfully.")


