from fpdf import FPDF

def create_resume(name, email, phone, summary, experience, education, cgpa, skills, languages, certifications, projects, industry_visits, achievements, photo_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    if photo_path:
        pdf.image(photo_path, x=160, y=10, w=30)
    
    pdf.set_fill_color(30, 144, 255)  # Dodger blue header
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Courier", style='B', size=22)
    pdf.cell(0, 15, name, ln=True, align='L', fill=True)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Courier", size=12)
    pdf.cell(0, 8, email, ln=True, align='L')
    pdf.cell(0, 8, phone, ln=True, align='L')
    pdf.ln(10)
    
    sections = [
        ("Summary", summary, (255, 165, 0)),  # Orange
        ("Experience", '\n'.join(experience), (60, 179, 113)),  # Medium sea green
        ("Education", '\n'.join(education), (72, 61, 139)),  # Dark slate blue
        ("CGPA", cgpa, (255, 69, 0)),  # Red-orange
        ("Skills", ', '.join(skills), (0, 139, 139)),  # Dark cyan
        ("Known Languages", ', '.join(languages), (218, 165, 32)),  # Goldenrod
        ("Certifications", '\n'.join(certifications), (128, 0, 128)),  # Purple
        ("Projects", '\n'.join(projects), (0, 128, 0)),  # Green
        ("Industry/Institute Visits", '\n'.join(industry_visits), (255, 99, 71)),  # Tomato
        ("Achievements", '\n'.join(achievements), (30, 144, 255)),  # Dodger blue
    ]
    
    for title, content, color in sections:
        if content:
            pdf.set_fill_color(*color)
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Courier", style='B', size=14)
            pdf.cell(0, 10, title, ln=True, align='L', fill=True)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font("Courier", size=12)
            pdf.multi_cell(0, 8, content)
            pdf.ln(5)
    
    pdf.output("resume.pdf")
    print("Resume saved as resume.pdf")

if __name__ == "__main__":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    summary = input("Enter a brief summary: ")
    experience = input("Enter your experience (comma-separated): ").split(',')
    education = input("Enter your education (comma-separated): ").split(',')
    cgpa = input("Enter your CGPA: ")
    skills = input("Enter your skills (comma-separated): ").split(',')
    languages = input("Enter known languages (comma-separated): ").split(',')
    certifications = input("Enter certifications (comma-separated): ").split(',')
    projects = input("Enter projects (comma-separated): ").split(',')
    industry_visits = input("Enter industry/institute visits (comma-separated): ").split(',')
    achievements = input("Enter achievements (comma-separated): ").split(',')
    photo_path = input("Enter the file path of your photo (leave blank if none): ")
    
    create_resume(name, email, phone, summary, experience, education, cgpa, skills, languages, certifications, projects, industry_visits, achievements, photo_path)