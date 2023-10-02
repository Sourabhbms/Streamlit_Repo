import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sourabh :wave:")
    st.title("A Data Engineer From India")
    st.write(
        "I am an IT professional with more than 12 years of full cycle software development experience in building large scale distributed polyglot persistence enterprise systems. Spearheaded multiple large data project \
migrations from on-premises to Multi Cloud (Azure/GCP) and Relational to NoSQL databases. Strong \
track record of building and leading high-performing teams focused on achieving great results ranging \
from broad IT transformation, to global enterprise data platforms, to targeted solutions using data at \
scale. Experience in building and leading large Agile teams (team size of 10+), grooming & mentoring \
second level leads Architects and Project Managers, participate in organizational strategic initiatives \
drives, publications / branding for the group and team. Interest includes designing new or improving \
existing Relational and Big Data warehouse systems on premises and on cloud"
    )
    st.write("[My Github >](https://github.com/Sourabhbms)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Design and develop Data Pipelines in Azure by using Azure Data Factory , Azure Databricks
            Worked extensively on Pyspark and sql and develped Lakehouse , Medaliion Architecture
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    #text_column, image_column = st.columns((1, 2))
    # with image_column:
    #     st.image(img_lottie_animation)
    #with text_column:
    st.subheader(" Siemens Gamesa Common Data Platform")
    st.write(
            """
            Lead a team of 10+ Data Engineer and Api developer as a Data Architect to make the world a bit livable 
by helping Gamesa Corporation to identify underperforming Turbines and reduce the cost of logistics 
using Data as a fuel, providing platform as product and develop data quality framework using python 
and azure stack to integrate Wind Turbine data from multiple pods and provide quality data as a 
product to different teams. Help Capgemini to hire Azure developers and train the new engineers.
Design and develop Data Quality framework to perform semantic checks andbusiness rule validations 
against multiple sources of data. Design and develop micro services with python, flask, cosmos dB, and
kubernetes.
Develop framework to pull data from on premise postgress tables to synapse, excel to cosmos.Designed
and developed API to post and consume from Cosmos Collections.
Conduct scrum call and help product owners maintain user stories in Azure Board.
Helped the pre-salesteam to write good quality RFPs and suggest applicable technology stack to Unisys
and Shell.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
#         st.write(
#             """
#             Want to add a contact form to your Streamlit website?
#             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/d741cf0753e91bfd1e197d1fde03c616" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
