import streamlit as st
import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(
    page_title="Culture Based Company Recommendation",
    page_icon="🧬",
    initial_sidebar_state="expanded",
)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(4vw, 15px);
            font-weight: 500;
            top: 0px;
            right: 15%;
            background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 0.5rem;
        }
    </style>
    <p id="effect">Work Culture Based Company Recommendation</p>
    """,
    height=100,
)


def page_layout():

    st.write("In the modern business landscape, fostering a vibrant work culture is vital for organizational success. This guide offers key recommendations for companies aiming to cultivate an environment that fosters productivity, innovation, and employee well-being. Strong leadership is fundamental, emphasizing clear communication, empathy, and leading by example. Employee engagement is crucial, supported by collaboration, recognition, and professional growth opportunities. Prioritizing work-life balance and well-being through flexible arrangements and support initiatives is essential to prevent burnout. Embracing diversity and inclusion enriches perspectives and drives innovation. Regular feedback mechanisms ensure continuous improvement, fostering a culture of adaptation and success. Overall, by implementing these strategies, companies can create a dynamic work culture where employees are empowered to excel, contributing to sustained organizational growth and success.")
    

    st.write("**TCS**")

    st.write("https://www.tcs.com/who-we-are")

    st.write("**ZOHO**")

    st.write("https://www.zoho.com/aboutus.html",)

   

    st.write("**Accenture**")

    st.write("https://www.accenture.com/us-en/about/company-index")
    
    
    st.write("**HCL Technologies**")
    st.write("https://www.hcltech.com/about-us")
    
    st.write("**Wipro**")
    st.write("https://www.wipro.com/about-us/")
    
    st.write("**Mphasis**")
    st.write("https://www.mphasis.com/home/corporate/about-mphasis.html")
    
    st.write("**LTIMindtree**")
    st.write("https://www.ltimindtree.com/about-us/")
    
    st.write("**Microsoft**")
    st.write("https://www.microsoft.com/en-in/about")
    
    st.write("**Cognizant**")
    st.write("https://www.cognizant.com/us/en/about-cognizant")
    
    st.write("**Honeywell**")
    st.write("https://www.honeywell.com/in/en/company/about-us")
    
    st.write("**Tech Mahindra**")
    st.write("https://www.techmahindra.com/en-in/techmahindra-overview/")
    
    st.write("**DXC Technology**")
    st.write("https://dxc.com/in/en/about-us")
    
    st.write("**Hexaware Technologies**")
    st.write("https://hexaware.com/about-us/")
    
    st.write("**PayPal**")
    st.write("https://www.paypal.com/va/webapps/mpp/about")
    
    st.write("**NTT DATA**")
    st.write("https://www.nttdata.com/global/en/about-us")
    
    st.write("**Atos-Syntel**")
    st.write("https://atos.net/en/")
    
    st.write("**Capgemini**")
    st.write("https://www.capgemini.com/about-us/#:~:text=Capgemini%20partners%20with%20companies%20to,for%20more%20than%2050%20years.")
    
    st.write("**ADP**")
    st.write("https://in.adp.com/about-adp.aspx")
    
    st.write("**Sopra Steria**")
    st.write("https://www.soprasteria.com/about-us")
    
    st.write("**Thoughtworks**")
    st.write("https://www.thoughtworks.com/en-in/about-us")
    
    st.write("**EY**")
    st.write("https://www.ey.com/en_in/about-us")
    
   
    st.write("**Deloitte**")
    st.write("https://www.deloitte.com/an/en/about.html")
    
    st.write("**Barclays**")
    st.write("https://www.barclays.in/home/about-us/#:~:text=Barclays%20Bank%20plc%2C%20which%20has,of%20offshore%20bonds%20in%202012.")
    
    st.write("**Alstom**")
    st.write("https://www.alstom.com/")
   
    st.write("**Daimler**")
    st.write("https://www.daimlertruck.com/en/company")

    st.write("**seimen**")
    st.write("https://www.tcs.com/who-we-are")

    st.write("**Gestamp**")
    st.write("https://www.gestamp.com/about-us#:~:text=Gestamp%20is%20an%20international%20group,manufacture%20of%20metal%20automotive%20components.")

    st.write("**Royal Enfield**")
    st.write("https://store.royalenfield.com/en/about-us")
    
    st.write("**Qualcom**")
    st.write("https://www.qualcomm.com/company#:~:text=Qualcomm%20is%20a%20company%20of,in%20more%20than%2030%20countries.&text=Our%20people%20are%20committed%20to,the%20world%20a%20better%20place.")
    
    st.write("**Hitachi**")
    st.write("https://www.globaldata.com/company-profile/hitachi-ltd/")
    
    st.write("**Micron**")
    st.write("https://www.micron.com/about#:~:text=Micron%20began%20in%201978%20as,the%20world's%20smallest%20256K%20DRAM.")
    
    st.write("**L&T**")
    st.write("https://www.larsentoubro.com/corporate/about-lt-group/")
    
    st.write("**Flex**")
    st.write("https://flex.com/company")
    
   

    

# Render page layout
page_layout()


