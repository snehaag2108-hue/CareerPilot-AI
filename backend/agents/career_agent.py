from backend.tools.gemini import gemini
from backend.tools.memory import memory


class CareerAgent:

    def suggest_career(self, skills, interests, experience):

        # Save the latest user interest
        memory.save("latest_interest", interests)

        # Load all saved memory
        saved_memory = memory.load()

        prompt = f"""
You are a professional Career Counselor.

Below is the user's saved information.

User Memory:
{saved_memory}

Current Skills:
{skills}

Current Interests:
{interests}

Experience:
{experience}

Based on this information, provide:

1. Best Career Paths
2. Why these careers are suitable
3. Expected Salary Range
4. Future Scope
5. Skills to Learn
6. Recommended Certifications
7. Projects to Build
8. A detailed 6-Month Learning Roadmap

Make the response well-structured and easy to read.
"""

        return gemini.generate(prompt)


career_agent = CareerAgent()