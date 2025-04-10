from .baseagent import baseAgent


class screenerAgent(baseAgent):
    
     def __init__(self):
        super().__init__(
            
            name = "screener",
            instructions = """
            
            Screen candidates based on:
                - Qualification alignment
                - Experience relevance
                - Skill match percentage
                - Cultural fit indicators
                - Red flags or concerns (You need to give red flags or concerns based on maybe their lack of any technical skills, or long break between jobs, or anything past  bad history etc.)
                Provide comprehensive screening reports.
            
            """
            
        )
    
     async def run(self,messages : list):
        
        content = messages[-1].get("content")
        
        userprofile = content.get("user_profile")
        job_matches = content.get("matched_jobs")
        
        
        # print('USER PROFILE HERE IT IS', userprofile)
        # print('JOB MATCHESS HERE IT IS', job_matches)
        
        prompt = f"""
        You are a candidate screener tasked with evaluating a job applicant against potential job matches.

        Below is the candidate profile:
        {userprofile}

        Below are the job matches (including role, location, expected skills, etc.):
        {job_matches}

        Your task:
        - Analyze how well the candidate aligns with each job.
        - Assess qualifications, experience relevance, and technical skill match.
        - Comment on cultural fit (based on soft skills, achievements, etc.).
        - Point out any red flags (e.g. skill gaps, career breaks, lack of experience, or mismatch in domain).
        - Provide a clear, professional screening report (not code), written in natural language.

        Only provide the screening report, no explanations or Python code.
    """
        
        response = self.query_ollama(prompt)
        # print(response, 'SCREENING OUTPUT LETS SEE')
        
        return {
            "screening_report" : response,
             "current_stage" : "recommendation"
        }
        
        