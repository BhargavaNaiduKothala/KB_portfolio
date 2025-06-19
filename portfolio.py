import streamlit as st
# import PyPDF2
#import plotly.express as px
import base64

# --- Page config (must be first) ---
st.set_page_config(page_title="Bhargava Naidu | Portfolio", layout="wide")

# --- Helper to Extract PDF Text ---
# @st.cache_data
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         for page in reader.pages:
#             text += page.extract_text()
#     return text

# resume_path = r"C:\Users\91944\Downloads\resume\Guru2025.pdf"
# resume_text = extract_text_from_pdf(resume_path)

# --- Simulated Structured Resume Data ---
personal_info = {
    "name": "Kothala Bhargava Naidu:)",
    "title": "AI/ML Enthusiast & Data Science | Python Developer",#"AI/ML & Data Science | Python Developer"
    
    "summary": (
        "Summary:-\n\n"
        "👉 Driven by curiosity and precision, I build intelligent systems using Python, ML, and SQL. \n\n"
        "👉 I love exploring datasets, uncovering hidden insights, and using AI to make smart, data-driven decisions\n\n"
        "👉 Skilled in NLP, Neural Networks, and solving real-world problems with data.\n\n"
        
    ),

    "email": "bhargavnaidu2333@gmail.com",
    "linkedin": "https://www.linkedin.com/in/bhargavanaidu-kothala/",
    "github": "https://github.com/BhargavaNaiduKothala"
}

education = [
    {
        "degree": "B.Tech in Electrical and Electronics Engineering",
        "institution": "College: Miracle educational society group of institutions",
        "year": "2019 - 2022",  
    },
    
]


skills = {
    "Python": 90,
    "Machine Learning": 85,
    "Deep Learning": 70,
    "HTML/CSS": 70,
    "SQL": 65,
    "Streamlit": 80,
    "Pandas/Numpy": 85
}

# experience = [
#     {"year": "2025 - Present", "role": "SOftware Engineering", "company": "Lyrostech", "description": "Handled data analysis, Developed ML models, Done projects "},

#     {"year": 'Feb 2024  -Nov 2024', "role": "Freelance Content Reviewer", "company": "Centific", "description": "Developed ML models for clients."},

#     {"year": "2022 - 2024", "role": "Technical Assistant", "company": "RACEnergy", "description": "Handled data entry, troubleshooting, and documentation."}
# ]



experience = [
    {
        "year": "Feb 2025 - Present",
        "role": "Software Engineer",
        "company": "Lyrostech",
        "description": "Handled data analysis, developed ML models, and executed end-to-end projects."
    },
    
]

projects = [
    {
        "name": "🎓 Student Grading System",
        "desc": (
            "- Developed a Tkinter-based GUI to manage student marks\n"
            "- Implemented role-based access for admins and teachers\n"
            "- Used Pandas for data handling and predictive grade analysis"
        )
    },
    {
        "name": "🏠 Airbnb Price Prediction",
        "desc": (
            "- Built regression models to predict listing prices\n"
            "- Analyzed key features affecting price fluctuations\n"
            "- Enabled data-driven pricing recommendations"
        )
    },
    {
        "name": "🎬 Movie Recommendation System",
        "desc": (
            "- Utilized NLP techniques like CountVectorizer and TF-IDF\n"
            "- Calculated cosine similarity for personalized recommendations\n"
            "- Created a scalable model to suggest movies based on user preferences"
        )
    },
    {
        "name": "🔍 Customer Segmentation using Machine Learning and python",
        "desc": (
            "- Applied K-Means clustering to group customers\n"
            "- Analyzed behavioral patterns and demographics\n"
            "- Supported targeted marketing and business strategies"
        )
    }
]

# projects = [
#     {"name": " Student Grading System", "desc": "Tkinter app with Pandas, user roles, predictive analysis."},
#     {"name": " Airbnb Price Prediction", "desc": "ML models to forecast listing prices."},
#     {"name": " Movie Recommendation", "desc": "Collaborative filtering using cosine similarity."},
#     {"name": " Customer Segmentation using Machine Learning", "desc": "Applied clustering algorithms (e.g., K-Means) to segment customers based on behavioral patterns and demographics."}

