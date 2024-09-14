# resume_generator.py
from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

client = Anthropic(api_key=ANTHROPIC_API_KEY)

def generate_resume_section(job_description, keywords, section, max_words):
    prompt = f"""Given the following job description and keywords, generate a {section} section for a resume:

    Job Description:
    {job_description}

    Keywords to focus on:
    {', '.join(keywords)}

    Please create a concise and relevant {section} section for a resume tailored to this job description.
    The section should be no longer than {max_words} words."""

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=max_words * 2,  # A rough estimate, as tokens != words
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text