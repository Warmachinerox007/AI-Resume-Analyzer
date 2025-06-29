from resume_parser import extract_text_from_pdf, extract_skills

text = extract_text_from_pdf("sample_resume.pdf")
skills = extract_skills(text)

print("Extracted Skills from Resume:")
print(skills)
