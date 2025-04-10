from Agents.orchestrator import Orchestrator
import json
import streamlit as st
from streamlit_option_menu import option_menu
import asyncio


async def process_resume(filepath):
    
    try:
        
      orchestrator = Orchestrator() 

        
      result = await  orchestrator.run([
        {
            "role": "user",
            "content": {
                "file_path" : "./pdfs/Resume3.pdf"
            }
        }])
      
      return result;        
        
    except Exception as e:
        st.error('Something went wrong....')
        return {"status": "failed", "current_stage": "process_resume", "error": str(e)}


if __name__ == "__main__":
    
    if 'page' not in st.session_state:
        st.session_state.page = "About me"
        
    
    st.markdown("""
                
         <style>
         
            .custom-title{
             color: pink;
             margin-top : 90px;
             margin-bottom : 30px;
             font-size : 2em;
             font-weight : bold;
         }
         
         </style>     
                
                """, unsafe_allow_html=True)
    
    
    
    with st.sidebar:
        
        st.markdown("""<div class="custom-title">AI Recruiter Agency</div>""", unsafe_allow_html=True)
        selected = option_menu("Navigation", ["About me", 'Upload'], 
            icons=['house', 'upload'], menu_icon="cast", default_index=0)
        
    
    if selected == 'About me':
        st.session_state.page = 'About me'
    elif selected == 'Upload':
        st.session_state.page = 'Upload'
  
        
    if st.session_state.page == 'Upload':
        st.markdown("""Upload your resume here...""")
        uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
        if uploaded_file is not None:
            with st.spinner("Saving uploaded file..."):
                f = open('./pdfs/Resume3.pdf',"wb")
                f.write(uploaded_file.getbuffer())
                f.close()
                st.success('Saved as resume3 in ./pdfs/resume3')
            st.info('Your file has been saved succesfully!')
            progress_bar = st.progress(0)
            status_text = st.empty()
            try:
                progress_bar.progress(25)
                status_text.text('Text extracted, now matching...')
                result = asyncio.run(process_resume('./pdfs/Resume3.pdf'))
                if result["status"] == 'completed':
                    progress_bar.progress(100)
                    status_text.text('Analysis complete!')
                    tab1, tab2, tab3,tab4 = st.tabs(["Information", "Matching", "Screening","Recommendation"])
                    with tab1:
                        st.header("Information On The Resume")
                        st.markdown(f"""
                                    
                                    {result["analysis"]}    
                                    
                                    """)
                    with tab2:
                        st.header("Matches with Potential Jobs")
                        st.markdown(f"""
                                    
                                    {result["matching"]}    
                                    
                                    """)
                    with tab3:
                        st.header("Screening Information")
                        st.markdown(f"""
                                    
                                    {result["screening"]}    
                                    
                                    """)
                    with tab4:
                        st.header("Recommendations")
                        st.markdown(f"""
                                    
                                    {result["recommendation"]}    
                                    
                                    """)
            except Exception as e:
                st.error(e)

            
   
        
    
    elif st.session_state.page =='About me':
        st.markdown("""Welcome to AI Recruiter Agency. """)
        st.markdown("""
                    
 <b><h1>🤖 AI Recruiter Agency</h1></b>
                    
An end-to-end intelligent recruitment assistant that automates resume parsing, job matching, screening, and personalized recommendations using a swarm of AI agents. This system simulates a real-world recruiting agency — from analyzing candidate profiles to providing clear recommendations for hiring success.

<h2 style='font-weight: bold;'>🧠 Core Features</h2>

<ol style='line-height: 1.6;'>
  <li><span style='font-size: 1.1em; font-weight: 600;'>Resume Extraction</span><br>
      Extracts detailed candidate information like skills, experience, education, and achievements from PDFs using LangChain's community loader.
  </li>
  <li><span style='font-size: 1.1em; font-weight: 600;'>Profile Analysis</span><br>
      Breaks down strengths, weaknesses, and improvement areas based on extracted data.
  </li>
  <li><span style='font-size: 1.1em; font-weight: 600;'>Job Matching</span><br>
      Compares candidate profiles with available job descriptions and calculates a match score.
  </li>
  <li><span style='font-size: 1.1em; font-weight: 600;'>Candidate Screening</span><br>
      Evaluates qualifications, experience, skill alignment, red flags (like long employment gaps), and cultural fit.
  </li>
  <li><span style='font-size: 1.1em; font-weight: 600;'>Final Recommendations</span><br>
      Provides personalized suggestions and next steps to enhance resume and job readiness.
  </li>
</ol>

<h2 style='font-weight: bold;'>🛠️ Tech Stack</h2>

<ul style='line-height: 1.6; list-style-type: disc;'>
  <li><span style='font-size: 1.05em; font-weight: 500;'>Python</span></li>
  <li><span style='font-size: 1.05em; font-weight: 500;'>Swarm Framework</span> – for agent creation and orchestration</li>
  <li><span style='font-size: 1.05em; font-weight: 500;'>LangChain</span> – with community loader for PDF parsing</li>
  <li><span style='font-size: 1.05em; font-weight: 500;'>Ollama</span> – using locally downloaded LLaMA model instead of OpenAI</li>
  <li><span style='font-size: 1.05em; font-weight: 500;'>MongoDB Atlas</span> – for storing and retrieving job data for matching with resumes</li>
  <li><span style='font-size: 1.05em; font-weight: 500;'>Modular Agent System</span> – includes baseAgent, orchestrator, etc.</li>
</ul>

                    
                    """,unsafe_allow_html=True)
       
    
        
        
    
    
    
    # print("------------------------------------------")

    # print("EXTRACTION \n\n" , result["extraction"]["new_structure"][0]["content"])
    
    # print("------------------------------------------")

    
    # print("ANALYSIS \n\n", json.loads(result["analysis"]["analysed_structure"]))
    
    # print("------------------------------------------")

    # print("MATCHING \n\n", result["matching"]["matched_jobs"])
    
    # print("------------------------------------------")

    # print("SCREENING \n\n", result["screening"]["screening_report"][0]["content"])
    
    # print("------------------------------------------")

    # print("RECOMMENDATION \n\n", result["recommendation"]["final_recommendation"][0]["content"])
    
    # print("------------------------------------------")

    
    