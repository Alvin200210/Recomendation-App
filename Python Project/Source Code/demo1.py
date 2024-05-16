import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import joblib
import hashlib
import csv

# File paths and user database file
user_database_file = "user_database.csv"

# Dictionary of questions and answers for IT domain
it_questions = {
    "Do you prefer a structured or flexible work environment?": ["Structured", "Flexible"],
    "Are you more comfortable with a formal or casual work atmosphere?": ["Formal", "Casual"],
    "How do you prefer to collaborate with colleagues?": ["Face-to-face", "Virtually", "Combination"],
    "Are you more productive when working independently or as part of a team?": ["Independently", "Part of a team"],
    "Do you prefer a hands-on, directive management style, or do you prefer more autonomy and freedom?": ["Hands-on", "Autonomy"],
    "How do you respond to feedback and guidance from supervisors?": ["Regular check-ins", "Independence"],
    "How important is work-life balance to you, and what initiatives or policies do you appreciate in this regard?": ["Very important", "Moderately important", "Not important"],
    "What values do you prioritize in a workplace?": ["Diversity and inclusivity", "Innovation", "Sustainability"],
    "How important is it for you to work for a company that aligns with your personal values and beliefs?": ["Very important", "Moderately important", "Not important"],
    "What are your expectations regarding career development opportunities within a company?": ["Strong opportunities for growth and advancement", "Structured training programs and mentorship opportunities"],
    "How do you respond to constructive feedback, and what type of feedback culture do you thrive in?": ["Open to feedback and appreciate a culture of continuous improvement", "Prefer positive reinforcement and recognition for achievements"],
    "How do you prefer to celebrate successes and achievements in the workplace?": ["Team celebrations and recognition", "Personal recognition and rewards", "Promotion"]
} 

# Dictionary of questions and answers for Mechanical Core domain
mechanical_core_questions = {
    "What type of work do you expect for your role in mechanical engineering?":["Routine, repetitive tasks", "Challenging and engaging projects","Simple, basic engineering projects","Unrelated administrative tasks"],
    "How important is career development to you in a mechanical engineering role?": ["Not important", "Important","Very important"],
    "What kind of work environment do you prefer in a mechanical engineering role?": ["Conservative and resistant to change", "Innovative and open to new ideas","Disengaged and uninspiring","Strict and rigid"],
    "How do you prefer to collaborate with colleagues in a mechanical engineering role?": ["Solo projects with no collaboration", "Occasional collaboration with other teams", "Working in isolation from others","Collaborative team environment"],
    "How important is work-life balance to you in a mechanical engineering role?": ["Not important", "Important","Very important"],
    "What type of management style do you prefer in a mechanical engineering role?": ["Supportive and approachable management", "Strict and unapproachable management","Indifferent management with little guidance","Micromanaging leadership style"],
    "What kind of compensation and benefits package are you expecting in a mechanical engineering role?": ["Below-market compensation and limited benefits", "Competitive compensation with fair benefits","Only base pay without benefits","Unpredictable and unstable compensation"],
    "How important is job security to you in a mechanical engineering role?": ["Not important", "Important","Very important"],
    "What kind of ethical practices do you expect from the company in a mechanical engineering role?": [" Unethical and unsustainable practices", "Adherence to ethical and sustainable practices","No regard for ethical considerations","Disregard for regulations and compliance"],
    "What resources and technology do you expect access to in a mechanical engineering role?": ["Outdated tools and limited resources", "Latest technology and sufficient resources","No access to new technology or resources","Only basic tools and equipment"]
}

# Dictionary of questions and answers for Electrical Core domain
electrical_core_questions = {
    "What type of work do you expect for your role in Electrical engineering?":["Routine, repetitive tasks", "Challenging and engaging projects","Simple, basic engineering projects","Unrelated administrative tasks"],
    "How important is career development to you in a Electrical engineering role?": ["Not important", "Important","Very important"],
    "What kind of work environment do you prefer in a Electrical engineering role?": ["Conservative and resistant to change", "Innovative and open to new ideas","Disengaged and uninspiring","Strict and rigid"],
    "How do you prefer to collaborate with colleagues in a Electrical engineering role?": ["Solo projects with no collaboration", "Occasional collaboration with other teams", "Working in isolation from others","Collaborative team environment"],
    "How important is work-life balance to you in a Electrical engineering role?": ["Not important", "Important","Very important"],
    "What type of management style do you prefer in a Electrical engineering role?": ["Supportive and approachable management", "Strict and unapproachable management","Indifferent management with little guidance","Micromanaging leadership style"],
    "What kind of compensation and benefits package are you expecting in a Electrical engineering role?": ["Below-market compensation and limited benefits", "Competitive compensation with fair benefits","Only base pay without benefits","Unpredictable and unstable compensation"],
    "How important is job security to you in a Electrical engineering role?": ["Not important", "Important","Very important"],
    "What kind of ethical practices do you expect from the company in a Electrical engineering role?": [" Unethical and unsustainable practices", "Adherence to ethical and sustainable practices","No regard for ethical considerations","Disregard for regulations and compliance"],
    "What resources and technology do you expect access to in a Electrical engineering role?": ["Outdated tools and limited resources", "Latest technology and sufficient resources","No access to new technology or resources","Only basic tools and equipment"]
}

