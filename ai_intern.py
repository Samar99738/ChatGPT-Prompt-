# -*- coding: utf-8 -*-
"""AI Intern


Prompt (Instruct ChatGPT to parse resume)

You are to act as a resume parser. I will provide you with a text resume, and your task is to parse it and output the content in JSON format. The JSON should include the following fields:

- Name
- Contact Information
  - Email
  - Phone
  - Address
- Summary / Objective
- Work Experience
  - Job Title
  - Company
  - Start Date
  - End Date
  - Location
  - Description
- Education
  - Degree
  - Institution
  - Start Date
  - End Date
  - Location
- Skills
- Certifications
- Projects
- Languages
- Other Information

Here's the text resume:

<table>
<!-- Include your resume details here -->
</table>
"""

config.yaml

openai_api_key: "YOUR_OPENAI_API_KEY"

# resume_parser.py
import openai
import yaml

# Load the config file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Define OpenAI API key
openai.api_key = config["openai_api_key"]

def format_resume_to_json(resume_text):
    prompt = f"""
You are to act as a resume parser. I will provide you with a text resume, and your task is to parse it and output the content in JSON format. 

- Name
- Contact Information
  - Email
  - Phone
  - Address
- Summary / Objective
- Work Experience
  - Job Title
  - Company
  - Start Date
  - End Date
  - Location
  - Description
- Education
  - Degree
  - Institution
  - Start Date
  - End Date
  - Location
- Skills
- Certifications
- Projects
- Languages
- Other Information

Here's the text resume:

{resume_text}
"""

    response = openai.Completion.create(
        engine="davinci",  # Use an NLU-focused engine
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Parse the response into a JSON-like structure (you'll need to customize this part)
    parsed_resume = {
        "name": "John Doe",
        "email": "john.doe@email.com",
        # Add other fields here...
    }

    return parsed_resume

if __name__ == "__main__":
    # Load Resume Text
    with open("resume.txt", "r") as resume_file:
        resume_content = resume_file.read()

    result_json = format_resume_to_json(resume_content)

    # Print or save the result
    print(result_json)
    with open("parsed_resume.json", "w") as json_file:
        yaml.dump(result_json, json_file)  


