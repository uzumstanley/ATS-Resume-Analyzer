from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PyPDF2 import PdfReader
import google.generativeai as genai
import time

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class ATSAnalyzer:
    @staticmethod
    def get_gemini_response(input_prompt, pdf_text, job_description):
        try:
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            response = model.generate_content([input_prompt, pdf_text, job_description])
            return response.text
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            return None

    @staticmethod
    def extract_text_from_pdf(uploaded_file):
        try:
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            st.error(f"Error extracting PDF text: {str(e)}")
            return None

def main():
    # Page configuration
    st.set_page_config(
        page_title="ATS Resume Expert",
        page_icon="📄",
        layout="wide"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            background-color: #0066cc;
            color: white;
        }
        .stButton>button:hover {
            background-color: #0052a3;
        }
        .success-message {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #d4edda;
            color: #155724;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header with professional description
    st.title("📄 ATS Resume Analyzer")
    st.markdown("""
        This tool helps you analyze your resume against job descriptions using AI. 
        Upload your resume and paste the job description to:
        - Get a detailed analysis of your resume
        - See the percentage match with job requirements
        - Identify missing keywords and areas for improvement
    """)

    # Create two columns for input
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📝 Job Description")
        job_description = st.text_area(
            "Paste the job description here",
            height=200,
            placeholder="Paste the complete job description here..."
        )

    with col2:
        st.subheader("📎 Resume Upload")
        uploaded_file = st.file_uploader(
            "Upload your resume (PDF format)",
            type=["pdf"],
            help="Please ensure your resume is in PDF format"
        )

        if uploaded_file:
            st.markdown('<p class="success-message">✅ PDF uploaded successfully!</p>', unsafe_allow_html=True)

    # Analysis options
    if uploaded_file and job_description:
        st.subheader("🔍 Analysis Options")
        analysis_type = st.radio(
            "Choose analysis type:",
            ["Detailed Resume Review", "Match Percentage Analysis"]
        )

        if st.button("Analyze Resume"):
            with st.spinner("Analyzing your resume... Please wait"):
                # Extract PDF text
                pdf_text = ATSAnalyzer.extract_text_from_pdf(uploaded_file)
                
                if pdf_text:
                    # Select prompt based on analysis type
                    if analysis_type == "Detailed Resume Review":
                        prompt = """
                        As an experienced Technical Human Resource Manager, provide a detailed professional evaluation 
                        of the candidate's resume against the job description. Please analyze:
                        1. Overall alignment with the role
                        2. Key strengths and qualifications that match
                        3. Notable gaps or areas for improvement
                        4. Specific recommendations for enhancing the resume
                        5. Final verdict on suitability for the role
                        
                        Format the response with clear headings and professional language.
                        """
                    else:
                        prompt = """
                        As an ATS (Applicant Tracking System) expert, provide:
                        1. Overall match percentage (%)
                        2. Key matching keywords found
                        3. Important missing keywords
                        4. Skills gap analysis
                        5. Specific recommendations for improvement
                        
                        Start with the percentage match prominently displayed.
                        """

                    # Get and display response
                    response = ATSAnalyzer.get_gemini_response(prompt, pdf_text, job_description)
                    
                    if response:
                        st.markdown("### Analysis Results")
                        st.markdown(response)
                        
                        # Add export option
                        st.download_button(
                            label="📥 Export Analysis",
                            data=response,
                            file_name="resume_analysis.txt",
                            mime="text/plain"
                        )
    else:
        st.info("👆 Please upload your resume and provide the job description to begin the analysis.")

    # Footer
    st.markdown("---")
    st.markdown(
        "Made with ❤️ by Your Company Name | "
        "This tool uses AI to analyze resumes but should be used as one of many factors in your job application process."
    )

if __name__ == "__main__":
    main()