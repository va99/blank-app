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
    # Example hospital data
    {
        "hospital_name": "City Hospital",
        "city": "Mumbai",
        "address": "123 Main St",
        "contact_number": "+91-22-12345678",
        "email": "contact@cityhospital.com",
        "TPAs": ["01", "03", "05"]
    },
    {
        "hospital_name": "Sunrise Clinic",
        "city": "Mumbai",
        "address": "456 Park Ave",
        "contact_number": "+91-22-87654321",
        "email": "info@sunriseclinic.com",
        "TPAs": ["02", "04", "06"]
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

# Display hospital information in a collapsible layout
for hospital in filtered_hospitals:
    with st.expander(f"{hospital['hospital_name']} 🏥", expanded=False):
        st.write(f"**Location:** {hospital['city']}, {hospital['address']}")
        st.write(f"**Contact:** {hospital['contact_number']} | **Email:** {hospital['email']}")

        if coverage_type:
            st.write(f"**TPA:** {tpa_data[selected_tpa]} is available for Cashless Coverage.")
        else:
            st.write("**Payment Method:** CASH (Non-Cashless)")

        # All policies list
        all_policies = [tpa_data[code] for code in tpa_data]
        default_policy = tpa_data.get(selected_tpa, "CASH")

        with st.form(f"patient_form_{hospital['hospital_name']}", clear_on_submit=True):
            st.write("### Patient Information")
            patient_name = st.text_input("Patient Name")
            patient_age = st.number_input("Age", min_value=0, max_value=120)
            patient_mobile = st.text_input("Mobile Number")
            
            # Select Policy dropdown with default to filtered policy
            selected_policy = st.selectbox(
                "Select Policy",
                options=all_policies,
                index=all_policies.index(default_policy) if default_policy in all_policies else 0
            )
            submit_button = st.form_submit_button(label="Refer Patient")
            if submit_button:
                st.success(f"Patient referral to {hospital['hospital_name']} submitted successfully.")

# Balance Section
st.header("Balance")

# Display balance with mock data
number_of_patients_referred = 130
earnings_per_patient = 1800
total_earnings = number_of_patients_referred * earnings_per_patient

st.write(f"**Balance:** ₹{total_earnings}")
st.button("Withdraw")  # Mock withdraw button