# Dictionary of company websites
company_website = {
    "ZOHO": "https://www.zoho.com/careers/#jobs",
    "TCS": "https://www.tcs.com/careers",
    "ACCENTURE": "https://www.accenture.com/in-en/careers/jobsearch?jk=&sb=1&vw=0&is_rj=0&pg=1",
    "HCL Technologies": "https://www.hcltech.com/careers",
    "Wipro": "https://careers.wipro.com/opportunities/jobs",
    "Mphasis": "https://careers.mphasis.com/home.html",
    "LTIMindtree": "https://www.ltimindtree.com/india-careers/",
    "Microsoft": "https://jobs.careers.microsoft.com/global/en/search",
    "Cognizant": "https://careers.cognizant.com/global/en",
    "Honeywell": "https://careers.honeywell.com/us/en",
    "Tech Mahindra": "https://careers.techmahindra.com/",
    "DXC Technology": "https://careers.dxc.com/global/en",
    "Hexaware Technologies": "https://jobs.hexaware.com/",
    "PayPal": "https://careers.pypl.com/home/",
    "NTT DATA": "https://www.nttdata.com/global/en/careers",
    "Atos-Syntel": "https://atos.net/en/careers",
    "Capgemini": "https://www.capgemini.com/in-en/careers/",
    "ADP": "https://jobs.adp.com/veterans/",
    "Freshworks": "https://www.freshworks.com/company/careers/",
    "Sopra Steria": "https://www.soprasteria.com/careers",
    "Thoughtworks": "https://www.thoughtworks.com/en-in/careers",
    "EY": "https://careers.ey.com/",
    "Deloitte": "https://www.deloitte.com/global/en/careers.html",
    "Barclays": "https://home.barclays/careers/",
    "Alstom": "https://jobsearch.alstom.com/",
    "Daimler": "https://www.daimlertruck.com/en/career",
    "seimen": "https://www.siemens.com/global/en/company/jobs.html",
    "Gestamp": "https://jobs.gestamp.com/",
    "Royal Enfield": "https://careers.royalenfield.com/us/en/home",
    "Qualcom": "https://careers.qualcomm.com/careers",
    "Hitachi": "https://careers.hitachi.com/",
    "Micron": "https://www.micron.com/about/careers",
    "L&T": "https://www.larsentoubro.com/corporate/careers/",
    "Flex": "https://flex.com/career",

}
def main():
    # Initialize session state for page management
    if 'page' not in st.session_state:
        st.session_state['page'] = 'login'
    if 'is_authenticated' not in st.session_state:
        st.session_state['is_authenticated'] = False

    # Navigate based on the current page state
    if st.session_state['page'] == 'login':
        login_successful = login_page()
        if login_successful:
            st.session_state['is_authenticated'] = True
            st.session_state['page'] = 'main'
    elif st.session_state['page'] == 'sign_up':
        sign_up_page()
    elif st.session_state['page'] == 'main':
        if st.session_state['is_authenticated']:
            display_main_page()
        else:
            st.session_state['page'] = 'login'  # Redirect to login if not authenticated

def login_page():
    st.title("Login")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Create a two-column layout for the login and sign-up buttons
    col1, col2 = st.columns(2)

    # Display the login button in the first column
    with col1:
        if st.button("Login", key="login_button"):
            # Authenticate the user
            login_successful = authenticate(username, password)
            # Return success state
            if login_successful:
                st.success("Login Successful!")
                return True
            else:
                st.error("Invalid username or password. Please try again.")
                return False

    # Display the sign-up button in the second column
    with col2:
        if st.button("Sign Up", key="signup_button"):
            # Navigate to the sign-up page
            st.session_state['page'] = 'sign_up'
            return False

    return False

