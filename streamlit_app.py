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

# Mock data
hospital_data = [
    {
        "hospital_name": "Kokilaben Dhirubhai Ambani Hospital",
        "city": "Mumbai",
        "address": "Rao Saheb Achutrao Patwardhan Marg, Four Bungalows, Andheri West, Mumbai, Maharashtra 400053",
        "contact_number": "+91 22 4269 6969",
        "email": "info@kokilabenhospital.com",
        "TPAs": ["01", "02", "05", "07", "08", "10", "11"]
    },
    {
        "hospital_name": "Tata Memorial Hospital",
        "city": "Mumbai",
        "address": "Dr E Borges Road, Parel, Mumbai, Maharashtra 400012",
        "contact_number": "+91 22 2417 7000",
        "email": "info@tmc.gov.in",
        "TPAs": ["03", "04", "06", "07", "09", "10", "12"]
    },
    {
        "hospital_name": "P.D. Hinduja Hospital & Medical Research Centre",
        "city": "Mumbai",
        "address": "Veer Savarkar Marg, Mahim, Mumbai, Maharashtra 400016",
        "contact_number": "+91 22 2445 2575",
        "email": "info@hindujahospital.com",
        "TPAs": ["01", "02", "03", "05", "08", "11", "12"]
    },
    {
        "hospital_name": "Fortis Hiranandani Hospital",
        "city": "Mumbai",
        "address": "Mini Sea Shore Road, Sector 10A, Vashi, Navi Mumbai, Maharashtra 400703",
        "contact_number": "+91 22 3919 9222",
        "email": "info@fortishealthcare.com",
        "TPAs": ["02", "04", "06", "07", "09", "10", "13"]
    },
    {
        "hospital_name": "Sir Ganga Ram Hospital",
        "city": "Delhi",
        "address": "Rajinder Nagar, New Delhi – 110060, INDIA",
        "contact_number": "011 4225 4000",
        "email": "info@sgra.com",
        "TPAs": ["01", "05", "06", "08", "11", "13", "16"]
    },
    {
        "hospital_name": "Indraprastha Apollo Hospital",
        "city": "Delhi",
        "address": "Mathura Road, Delhi-110076",
        "contact_number": "1860 500 1066",
        "email": "info@apollohospitals.com",
        "TPAs": ["02", "03", "05", "07", "09", "12", "14"]
    },
    {
        "hospital_name": "Moolchand Medicity",
        "city": "Delhi",
        "address": "Lajpat Nagar, New Delhi, Delhi - 110024",
        "contact_number": "011 4200 0000",
        "email": "info@moolchand.com",
        "TPAs": ["01", "04", "06", "08", "10", "13", "15"]
    },
    {
        "hospital_name": "Manipal Hospital",
        "city": "Jaipur",
        "address": "Sector 5, Main Sikar Road, Vidhyadhar Nagar, Jaipur, Rajasthan 302023",
        "contact_number": "+91 141 404 4444",
        "email": "info@manipalhospitals.com",
        "TPAs": ["03", "05", "07", "08", "11", "14", "17"]
    },
    {
        "hospital_name": "Fortis Escorts Hospital",
        "city": "Jaipur",
        "address": "Jawahar Lal Nehru Marg, Sector 5, Malviya Nagar, Jaipur, Rajasthan 302017",
        "contact_number": "+91 141 405 5555",
        "email": "info@fortishealthcare.com",
        "TPAs": ["02", "04", "06", "09", "12", "16", "18"]
    },
    {
        "hospital_name": "AIIMS Jodhpur",
        "city": "Jodhpur",
        "address": "Marudhar Industrial Area, 2nd Phase, M.I.A. 1st Phase, Basni, Jodhpur, Rajasthan 342005",
        "contact_number": "+91 291 2740741",
        "email": "info@aiimsjodhpur.edu.in",
        "TPAs": ["01", "05", "07", "10", "12", "14", "19"]
    },
    {
        "hospital_name": "CK Birla Hospital",
        "city": "Jaipur",
        "address": "Near Mahindra World City, Jaipur, Rajasthan 302018",
        "contact_number": "+91 141 404 2000",
        "email": "info@ckbirlahospital.com",
        "TPAs": ["02", "03", "06", "08", "11", "15", "18"]
    },
    {
        "hospital_name": "HCG Cancer Centre",
        "city": "Ahmedabad",
        "address": "Science City Rd, off Sarkhej - Gandhinagar Highway, Sola, Ahmedabad, Gujarat 380060",
        "contact_number": "+91 635 888 8814",
        "email": "info@hcgoncology.com",
        "TPAs": ["01", "03", "06", "08", "09", "13", "20"]
    },
    {
        "hospital_name": "Apollo Hospitals",
        "city": "Ahmedabad",
        "address": "Plot No, 1A, Gandhinagar - Ahmedabad Rd, GIDC Bhat, estate, Ahmedabad, Gujarat 382428",
        "contact_number": "+91 79 6670 1800",
        "email": "info@apollohospitals.com",
        "TPAs": ["02", "05", "07", "10", "12", "14", "16"]
    },
    {
        "hospital_name": "Sterling Hospitals",
        "city": "Ahmedabad",
        "address": "Sterling Hospital Rd, near Maharaja Agrasen Vidhyalaya, Memnagar, Ahmedabad, Gujarat 380052",
        "contact_number": "+91 9898 987878",
        "email": "info@sterlinghospitals.com",
        "TPAs": ["04", "06", "09", "11", "13", "15", "17"]
    },
    {
        "hospital_name": "Shalby Hospitals",
        "city": "Ahmedabad",
        "address": "Near Gujarat High Court, Ellis Bridge, Ahmedabad, Gujarat 380006",
        "contact_number": "+91 9512 009180",
        "email": "info@shalby.org",
        "TPAs": ["03", "07", "08", "10", "12", "14", "18"]
    },
    {
        "hospital_name": "Narayana Multispeciality Hospital",
        "city": "Ahmedabad",
        "address": "Nr. Chakudiya Mahadev, Rakhial Cross Road, Opp. Rakhial Police Station, Rakhial Ahmedabad, Gujarat - 380023",
        "contact_number": "+91 80 6750 6922",
        "email": "info@narayanahealth.org",
        "TPAs": ["01", "05", "09", "12", "14", "17", "20"]
    },
    {
        "hospital_name": "Wockhardt Hospital",
        "city": "Surat",
        "address": "5RM5+JJ7, R K Desai Marg Opposite Chowpatty, Athwalines, Athwa Gate, Surat, Gujarat 395001",
        "contact_number": "+91 22 6178 4400",
        "email": "info@wockhardthospitals.com",
        "TPAs": ["02", "04", "06", "08", "11", "13", "19"]
    },
    {
        "hospital_name": "Aster RV Hospital",
        "city": "Bengaluru",
        "address": "Sardar Patel Ring Road, Thaltej, Ahmedabad, Gujarat 380054",
        "contact_number": "+91 79 6600 0000",
        "email": "info@asterdmhealthcare.com",
        "TPAs": ["03", "05", "07", "10", "12", "15", "16"]
    },
    {
        "hospital_name": "Manipal Hospital",
        "city": "Bengaluru",
        "address": "No. 98, 1st Cross, 1st Block, Koramangala, Bengaluru, Karnataka 560034",
        "contact_number": "+91 80 2222 2222",
        "email": "info@manipalhospitals.com",
        "TPAs": ["01", "02", "04", "07", "09", "14", "20"]
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

