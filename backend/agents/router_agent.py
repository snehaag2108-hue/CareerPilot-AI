class RouterAgent:

    def route(self, user_input: str):

        message = user_input.lower()

        if any(word in message for word in [
            "resume",
            "cv",
            "ats"
        ]):
            return "resume"

        elif any(word in message for word in [
            "career",
            "job",
            "future",
            "role"
        ]):
            return "career"

        elif any(word in message for word in [
            "interview",
            "questions",
            "mock"
        ]):
            return "interview"

        elif any(word in message for word in [
            "roadmap",
            "study",
            "learn",
            "plan"
        ]):
            return "roadmap"

        return "career"


router_agent = RouterAgent()