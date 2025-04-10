from .baseagent import baseAgent

class analyser(baseAgent):
    
     def __init__(self):
    
        super().__init__(
            name = "analyzer",
            instructions= """Analyze candidate profiles and extract:
                1. Technical skills (as a list)
                2. Years of experience (numeric)
                3. Education level
                4. Experience level (Junior/Mid-level/Senior)
                5. Key achievements (Based on her experiences or (achievements if explicitly mentioned in the data.))
                6. Domain expertise (Based on her experiences, her skills, or if domain expertise explicity mentioned. )
                
                Format the output as structured data."""
        )
    
     async def run(self,messages : list):
        
        content = messages[-1].get("content")
        
        prompt =f"""
        
         Analyze this resume data and return a JSON object with the following structure:
        {{
            "technical_skills": ["skill1", "skill2"],
            "years_of_experience": number,
            "education": {{
                "level": "Bachelors/Masters/PhD",
                "field": "field of study"
            }},
            "experience_level": "Junior/Mid-level/Senior",
            "key_achievements": ["achievement1", "achievement2"],
            "domain_expertise": ["domain1", "domain2"]
        }}

        Resume data:
        {content}

        **Return ONLY the JSON object, no other text.**
        
        """
        
        response = self.query_ollama(prompt)
        
        # print(response, 'AAAAAAAAAAAAAAAAAAA')
        response2 = self.helpJson(response[0].get("content"))
        # print('Analysed Response AAAAAA',response2)
        
        return {
            "analysed_structure" : response2,
            "analysis" : "done",
            "current_stage" : "matching"
        }
        
    
     def helpJson(self,data):
         
         try:
         
            start = data.find('{')
            end = data.rfind('}')
            
            if(start!=-1 and end!=-1):
                data2 = data[start : end + 1]
                return data2
         
         except Exception as e:
             print(e)
    
    