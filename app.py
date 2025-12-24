import streamlit as st
from jinja2 import Template

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Resume Generator",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Resume Generator")
st.write("Create a professional resume instantly")

# ---------------- USER INPUT ----------------
st.subheader("Personal Information")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

st.subheader("Professional Details")

skills = st.text_area("Skills (comma separated)")
education = st.text_area("Education")
experience = st.text_area("Experience")
projects = st.text_area("Projects")

template = st.selectbox(
    "Choose Resume Template",
    ["classic", "modern"]
)

# ---------------- GENERATE RESUME ----------------
if st.button("📄 Generate Resume"):

    if not name:
        st.warning("Please enter your name")
        st.stop()

    # Load HTML template
    with open("resume_template.html", "r", encoding="utf-8") as f:
        template_html = Template(f.read())

    # Load CSS
    with open("assets/style.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Render HTML
    html_content = template_html.render(
        name=name,
        email=email,
        phone=phone,
        skills=skills,
        education=education,
        experience=experience,
        projects=projects,
        template=template,
        css=css
    )

    # Preview Resume
    st.subheader("📄 Resume Preview")
    st.components.v1.html(html_content, height=800, scrolling=True)

    # Download Resume
    st.download_button(
        label="⬇️ Download Resume (HTML)",
        data=html_content,
        file_name="resume.html",
        mime="text/html"
    )
