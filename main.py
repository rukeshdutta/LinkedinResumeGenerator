import streamlit as st
from ui import render_ui
from resume_generator import generate_resume_section

def main():
    st.set_page_config(page_title="Job Description to Resume Section Generator", layout="wide")
    
    job_description, keywords, selected_section, max_words = render_ui()
    
    if st.button("Generate Section"):
        if job_description and keywords and selected_section:
            keyword_list = [k.strip() for k in keywords.split(',')]
            
            generated_section = generate_resume_section(job_description, keyword_list, selected_section, max_words)
            
            st.subheader(f"Generated {selected_section} Section")
            st.write(generated_section)
        else:
            st.warning("Please enter the job description, keywords, and select a section.")

if __name__ == "__main__":
    main()