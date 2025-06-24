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
        "institution": " Miracle Educational Society Group Of Institutions",
        "year": "2019 - 2022",  
        "name": " **Optimal placement of  capacitor for loss reduction in Distribution system Using EPSO** ",
        "desc": (
            "Successfully implemented the EPSO algorithm to reduce electric losses in the distribution system by 15%,resulting in significant cost saving for the company.\n"
            "Designed and installed shunt capacitors that improved  power factor and reduced harmonic distribution in system ,resulting in improved power quality for customers.\n"
            "Developed software tools in c programming for data analysis and Simulation, which helped to identify and trouble shoot system issues more efficiently.\n"
            "Collaborated with a team of engineers to develop and implement system upgrades, resulting in improved reliability and reduced downtime. "

        )
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

experience = [
    {
        "year": "Feb 2025 - Present",
        "role": "Software Engineer",
        "company": "Lyrostech"
    },
    
    
]
exps = [
    {
        "name": "Machine Learning & AI Development",
        "desc": (
            "- Designed and implemented end-to-end machine learning pipelines (data collection, preprocessing, feature engineering, model training, and evaluation) for real-world AI applications.\n"
            "- Developed and fine-tuned supervised & unsupervised models (Regression, Classification, Clustering, NLP) using Scikit‑learn, TensorFlow, and PyTorch, improving model accuracy by 10%.\n"
            "- Optimized AI workflows by applying hyperparameter tuning, cross-validation, and ensemble techniques, reducing inference time by 12%."
        )
    },
    {
        "name": "Data Engineering & Analytics",
        "desc": (
            "- Built automated data pipelines (Pandas, NumPy, SQL) for cleaning and structuring large‑scale datasets, enhancing data processing efficiency by 15%.\n"
            "- Created interactive data visualizations (Matplotlib, Seaborn, Plotly) to extract insights and support decision‑making.\n"
            "- Performed statistical analysis (hypothesis testing, A/B testing) to validate model performance and business impact."
        )
    },
    {
        "name": "MLOps & Deployment",
        "desc": (
            "- Deployed ML models as scalable APIs using Flask, FastAPI, and Streamlit for user‑friendly interfaces.\n"
            "- Containerized applications with Docker and orchestrated microservices using Minikube (Kubernetes).\n"
            "-Managed CI/CD workflows via GitHub Actions and cloud deployment on Render."
        )
    },
    {
        "name": "Collaboration & Best Practices",
        "desc":( 
            "-Followed Agile methodologies for project tracking (Jira, GitHub Projects).\n"
            "-Documented experiments using MLflow/Weights & Biases (W&B) for reproducibility.\n"
            "-Conducted code reviews and maintained version control (Git/GitHub).\n"
        )
    }
]






projects = [
    {
        "name": "🎓 Student Grading System",
        "overview": (
            "A desktop application for managing student records and roles, "
            "featuring predictive analytics for grades."
        ),
        "desc": (
            "- Developed a Tkinter-based GUI to manage student marks\n"
            "- Implemented role-based access for admins and teachers\n"
            "- Used Pandas for data handling and predictive grade analysis"
        ),
        "tools": ["Python", "Tkinter", "Pandas", "Scikit-learn", "SQLite", "pytest"]
    },
    {
        "name": "🏠 Airbnb Price Prediction",
        "overview": (
            "A data-driven model to predict Airbnb listing prices, "
            "highlighting key factors that influence pricing."
        ),
        "desc": (
            "- Built regression models to predict listing prices\n"
            "- Analyzed key features affecting price fluctuations\n"
            "- Enabled data-driven pricing recommendations"
        ),
        "tools": ["Python", "Pandas", "Scikit-learn", "XGBoost", "Matplotlib", "Jupyter"]
    },
    {
        "name": "🎬 Movie Recommendation System",
        "overview": (
            "An NLP‑based recommendation engine suggesting movies "
            "based on user preferences using content similarity."
        ),
        "desc": (
            "- Utilized NLP techniques like CountVectorizer and TF-IDF\n"
            "- Calculated cosine similarity for personalized recommendations\n"
            "- Created a scalable model to suggest movies based on user preferences"
        ),
        "tools": ["Python", "Scikit-learn", "NLTK", "Pandas", "Streamlit", "Docker"]
    },
    {
        "name": "🔍 Customer Segmentation",
        "overview": (
            "A clustering-driven segmentation pipeline that "
            "segments customers for tailored marketing strategies."
        ),
        "desc": (
            "- Applied K-Means clustering to group customers\n"
            "- Analyzed behavioral patterns and demographics\n"
            "- Supported targeted marketing and business strategies"
        ),
        "tools": ["Python", "Pandas", "Scikit-learn", "Seaborn", "Plotly", "Streamlit"]
    }
]



st.sidebar.title("📌 Bhargava Naidu Kothala")

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
        st.subheader(f"{edu['degree']}")
        st.markdown(f"{edu['institution']}")
        st.markdown(f"📅 {edu['year']}")
        st.markdown(f" ***ACADAMIC PROJECT:*** {edu['name']}")
    
        
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
            # st.write(exp['description'])
            st.markdown("---")
    for proj in exps:
        st.markdown(f"#### {proj['name']}")
        st.success(proj['desc'])

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
        st.markdown(f"Overview: {proj['overview']}")
        st.markdown(f"{proj['desc']}")
        st.success(f"Tools: {proj['tools']}")

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

