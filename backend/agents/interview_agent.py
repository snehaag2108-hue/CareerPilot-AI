from backend.tools.gemini import gemini


class InterviewAgent:

    def generate_questions(self, role):

        prompt = f"""
You are an Interview Coach.

Generate

15 Interview Questions

for

{role}

Also provide

• Expected Answer

• Difficulty

• Tips

Format properly.
"""

        return gemini.generate(prompt)


interview_agent = InterviewAgent()