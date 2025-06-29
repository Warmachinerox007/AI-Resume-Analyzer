import fitz  # PyMuPDF
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Example skill keywords (customize this list as needed)
COMMON_SKILLS = [
    "python", "machine learning", "deep learning", "pandas", "numpy",
    "tensorflow", "keras", "opencv", "nlp", "sql", "power bi", "excel",
    "tableau", "matplotlib", "scikit-learn", "git", "flask", "django"
]

def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(resume_text):
    doc = nlp(resume_text.lower())
    extracted_skills = []

    for token in doc:
        if token.text in COMMON_SKILLS:
            extracted_skills.append(token.text)

    return list(set(extracted_skills))
