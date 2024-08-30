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
    },
    {
        "hospital_name": "Apollo Hospitals",
        "city": "Chennai",
        "address": "21 Greams Lane, Off Greams Road, Chennai, Tamil Nadu 600006",
        "contact_number": "+91 44 2829 3333",
        "email": "info@apollohospitals.com",
        "TPAs": ["01", "02", "03", "04", "05", "06", "07"]
    },
    {
        "hospital_name": "Max Super Specialty Hospital",
        "city": "Delhi",
        "address": "Saket, New Delhi, Delhi 110017",
        "contact_number": "+91 11 2651 5050",
        "email": "info@maxhealthcare.com",
        "TPAs": ["02", "03", "04", "05", "08", "09", "10"]
    },
    {
        "hospital_name": "Cleveland Clinic",
        "city": "Chennai",
        "address": "Chennai, Tamil Nadu 600001",
        "contact_number": "+91 44 1234 5678",
        "email": "info@clevelandclinic.org",
        "TPAs": ["01", "03", "05", "07", "10", "12", "14"]
    },
    {
        "hospital_name": "Fortis Hospital",
        "city": "Chennai",
        "address": "Pallikaranai, Chennai, Tamil Nadu 600100",
        "contact_number": "+91 44 4200 0000",
        "email": "info@fortishealthcare.com",
        "TPAs": ["02", "04", "06", "08", "09", "11", "13"]
    },
    {
        "hospital_name": "Sri Ramachandra Medical Centre",
        "city": "Chennai",
        "address": "Porur, Chennai, Tamil Nadu 600116",
        "contact_number": "+91 44 2476 6000",
        "email": "info@sriramachandra.edu.in",
        "TPAs": ["01", "02", "03", "05", "06", "08", "12"]
    },
    {
        "hospital_name": "Aster CMI Hospital",
        "city": "Bengaluru",
        "address": "Bangalore, Karnataka 560034",
        "contact_number": "+91 80 4330 0000",
        "email": "info@astercmi.com",
        "TPAs": ["02", "03", "04", "05", "09", "10", "14"]
    },
    {
        "hospital_name": "HCG Cancer Hospital",
        "city": "Bengaluru",
        "address": "Sankey Road, Bengaluru, Karnataka 560020",
        "contact_number": "+91 80 2222 2222",
        "email": "info@hcghospitals.com",
        "TPAs": ["01", "05", "06", "08", "10", "12", "19"]
    },
    {
        "hospital_name": "Care Hospital",
        "city": "Hyderabad",
        "address": "Banjara Hills, Hyderabad, Telangana 500034",
        "contact_number": "+91 40 2333 3333",
        "email": "info@carehospitals.com",
        "TPAs": ["02", "04", "06", "08", "11", "14", "18"]
    },
    {
        "hospital_name": "Yashoda Hospital",
        "city": "Hyderabad",
        "address": "Secunderabad, Hyderabad, Telangana 500003",
        "contact_number": "+91 40 2780 1234",
        "email": "info@yashodahospitals.com",
        "TPAs": ["03", "05", "07", "09", "12", "15", "20"]
    },
    {
        "hospital_name": "Narayana Health",
        "city": "Bengaluru",
        "address": "Bangalore, Karnataka 560029",
        "contact_number": "+91 80 2202 2202",
        "email": "info@narayanahealth.org",
        "TPAs": ["01", "02", "03", "06", "08", "10", "13"]
    },
    {
        "hospital_name": "Sankara Nethralaya",
        "city": "Chennai",
        "address": "Chennai, Tamil Nadu 600006",
        "contact_number": "+91 44 2821 2020",
        "email": "info@sankaranethralaya.org",
        "TPAs": ["02", "04", "06", "09", "11", "15", "17"]
    },
    {
        "hospital_name": "Shree Krishna Hospital",
        "city": "Chhattisgarh",
        "address": "Raipur, Chhattisgarh 492001",
        "contact_number": "+91 771 222 3333",
        "email": "info@shreekrishnahospital.com",
        "TPAs": ["01", "03", "05", "07", "09", "12", "14"]
    },
    {
        "hospital_name": "Paras HMRI Hospital",
        "city": "Bihar",
        "address": "Patna, Bihar 800001",
        "contact_number": "+91 612 222 4444",
        "email": "info@parashmri.com",
        "TPAs": ["02", "04", "06", "08", "11", "13", "19"]
    },
    {
        "hospital_name": "Max Super Specialty Hospital",
        "city": "Uttar Pradesh",
        "address": "Saket, Noida, Uttar Pradesh 201301",
        "contact_number": "+91 120 404 0404",
        "email": "info@maxhealthcare.com",
        "TPAs": ["01", "02", "03", "05", "08", "10", "12"]
    },
    {
        "hospital_name": "HCG Hospital",
        "city": "Nagpur",
        "address": "Nagpur, Maharashtra 440001",
        "contact_number": "+91 712 222 5555",
        "email": "info@hcghospitals.com",
        "TPAs": ["03", "05", "07", "09", "12", "15", "20"]
    },
    {
        "hospital_name": "Fortis Hospital",
        "city": "Punjab",
        "address": "Ludhiana, Punjab 141001",
        "contact_number": "+91 161 222 3333",
        "email": "info@fortishealthcare.com",
        "TPAs": ["01", "02", "04", "06", "08", "11", "14"]
    },
    {
        "hospital_name": "Indira Gandhi Medical College",
        "city": "Himachal Pradesh",
        "address": "Shimla, Himachal Pradesh 171001",
        "contact_number": "+91 177 222 4444",
        "email": "info@igmcshimla.edu.in",
        "TPAs": ["02", "03", "05", "07", "09", "12", "18"]
    },
    {
        "hospital_name": "Sanjeevani Hospital",
        "city": "Uttarakhand",
        "address": "Dehradun, Uttarakhand 248001",
        "contact_number": "+91 135 222 5555",
        "email": "info@sanjeevanihospital.com",
        "TPAs": ["01", "04", "06", "08", "10", "13", "19"]
    },
    {
        "hospital_name": "Shri Mata Vaishno Devi Narayana Superspeciality Hospital",
        "city": "Jammu & Kashmir",
        "address": "Katra, Jammu & Kashmir 182301",
        "contact_number": "+91 1991 234 567",
        "email": "info@smvdns.com",
        "TPAs": ["02", "03", "05", "07", "09", "12", "15"]
    },
    {
        "hospital_name": "Kalinga Hospital",
        "city": "Orissa",
        "address": "Bhubaneswar, Orissa 751024",
        "contact_number": "+91 674 222 3333",
        "email": "info@kalingahospital.com",
        "TPAs": ["01", "02", "04", "06", "08", "11", "20"]
    },
    {
        "hospital_name": "Apollo Hospitals",
        "city": "Hyderabad",
        "address": "Hyderabad, Telangana 500034",
        "contact_number": "+91 40 2331 1111",
        "email": "info@apollohospitals.com",
        "TPAs": ["03", "05", "07", "09", "10", "13", "19"]
    },
    {
        "hospital_name": "Paras Hospital",
        "city": "Jharkhand",
        "address": "Ranchi, Jharkhand 834001",
"contact_number": "+91 651 222 4444",
"email": "info@parashospital.com",
"TPAs": ["02", "05", "07", "09", "10", "12", "19"]
},
{
"hospital_name": "Tata Main Hospital",
"city": "Jharkhand",
"address": "Bistupur, Jamshedpur, Jharkhand 831001",
"contact_number": "+91 657 222 5555",
"email": "info@tatatmh.com",
"TPAs": ["01", "03", "06", "08", "11", "13", "17"]
},
{
"hospital_name": "Bokaro General Hospital",
"city": "Jharkhand",
"address": "Bokaro Steel City, Jharkhand 827001",
"contact_number": "+91 654 222 6666",
"email": "info@bokarohospital.com",
"TPAs": ["02", "04", "07", "09", "12", "15", "19"]
},
{
"hospital_name": "Medica Superspecialty Hospital",
"city": "Kolkata",
"address": "Mukundapur, Kolkata, West Bengal 700099",
"contact_number": "+91 33 4444 7777",
"email": "info@medicahospital.com",
"TPAs": ["01", "05", "08", "10", "13", "16", "20"]
},
{
"hospital_name": "Apollo Gleneagles Hospital",
"city": "Kolkata",
"address": "Kolkata, West Bengal 700054",
"contact_number": "+91 33 2320 3040",
"email": "info@apollogleneagles.com",
"TPAs": ["02", "03", "06", "09", "11", "14", "17"]
},
{
"hospital_name": "Woodlands Hospital",
"city": "Kolkata",
"address": "Kolkata, West Bengal 700025",
"contact_number": "+91 33 2283 8811",
"email": "info@woodlandshospital.com",
"TPAs": ["01", "04", "07", "10", "12", "15", "19"]
},
{
"hospital_name": "Dispur Hospital",
"city": "Guwahati",
"address": "Guwahati, Assam 781005",
"contact_number": "+91 361 222 4444",
"email": "info@dispurhospital.com",
"TPAs": ["03", "05", "08", "11", "13", "16", "20"]
},
{
"hospital_name": "Nemcare Hospital",
"city": "Guwahati",
"address": "Guwahati, Assam 781007",
"contact_number": "+91 361 252 8888",
"email": "info@nemcarehospital.com",
"TPAs": ["02", "04", "06", "09", "12", "14", "17"]
},
{
"hospital_name": "Excelcare Hospital",
"city": "Guwahati",
"address": "Guwahati, Assam 781022",
"contact_number": "+91 361 400 1111",
"email": "info@excelcarehospital.com",
"TPAs": ["01", "05", "07", "10", "13", "15", "19"]
},
{
"hospital_name": "Tripura Medical College & Dr. B.R.Ambedkar Memorial Teaching Hospital",
"city": "Tripura",
"address": "Hapania, Tripura 799014",
"contact_number": "+91 381 222 4444",
"email": "info@tripuramedicalcollege.com",
"TPAs": ["02", "03", "06", "08", "11", "14", "16"]
},
{
"hospital_name": "Bethany Hospital",
"city": "Shillong",
"address": "Shillong, Meghalaya 793001",
"contact_number": "+91 364 222 5555",
"email": "info@bethanyhospital.com",
"TPAs": ["01", "04", "07", "09", "12", "15", "17"]
},
{
"hospital_name": "Naga Hospital Authority Kohima",
"city": "Nagaland",
"address": "Kohima, Nagaland 797001",
"contact_number": "+91 370 222 6666",
"email": "info@nagahospital.com",
"TPAs": ["03", "05", "08", "10", "13", "16", "19"]
},
{
"hospital_name": "Odisha Cancer Hospital",
"city": "Cuttack",
"address": "Cuttack, Odisha 753007",
"contact_number": "+91 671 222 7777",
"email": "info@odishacancerhospital.com",
"TPAs": ["02", "04", "06", "09", "11", "14", "20"]
},
{
"hospital_name": "Yashoda Super Specialty Hospital",
"city": "Hyderabad",
"address": "Secunderabad, Hyderabad, Telangana 500003",
"contact_number": "+91 40 4567 8901",
"email": "info@yashodasuperspecialty.com",
"TPAs": ["01", "03", "05", "07", "10", "12", "15"]
},
{
"hospital_name": "Aware Gleneagles Global Hospital",
"city": "Hyderabad",
"address": "Hyderabad, Telangana 500032",
"contact_number": "+91 40 2345 6789",
"email": "info@awaregleneagles.com",
"TPAs": ["02", "04", "06", "08", "11", "13", "17"]
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

