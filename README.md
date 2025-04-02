# ATS Resume Analyzer

## Overview

The **ATS Resume Analyzer** is an AI-powered tool designed to help job seekers improve their resumes. It analyzes the resume against a provided job description and gives insights into the alignment between the two. The tool provides a match percentage, identifies missing keywords, and offers recommendations for improvement. The analysis is based on natural language processing and generative AI technology to provide a detailed evaluation.

## Features

- **Resume Upload**: Upload your resume in PDF format.
- **Job Description Input**: Paste the job description to analyze the match.
- **Analysis Options**: 
  - **Detailed Resume Review**: In-depth analysis of the resume against the job description.
  - **Match Percentage Analysis**: Percentage match between the resume and the job description, including missing keywords and skills gap.
- **Export Results**: Export the analysis as a text file for reference.
- **AI-Powered Insights**: Powered by Google Gemini AI, providing professional evaluation and recommendations.

## Technologies Used

- **Streamlit**: For building the web interface and user interaction.
- **Google Gemini AI**: For generating detailed analysis and match percentage based on the job description and resume.
- **PyPDF2**: For extracting text from PDF resumes.
- **dotenv**: For securely managing API keys and configuration.

## Requirements

- Python 3.7 or higher
- Google API Key for Gemini AI
- Required Python libraries:
  - `streamlit`
  - `google-generativeai`
  - `PyPDF2`
  - `python-dotenv`

### Installation

1. Clone or download the repository.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Google API key:

   ```bash
   GOOGLE_API_KEY=your-google-api-key-here
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## How to Use

1. **Upload Your Resume**: Click on the "Upload your resume (PDF format)" section to upload your resume file.
2. **Paste Job Description**: Paste the relevant job description in the "Job Description" text area.
3. **Choose Analysis Type**: Select between "Detailed Resume Review" or "Match Percentage Analysis".
4. **Click Analyze**: Press the "Analyze Resume" button to generate the analysis.
5. **Export Analysis**: After analysis, you can download the results by clicking the "Export Analysis" button.

## Example Analysis

- **Detailed Resume Review**: This will give a comprehensive review of the alignment between your resume and the job description. It includes the strengths, areas for improvement, and a final verdict on your suitability for the role.
  
- **Match Percentage Analysis**: This analysis shows the percentage match, identifies missing keywords, and suggests improvements based on a skill gap analysis.

## Contribution

If you'd like to contribute to this project, feel free to submit pull requests, report issues, or suggest new features.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
