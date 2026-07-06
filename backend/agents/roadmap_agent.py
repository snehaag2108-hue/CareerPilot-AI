from backend.tools.gemini import gemini


class RoadmapAgent:

    def generate_roadmap(self, goal):

        prompt = f"""
You are a Senior Mentor.

Create a detailed roadmap for

{goal}

Include

Month-wise learning

Projects

Books

Courses

Certificates

Practice Platforms

Interview Preparation

Timeline

Be extremely detailed.
"""

        return gemini.generate(prompt)


roadmap_agent = RoadmapAgent()