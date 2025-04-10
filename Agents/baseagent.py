from openai import OpenAI
from swarm import Agent, Swarm


class baseAgent():
    
    def __init__(self,name : str,instructions : str):
        self.name = name
        self.instructions = instructions
        self.ollamaclient =  OpenAI(base_url='http://localhost:11434/v1',api_key='ollama')
        self.swarm = Agent(
            name=self.name,
            instructions = self.instructions,
            model = 'llama3.2'
        )
        
        self.client = Swarm(client = self.ollamaclient)
        
    async def run(self,messages : list):
        
       
        raise NotImplementedError('Every subclass needs to implement this.')
    
    def query_ollama(self,prompt : str):
        
        response = self.client.run(agent = self.swarm, messages  = [{
            "role":"user",
            "content" : prompt
        }])
        
        return response.messages
        
       