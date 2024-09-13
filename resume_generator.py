from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

client = Anthropic(api_key=ANTHROPIC_API_KEY)

def generate_resume_section(job_description, keywords, section):
    prompt = f"""
    Given the following job description and keywords, generate a {section} section for a resume:

    Job Description:
    {job_description}

    Keywords to focus on:
    {', '.join(keywords)}

    Please create a concise and relevant {section} section for a resume tailored to this job description.
    """
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=500,
    )
    
    return response.completion

def generate_resume_sections(job_description, keywords, sections):
    resume = {}
    for section in sections:
        resume[section] = generate_resume_section(job_description, keywords, section)
    return resume