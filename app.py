import os

# Ensure Streamlit doesn't try to write to root dir
os.environ["HOME"] = "/app"
os.environ["HF_HOME"] = "/app/huggingface"

import streamlit as st
from main import ResumeOptimiser, extract_text_from_pdf

st.title("Resume Optimiser")

resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the job description here")

if st.button("Generate Optimised Resume"):
  if resume_file and job_description:
    with st.spinner("Analysing and optimising your resume..."):
      resume_text = extract_text_from_pdf(resume_file)
      optimiser = ResumeOptimiser()
      optimised_resume = optimiser.generate_updated_resume(resume_text, job_description)
      st.success("Optimised Resume Generated")
      st.text_area("Updated Resume", optimised_resume, height=400)
  else:
    st.error("Please upload a resume and paste a job description")
