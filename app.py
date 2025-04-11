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
        
        upload_instruction = st.empty()
        uploaded_file_p = st.empty()
        status_placeholder = st.empty()
        progress_bar_p = st.empty()
        suc = st.empty()

        upload_instruction.markdown("""Upload your resume here...""")
        uploaded_file = uploaded_file_p.file_uploader('Choose your .pdf file', type="pdf")
        if uploaded_file is not None:
            with st.spinner("Saving uploaded file..."):
                f = open('./pdfs/Resume3.pdf',"wb")
                f.write(uploaded_file.getbuffer())
                f.close()
                suc.success('Saved as resume3 in ./pdfs/resume3')
            status_placeholder.info('Your file has been saved succesfully!')
            progress_bar = progress_bar_p.progress(0)
            status_text = st.empty()
            progress_bar.progress(25)
            status_text.text('Text extracted, now matching...')
            result = asyncio.run(process_resume('./pdfs/Resume3.pdf'))
            if result["status"] == 'completed':
                    progress_bar.progress(100)
                    status_text.text('Analysis complete!')
                    upload_instruction.empty()
                    uploaded_file_p.empty()
                    status_text.empty()
                    status_placeholder.empty()
                    progress_bar_p.empty()
                    suc.empty()
                    
                    
                    
                    if isinstance(result.get("analysis"), str):
                        result["analysis"] = json.loads(result["analysis"])
                        
                    if isinstance(result["analysis"].get("analysed_structure"), str):
                        result["analysis"]["analysed_structure"] = json.loads(result["analysis"]["analysed_structure"])


                    tech_skills = result["analysis"]["analysed_structure"]["technical_skills"]
                    skill_summary = "\n".join(f"• {skill}" for skill in tech_skills)

                    yearsOfExp = result["analysis"]["analysed_structure"]["years_of_experience"]

                    education = (
                        result["analysis"]["analysed_structure"]["education"]["level"]
                        + ": "
                        + result["analysis"]["analysed_structure"]["education"]["field"]
                    )

                    key_achievements = "\n".join(
                        f"• {achievement}" for achievement in result["analysis"]["analysed_structure"]["key_achievements"]
                    )

                    exp_level = result["analysis"]["analysed_structure"]["experience_level"]

                    domain_expertise = "\n".join(
                        f"• {domain}" for domain in result["analysis"]["analysed_structure"]["domain_expertise"]
                    )
                    
                    print("MATCHING DEBUG:", result["matching"])

                    matched_jobs = result["matching"]["matched_jobs"]
                    html = ""

                    if matched_jobs:
                        html = """<table style="width:100%; border-collapse: collapse; font-size: 16px;">
<thead>
<tr style="font-weight:bold; text-align:left;">
<td>Company</td>
<td>Job Role</td>
<td>Location</td>
<td>Salary</td>
<td>Match Score</td>
<td>Responsibilities</td>
</tr>
</thead>
<tbody>
                        """

                        for job in matched_jobs:
                            html += f"""<tr>
<td>{job['company']}</td>
<td>{job['job_role']}</td>
<td>{job['location']}</td>
<td>{job['salary_range']}</td>
<td>{round(job['match_score'], 2)}%</td>
<td>{'<br>'.join(job['key_responsiblities'])}</td>
</tr>
                        """

                        html += "</tbody></table>"
                    
                    screeningReport = result["screening"]["screening_report"][0]["content"].replace('\n','<br>')
                    
                    recommendations = result["recommendation"]["final_recommendation"][0]["content"].replace('\n','<br>')


                    tab1, tab2, tab3,tab4 = st.tabs(["Information", "Matching", "Screening","Recommendation"])
                    with tab1:
                        st.header("Information On The Resume")
                        st.markdown(f"""
                                                                        
                                   <b><h4> Technical Skills- </h4></b>
                                    {skill_summary}
                                    <b><h4> Years Of Experience : {yearsOfExp} </h4></b>
                                    <b><h4> Education- </h4></b>
                                    {education}
                                    <b><h4> Key Achievements </h4></b>
                                    {key_achievements}
                                    <b><h4> Experience Level </h4></b>
                                    {exp_level}
                                    <b><h4> Domain Expertise- </h4></b>
                                    {domain_expertise}
                                    
                                    """,unsafe_allow_html=True)
                    with tab2:
                        st.header("Matches with Potential Jobs")
                        st.markdown(html, unsafe_allow_html=True)
                    with tab3:
                        st.header("Screening Information")
                        st.markdown(f"""
                                     <div style='font-size:16px; line-height:1.6'>
                                    {screeningReport}
                                    </div>    
                                    
                                    """,unsafe_allow_html=True)
                    with tab4:
                        st.header("Recommendations")
                        st.markdown(f"""
                                    <div style='font-size:16px; line-height:1.6'>
                                    {recommendations}    
                                    </div>
                                    """,unsafe_allow_html = True)
           

            
   
        
    
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

    
    