from resume_parser import extract_text_from_pdf, extract_skills
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract skills from job description
def extract_skills_from_job(job_text):
    doc = nlp(job_text.lower())
    common_skills = [
        "python", "machine learning", "deep learning", "pandas", "numpy",
        "tensorflow", "keras", "opencv", "nlp", "sql", "power bi", "excel",
        "tableau", "matplotlib", "scikit-learn", "git", "flask", "django"
    ]
    found = [token.text for token in doc if token.text in common_skills]
    return list(set(found))

# Sample usage
if __name__ == "__main__":
    # Step 1: Extract from resume
    resume_text = extract_text_from_pdf("sample_resume.pdf")
    resume_skills = extract_skills(resume_text)

    # Step 2: Paste job description here
    job_description = """
    We are hiring a data analyst with strong Python, SQL, and Excel skills.
    Experience with pandas, scikit-learn, Power BI, and machine learning is preferred.
    """

    # Step 3: Extract job skills and compare
    job_skills = extract_skills_from_job(job_description)
    matched = set(resume_skills).intersection(set(job_skills))
    missing = set(job_skills) - set(resume_skills)
    match_percentage = (len(matched) / len(job_skills)) * 100 if job_skills else 0

    # Step 4: Show results
    print("🔍 Job Skills:", job_skills)
    print("✅ Matched Skills:", list(matched))
    print("❌ Missing Skills:", list(missing))
    print(f"🎯 Match Percentage: {match_percentage:.2f}%")
