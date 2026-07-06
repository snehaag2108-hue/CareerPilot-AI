from backend.tools.pdf_reader import pdf_reader
from backend.tools.gemini import gemini


class ResumeAgent:

    def analyze_resume(self, pdf_path: str):

        resume_text = pdf_reader.extract_text(pdf_path)

        prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze this resume carefully.

Return your response in the following format.

Resume Score:
Overall Summary:
Strengths:
Weaknesses:
Missing Skills:
Projects to Add:
Certifications Recommended:
ATS Improvements:
Final Advice:

Resume:

{resume_text}
"""

        return gemini.generate(prompt)


resume_agent = ResumeAgent()