def authenticate(username, password):
    # Authenticate the user using the user database
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open(user_database_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            stored_username, stored_email, stored_password = row
            if stored_username == username and stored_password == hashed_password:
                return True
    return False

def sign_up_page():
    st.title("Sign Up")

    # Input fields for the sign-up form
    new_username = st.text_input("New Username")
    new_email = st.text_input("New Email")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    # Handle sign-up button click
    if st.button("Sign Up"):
        if new_password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        else:
            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
            success = add_user_to_database(new_username, new_email, hashed_password)
            if success:
                st.success("Sign-up successful! Please log in.")
                # Redirect to login page
                st.session_state['page'] = 'login'
            else:
                st.error("Username already exists. Please choose a different username.")

def add_user_to_database(username, email, password):
    # Add the new user to the user database if the username does not exist
    with open(user_database_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            stored_username, stored_email, stored_password = row
            if stored_username == username:
                return False  # Username already exists

    # Add the new user to the database
    with open(user_database_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, email, password])
    return True

def display_main_page():
    st.markdown("<h1 style='text-align: center; color: #ff6347;'>Career Crafter</h1>", unsafe_allow_html=True)
    st.write("")
    image = st.image('https://culturepartners.com/wp-content/uploads/2023/12/culture-2.png', use_column_width=True)

    # Collect user information
    st.sidebar.title("Your Information")
    Name = st.sidebar.text_input("Full Name")
    Contact_Number = st.sidebar.text_input("Contact Number")
    Email_address = st.sidebar.text_input("Email address")

    if not Name or not Email_address:
        st.sidebar.warning("Please fill out your name and email address.")
    else:
        st.sidebar.success("Information collected.")

    # Add dropdown for selecting domain
    selected_domain = st.sidebar.selectbox("Select Domain", ["IT", "Mechanical Core", "Electrical Core"])

    # Display questions based on the selected domain
    if selected_domain == "IT":
        st.subheader("IT Domain Questions")
        user_responses = display_questions(it_questions, "it")
    elif selected_domain == "Mechanical Core":
        st.subheader("Mechanical Core Domain Questions")
        user_responses = display_questions(mechanical_core_questions, "mechanical_core")
    elif selected_domain == "Electrical Core":
        st.subheader("Electrical Core Domain Questions")
        user_responses = display_questions(electrical_core_questions, "electrical_core")

    # Submit button to recommend companies
    if st.button("Submit", key="submit_button"):
        recommended_companies = get_companies(user_responses, selected_domain)
        if recommended_companies:
            st.success(f"**Recommended companies based on your preferences:** {', '.join(recommended_companies)}")
            for company in recommended_companies:
                st.info(f"- **Company website:** [{company}]({company_website.get(company)})")
        else:
            st.error("No matching companies found based on your preferences.")

        # Clear the main page content after submission
        st.empty()

def display_questions(questions, prefix):
    user_responses = {}
    for i, (question, options) in enumerate(questions.items()):
        key = f"{prefix}_question_{i}"
        st.markdown(f"### {question}")
        selected_option = st.radio("", options, key=key)
        user_responses[question] = selected_option
        st.write("")
    return user_responses

def get_companies(responses, selected_domain):
    # Define dataset paths based on domain
    if selected_domain == "IT":
        dataset_path = "Dataset/dataset.csv"
    elif selected_domain == "Mechanical Core":
        dataset_path = "Dataset/dataset1.csv"
    elif selected_domain == "Electrical Core":
        dataset_path = "Dataset/dataset2.csv"
    else:
        raise ValueError("Invalid domain selected.")

    # Load historical data and model
    historical_data = pd.read_csv(dataset_path)
    model = joblib.load("Models/random_forest_model.pkl")

    # Add user responses to the data and encode features
    all_data = pd.concat([historical_data, pd.DataFrame(responses, index=[0])])
    all_data.fillna(method='ffill', inplace=True)

    encoder = OneHotEncoder(drop='first', sparse=False)
    all_data_encoded = encoder.fit_transform(all_data.drop(columns=["Company"]))

    # Train the model and predict
    X = all_data_encoded[:-1]
    y = all_data["Company"][:-1]

    model = RandomForestClassifier(random_state=42, class_weight='balanced')
    model.fit(X, y)

    # Predict based on user responses
    user_responses_encoded = all_data_encoded[-1].reshape(1, -1)
    predicted_companies = model.predict(user_responses_encoded)
    return predicted_companies.tolist()

if __name__ == "__main__":
    main()