# ]

# --- Sidebar Navigation ---
# st.sidebar.image("https://easydrawingguides.com/wp-content/uploads/2019/01/how-to-draw-thors-hammer-featured-image-1200.png"
# , width=140)

 


# st.sidebar.title("📌 Navigation")
# page = st.sidebar.radio("", ["About Me", "Skills", "Experience", "Projects", "Contact"])


# ------------side bar navigation 1, check up for the new one----
st.sidebar.title("📌 Navigation")

if 'page' not in st.session_state:
    st.session_state.page = "About Me"

if st.sidebar.button("About Me"):
    st.session_state.page = "About Me"
if st.sidebar.button("Education"):
    st.session_state.page = "Education"
if st.sidebar.button("Skills   "):
    st.session_state.page = "Skills"
if st.sidebar.button("Experience"):
    st.session_state.page = "Experience"
if st.sidebar.button("Projects"):
    st.session_state.page = "Projects"
if st.sidebar.button("Contact"):
    st.session_state.page = "Contact"

page = st.session_state.page
#------ side bar------------



# --- About Me ---
if page == "About Me":
    st.title(f"👋 Hi, I'm {personal_info['name']}")
    st.markdown(f"### {personal_info['title']}")
    # st.markdown(f"###### {personal_info['summary']}")
    st.info(personal_info['summary'])

    st.markdown(f"""
    *📧 Email:* [{personal_info['email']}](mailto:{personal_info['email']})  
    *🔗 LinkedIn:* [{personal_info['linkedin']}]({personal_info['linkedin']})  
    *💻 GitHub:* [{personal_info['github']}]({personal_info['github']})
    """)

# --- Education ---
elif page == "Education":
    st.header("🎓 Education")
    for edu in education:
        st.subheader(f"{edu['institution']}")
        st.markdown(f"{edu['degree']}")
        st.markdown(f"📅 {edu['year']}")
        
        #st.info(edu['details'])
        st.markdown("---")

# --- Skills ---
elif page == "Skills":
    st.header("🧠 Skills Overview")
    for skill, value in skills.items():
        st.markdown(f"{skill}")
        st.progress(value)

# --- Experience ---
elif page == "Experience":
    st.header("💼 Experience Timeline")

    for exp in experience:
        with st.container():
            st.subheader(f"{exp['role']} @ {exp['company']}")
            st.markdown(f"📅 {exp['year']}")
            st.write(exp['description'])
            st.markdown("---")

# elif page == "Experience":
#     st.header("💼 Experience Timeline")
#     cols = st.columns(len(experience))
#     for col, exp in zip(cols, experience):
#         col.markdown(f"{exp['year']}")
#         col.write(f"{exp['role']}** @ {exp['company']}")
#         col.caption(exp['description'])

# --- Projects ---
elif page == "Projects":
    st.header("🛠 Projects Showcase")
    for proj in projects:
        st.markdown(f"#### {proj['name']}")
        st.success(proj['desc'])

# --- Contact ---
elif page == "Contact":
    st.header("📬 Contact Me")
    contact_form = """
    <form action="https://formsubmit.co/bhargavnaidu2333@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px;"><br><br>
         <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px;"><br><br>
         <textarea name="message" placeholder="Your message" required style="width: 100%; padding: 10px;"></textarea><br><br>
         <button type="submit" style="padding: 10px 20px; background-color: teal; color: white;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown("\n\n 💡Tip: Replace your email with the one you want to receive messages on.")

# --- Footer ---
st.markdown("---")
# st.write("Crafted with precision and passion for 💖Python and Data Science. © 2025 Gurunath Tokala")
# st.write("Data speaks, Python listens, and 💖 I build. © 2025 Gurunath Tokala")
st.markdown("""
<div style="text-align:center; font-size:16px;">
   
</div>
""", unsafe_allow_html=True)
