from fpdf import FPDF
import os

def create_resume(name, email, phone, summary, experience, education, cgpa, skills, languages, certifications, projects, industry_visits, achievements, photo_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    if photo_path and os.path.exists(photo_path):
        pdf.image(photo_path, x=160, y=10, w=30)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", style='B', size=22)
    pdf.cell(0, 15, name, ln=True, align='L')
    
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 8, f"Email: {email}", ln=True, align='L')
    pdf.cell(0, 8, f"Phone: {phone}", ln=True, align='L')
    pdf.ln(10)
    
    sections = [
        ("Summary", summary),
        ("Experience", '\n'.join(experience)),
        ("Education", '\n'.join(education)),
        ("CGPA", cgpa),
        ("Skills", ', '.join(skills)),
        ("Known Languages", ', '.join(languages)),
        ("Certifications", '\n'.join(certifications)),
        ("Projects", '\n'.join(projects)),
        ("Industry/Institute Visits", '\n'.join(industry_visits)),
        ("Achievements", '\n'.join(achievements)),
    ]
    
    for title, content in sections:
        if content.strip():
            pdf.set_font("Helvetica", style='B', size=14)
            pdf.cell(0, 10, title, ln=True, align='L')
            pdf.set_font("Helvetica", size=12)
            pdf.multi_cell(0, 8, content.strip())
            pdf.ln(5)
    
    pdf.output("resume.pdf")
    print("Resume saved as resume.pdf")

if __name__ == "__main__":
    os.system("clear")  # Clears the screen in Termux
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
    photo_path = input("Enter the file path of your photo (leave blank if none): ").strip()
    
    create_resume(name, email, phone, summary, experience, education, cgpa, skills, languages, certifications, projects, industry_visits, achievements, photo_path)
