from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import os

# load_dotenv(override=True)
# client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
class ResumeOptimiser:
  def __init__(self):
    self.openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

  def system_prompt(self):
    return """
      You are a professional resume optimization assistant. Your task is to analyze a user's resume and a target job description, then generate a fully optimized and tailored resume that will pass Applicant Tracking Systems (ATS) and impress human recruiters. Follow these instructions strictly:
      1. Analyze the user's resume and extract all usable skills, tools, technologies, achievements, and responsibilities—even from unrelated job roles.
      2. Carefully review the job description and extract key responsibilities, qualifications, tools, and language used by the employer.
      3. Completely revamp the resume if needed to better align with the job description. Reorganize, rephrase, or rewrite every section to highlight relevant experience, transferable skills, and job-specific accomplishments.
      4. Update past responsibilities to emphasize transferable skills and relevant achievements that match the job requirements—without fabricating experience.
      5. Integrate exact phrases and keywords from the job description to ensure the resume is highly optimized for ATS parsing.
      6. Use professional, concise, and achievement-oriented bullet points under each role, showing measurable impact where possible.
      7. Structure the resume with the following clear, ATS-friendly sections (where applicable): 
        - Professional Summary
        - Core Skills & Tools
        - Relevant Experience
        - Projects (if needed)
        - Education
        - Certifications
      8. Format the resume with clean, modern styling—no tables, images, graphics, or multiple columns. Keep it in plain text, ready for PDF export.
      9. Maintain a consistent voice, grammar, verb tense (past for previous roles, present for current), and formatting throughout.
      10. The resume should be no longer than 2 pages unless explicitly instructed otherwise.
      11. If any important information (e.g. dates, portfolio link, location) is missing, insert a clear placeholder like [Insert Date] or [Insert URL].
      12. Output only the final optimized resume in plain text—no extra commentary, analysis, or headings outside of the resume.

      Your goal is to maximize the user’s chances of being shortlisted for an interview by both ATS filters and human recruiters—even if this requires completely transforming the original resume.

    """
  
  def generate_updated_resume(self, resume_text, job_description):
    messages = [
      {"role": "assistant", "content": self.system_prompt()},
      {"role": "user", "content": f"Resume:\n{resume_text}\n\nJob Description:\n{job_description}"}
    ]

    response = self.openai.chat.completions.create(
      model="gpt-4.1",
      messages=messages
    )
    return response.choices[0].message.content

def extract_text_from_pdf(uploaded_file):
  reader = PdfReader(uploaded_file)
  text = ""
  for page in reader.pages:
    text += page.extract_text() or ""
  return text

