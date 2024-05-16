import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import joblib

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

# Dictionary of questions and answers for Core domain
core_questions = {
    "What is the chemical symbol for water?": ["H2O", "CO2", "NaCl", "O2"],
    "Who is known as the father of modern physics?": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Niels Bohr"],
    "What is the unit of electrical resistance?": ["Ohm", "Volt", "Ampere", "Watt"]
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
}

def main():
    st.markdown("<h1 style='text-align: center; color: #ff6347;'>Career crafter</h1>", unsafe_allow_html=True)

    image = st.image('https://culturepartners.com/wp-content/uploads/2023/12/culture-2.png', use_column_width=True)
    st.sidebar.title("Your Information")

    Name = st.sidebar.text_input("Full Name")
    Contact_Number = st.sidebar.text_input("Contact Number")
    Email_address = st.sidebar.text_input("Email address")

    if not Name and Email_address:
        st.sidebar.warning("Please fill out your name and EmailID")

    if Name and Contact_Number and Email_address:
        st.sidebar.success("Thanks!")

    # Add a dropdown for selecting domain
    selected_domain = st.sidebar.selectbox("Select Domain", ["IT", "Core"])

    # Display questions based on the selected domain
    if selected_domain == "IT":
        st.subheader("IT Domain Questions")
        user_responses = display_questions(it_questions, "it")
    elif selected_domain == "Core":
        st.subheader("Core Domain Questions")
        user_responses = display_questions(core_questions, "core")

    # Submit button
    if st.button("Submit"):
        # Get user responses and recommend companies
        recommended_companies = get_companies(user_responses)
        if recommended_companies:
            st.success(f"**Recommended company based on your preferences:** {', '.join(recommended_companies)}")
            for company in recommended_companies:
                st.info(f"- **Click the link to check website:** [{company}]({company_website.get(company)})")
        else:
            st.error("No matching companies found based on your preferences.")

        # Clear main page content after submission
        st.empty()

def display_questions(questions, prefix):
    user_responses = {}
    for i, (question, options) in enumerate(questions.items()):
        key = f"{prefix}_question_{i}"
        st.write(question)
        selected_option = st.radio("Select your answer:", options, key=key)
        user_responses[question] = selected_option
        st.write("Your selected answer:", selected_option)
        st.write("---")
    return user_responses

def get_companies(responses):
    historical_data = pd.read_csv("Dataset/dataset.csv")
    model = joblib.load("Models/random_forest_model.pkl")

    all_data = pd.concat([historical_data, pd.DataFrame(responses, index=[0])])
    all_data.fillna(method='ffill', inplace=True)

    encoder = OneHotEncoder(drop='first', sparse=False)
    all_data_encoded = encoder.fit_transform(all_data.drop(columns=["Company"]))

    X = all_data_encoded[:-1]
    y = all_data["Company"][:-1]

    model = RandomForestClassifier(random_state=42, class_weight='balanced')
    model.fit(X, y)

    user_responses_encoded = all_data_encoded[-1].reshape(1, -1)

    predicted_companies = model.predict(user_responses_encoded)
    return predicted_companies.tolist()


if __name__ == "__main__":
    main()
