from db_connection import db

jobs_collection = db['Jobs']

# fake job data 
fake_jobs = [
    {
        "experience": 2,
        "expected_technical_skills": ["JavaScript", "React", "HTML", "CSS"],
        "experience_level": "Junior",
        "salary_expectations": "4-6 LPA",
        "job_role": "Frontend Developer",
        "location": "Delhi",
        "company": "TechNova",
        "key_responsibilities": [
            "Develop user-facing features",
            "Ensure technical feasibility of UI/UX designs",
            "Collaborate with backend developers and designers"
        ]
    },
    {
        "experience": 5,
        "expected_technical_skills": ["Python", "Django", "REST APIs"],
        "experience_level": "Mid",
        "salary_expectations": "7-10 LPA",
        "job_role": "Backend Developer",
        "location": "Bangalore",
        "company": "CodeWave",
        "key_responsibilities": [
            "Build and maintain backend logic using Django",
            "Integrate third-party APIs",
            "Ensure data security and protection"
        ]
    },
    {
        "experience": 1,
        "expected_technical_skills": ["HTML", "CSS", "Bootstrap"],
        "experience_level": "Intern",
        "salary_expectations": "10-15K/month",
        "job_role": "Web Design Intern",
        "location": "Remote",
        "company": "DesignHive",
        "key_responsibilities": [
            "Assist in designing responsive web pages",
            "Convert Figma designs to HTML/CSS",
            "Support the frontend team with routine tasks"
        ]
    },
    {
        "experience": 7,
        "expected_technical_skills": ["Node.js", "MongoDB", "AWS", "Docker"],
        "experience_level": "Senior",
        "salary_expectations": "15-20 LPA",
        "job_role": "Full Stack Developer",
        "location": "Mumbai",
        "company": "CloudStack Solutions",
        "key_responsibilities": [
            "Lead full-stack development projects",
            "Deploy applications on AWS using Docker",
            "Mentor junior developers and conduct code reviews"
        ]
    },
    {
        "experience": 4,
        "expected_technical_skills": ["Java", "Spring Boot", "Microservices"],
        "experience_level": "Mid",
        "salary_expectations": "9-12 LPA",
        "job_role": "Software Engineer",
        "location": "Hyderabad",
        "company": "NextGenTech",
        "key_responsibilities": [
            "Develop scalable microservices using Spring Boot",
            "Collaborate in Agile development cycles",
            "Write unit and integration tests"
        ]
    }
]

result = jobs_collection.insert_many(fake_jobs)
