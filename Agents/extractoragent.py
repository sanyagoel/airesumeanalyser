from .baseagent import baseAgent

from langchain_community.document_loaders import PDFMinerLoader

from pdfminer.high_level import extract_text

import os


class extractorAgent(baseAgent):
    
     def __init__(self):
    
        super().__init__(
            
            name = "extractor",
            instructions= """Extract and structure information from resumes.
                Focus on: personal info, work experience, education, skills, and certifications.
                Provide output in a clear, structured format."""
            
        )
    
     def run(self, messages : list):
        
        """process resume and extract information"""
        
        resume_data = messages[-1].get("content")
        
        if not os.path.exists(resume_data["file_path"]):
            print('the file isnt valid')
           

        
        data = extract_text(resume_data["file_path"])
        
        result = self.query_ollama(data)
        
        return {
            "old_structure" : data,
            "new_structure" : result,
            "extraction" : "completed"
        }
        
        
        
        
