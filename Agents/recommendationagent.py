from .baseagent import baseAgent


class recommendationAgent(baseAgent):
    
     def __init__(self):
        super().__init__(
            
            name = "recommendation",
            instructions = """
You are a career coach helping a job seeker improve their resume and job readiness.

Here’s what you have:
- Their extracted profile (education, experience, skills)
- Skill analysis and gaps
- Job matches (roles they're interested in)
- Screening feedback (issues or alignment)

Your task:
- Give clear and personalized advice on how they can improve their resume and job alignment.
- Suggest what skills to highlight, what to add/remove, or reword in their resume.
- Recommend concrete next steps (e.g., upskilling, changing focus, applying to certain roles).
- Write your response like a human career consultant — DO NOT provide code or implementation logic.
"""

            
            
        )
    
     async def run(self, messages : list):
        
        content = messages[-1].get("content")[0].get("content")
        
        # print("CONTENT >>>", content)
        
        response = self.query_ollama(content)
        
        return {
            "final_recommendation" : response,
             "current_stage" : "completed",
             "status" : "completed"
        }