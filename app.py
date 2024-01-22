from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "file" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTING ---

PAGE_TITLE = "Digital CV 13 | Herbert Nascimento"
PAGE_ICON = ":rocket:"
NAME = "Herbert Nascimento"
DESCRIPTION = """BUSINESS INTELLIGENCE | ANALYTICS | BUSINESS DEVELOPMENT"""
EMAIL = "herbert.a.nascimento@gmail.com"
SOCIAL_MEDIA = {
    "🛠️ LinkedIn": "https://www.linkedin.com/in/herbert-nascimento-017848a/",
    "🐱Github": "https://github.com/HACN85",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# LOAD CSS, PDF & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="🗂️ Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📧", EMAIL)

        # --- SOCIAL LINKS ---
        st.write("#")
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️+12 years of experience working with Business Intelligence
- ✔️Professional with strong problem-solving skills and Results oriented
- ✔️Management of projects for sales growth in Latin America and EMEA
- ✔️Management projects with limited resources and deadline   
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write(
    """
- 🖥️ Programming: Python, SQL, VBA
-  🗠 Data Visualization: PowerBi, Tableau, Excel
- 📐 Modeling: Logistic regression, linear regression, decision trees
- 🗃️ Databases: MySQL
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")

# --- JOB 1
st.write("🏢", "**Medtronic - UK**")
st.write("🧑🏾‍💻", "**Senior Contract Compliance Analyst | Business Intelligence**")
st.write("2022 - Present")
st.write(
    """
- ► Conducted data cleaning, transformation, and validation using SQL queries
- ► Utilized Power BI to visualize and communicate findings to executive leadership
- ► Collaborated with teams to automate reporting processes, reducing manual effort by 80% """
)
st.write("---")
# --- JOB 2
st.write("🏢", "**Medtronic - LATAM**")
st.write("🧑🏾‍💻", "**Business Intelligence Specialist **")
st.write("2019 - 2022")
st.write(
    """
- ► Constructed impactful reports to advise Business Units using market insights and product analysis, guiding risk mitigation and performance enhancement strategies.
- ► Created market maps, identified opportunities, and assessed market share and competitive advantages, developing innovative strategies for the company.
- ► Developed tools for market analysis, monitoring performance in audited and import markets, ensuring goal achievement.
- ► Aligned with macro, technological, procedural, and competitive trends, understanding their influence on markets.
- ► Led cross-functional processes to synchronize data, key assumptions, and outputs.
- ► Integrated internal and external market research as needed for informed decision-making.
"""
)
st.write("---")
# --- JOB 3
st.write("🏢", "**Bunzl Healthcare - BRAZIL**")
st.write("🧑🏾‍💻", "**Product & Marketing Intelligence Manager**")
st.write("2017 - 2018")
st.write(
    """
- ► Strengthened brand and executed successful product launches by strategizing positioning tactics.
- ► Constructed insightful reports, utilizing market data and product analysis to advise business teams and the Board, minimizing risk and enhancing performance.
- ► Managed budgeting and forecasting through detailed analysis, aiding the Company and relevant departments.
- ► Created market maps, identified opportunities, analyzed market share, and crafted innovative strategies leveraging competitive advantages.
- ► Developed tools for market analysis, tracking performance in audited and import markets, ensuring goal attainment. """
)
st.write("---")
# --- JOB 4
st.write("🏢", "**Medtronic - LATAM**")
st.write("🧑🏾‍💻", "**Business Intelligence Analyst**")
st.write("2014 - 2017")
st.write(
    """
- ► Produced management reports utilizing Tableau for market opportunity mapping and competitive analysis, driving sales growth across Latin American countries.
- ► Led and mentored two interns during my tenure as an interim manager within the Business Intelligence department.
- ► Conducted in-depth analyses of the Hospital Market using public data sources, Ministry of Health, DataSUS, ANVISA, clinical protocols, and pricing databases.
- ► Managed data collection and assessed market potential, analyzing unaudited markets for strategic insights.
- ► Oversaw Distributors' and Representatives' sales and performance through data consolidation and analysis.
- ► Proficient in tools like Sigtap, Tabwin, Tabnet, Cnesweb, and Customs Base, leveraging them for comprehensive analysis.
- ► Created import reports, providing technical analysis of the competition.
- ► Provided marketing support by generating management reports and delivering presentations for internal and external stakeholders.
"""
)

# --- SOME PORTFOLIOS SAMPLE ---
st.write("#")
st.subheader("Some Portfolios Sample")

# --- Sales ---
st.write("## Sales")
st.write(
    "[Supermarket - Consumer purchasing habits](https://supermarketsales-kgtjrnuvkhyzwmqln2c8fz.streamlit.app/)"
)

# --- Game Sales Data Explorer ---
st.write("## Game Sales Data Explorer")
st.write("[Game Sales Data Explorer](https://gamesales-jbzmd2mtwqgmxsnn2v9s8j.streamlit.app/)")
