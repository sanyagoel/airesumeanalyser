from .baseagent import baseAgent

import json 
from db.db_connection import db

jobs_collection = db['Jobs']

class matcherAgent(baseAgent):
    
     def __init__(self):
        super().__init__(
            
            name="matcher",
            instructions = """
            
            Match candidate profiles with job positions.
                Consider: skills match, experience level, location preferences.
                Provide detailed reasoning and compatibility scores.
                **IMPORTANT INSTRUCTION**
                **Return matches in **JSON format** with title, match_score, and location fields.**
                
            
            """
            
        )
    
     def run(self,messages : list):
        
        content = messages[-1].get("content")
        
               
        analy2 = json.loads(content)
        
        # print("ANALYSED CONTENT AAA", analy2)
        
        jobs = jobs_collection.find({"experience" : {"$lte" : analy2.get("years_of_experience")}, "expected_technical_skills" :{ "$in" : analy2.get("technical_skills")}})
        
        scored_jobs = []
        
        for job in jobs:
            required_skills = set(job["expected_technical_skills"])
            actual_skills = set(analy2.get("technical_skills"))
            matched_skills = len(required_skills.intersection(actual_skills))
            matched_score = (matched_skills/len(required_skills))*100
            if matched_score > 30:
                new_job = {
                "company" : job["company"],
                "key_responsiblities" : job["key_responsibilities"],
                "salary_range" : job["salary_expectations"],
                "location" : job["location"],
                "job_role" : job["job_role"] ,
                "match_score" : matched_score,
                "expected_technical_skills" : job["expected_technical_skills"]
                }
                scored_jobs.append(new_job)
                
        # scored_jobs.sort()
        # print(scored_jobs, "SCORED JOB  :D")   
        scored_jobs2 = sorted(scored_jobs, key = lambda job : job["match_score"], reverse=True) 
        # print(scored_jobs2, "SCORED JOBSSSSSS   :D")   

            
        return  {
                
                "matched_jobs" : scored_jobs2[:3],
                "number_of_matches" : len(scored_jobs),
                "user_profile" : analy2
                
                
            }
        
        
        
            

        
        
        