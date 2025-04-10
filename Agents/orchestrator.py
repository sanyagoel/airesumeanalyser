from .baseagent import baseAgent

from .extractoragent import extractorAgent
from .analyzeragent import analyser
from .matcheragent import matcherAgent
from .screeneragent import screenerAgent
from .recommendationagent import recommendationAgent


class Orchestrator(baseAgent):
    
    def __init__(self):
        super().__init__(name = "Orchestrator", instructions  = """
                         
                         Coordinate the recruitment workflow and delegate tasks to specialized agents.
            Ensure proper flow of information between extraction, analysis, matching, screening, and recommendation phases.
            Maintain context and aggregate results from each stage."
                         
                         """)
        
        self.extractor = extractorAgent()
        self.analyzer = analyser()
        self.matcher = matcherAgent()
        self.screener = screenerAgent()
        self.recommender = recommendationAgent()
        
    
    async def run(self, messages : list):
        
        print("Extracting information....")
        data = await self.extractor.run(messages)
        
        print("Analysing information....")
        
        analysis = await self.analyzer.run([{
            
            "role" : "user",
            "content" : str(data["new_structure"])
        }])
        
        print("Matching information...")
        
        match = await self.matcher.run([{
            
            "role" :"user",
            "content": analysis["analysed_structure"]

            
        }])
        
        print("Screening user...")
        
        screen =await  self.screener.run([{
            
            "role" : "user",
            "content" : {
                "matched_jobs" : match["matched_jobs"],
                "user_profile" : match["user_profile"]
            }
            
        }])
        
        print("Making recommendations...")
        
        recommend = await self.recommender.run([
            
            {
                "role" : "user",
                "content" : screen["screening_report"]
            }
            
        ])
        
        return {
            "extraction": data,
            "analysis": analysis,
            "matching": match,
            "screening": screen,
            "recommendation": recommend,
            "status" : "completed"
        }
        
