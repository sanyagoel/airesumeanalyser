from Agents.orchestrator import Orchestrator
import json

if __name__ == "__main__":
    orchestrator = Orchestrator() 

    result = orchestrator.run([
        {
            "role": "user",
            "content": {
                "file_path" : "./pdfs/Jane_Smith_Resume.pdf"
            }
        }
    ])
    
    print("------------------------------------------")

    print("EXTRACTION \n\n" , result["extraction"]["new_structure"][0]["content"])
    
    print("------------------------------------------")

    
    print("ANALYSIS \n\n", json.loads(result["analysis"]["analysed_structure"]))
    
    print("------------------------------------------")

    print("MATCHING \n\n", result["matching"]["matched_jobs"])
    
    print("------------------------------------------")

    print("SCREENING \n\n", result["screening"]["screening_report"][0]["content"])
    
    print("------------------------------------------")

    print("RECOMMENDATION \n\n", result["recommendation"]["final_recommendation"][0]["content"])
    
    print("------------------------------------------")

    
    