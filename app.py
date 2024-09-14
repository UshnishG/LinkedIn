import streamlit as st
import fitz  
import openai
import os

def extract_text_from_pdf(pdf_file):
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def generate_html_resume(pdf_text, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=f"""You are an expert at generating HTML. Convert the following resume text into a clean, modern HTML format using best practices:
        
        1. Use semantic HTML5 elements like <header>, <main>, <section>, and <footer>.
        2. Add CSS properly please
        3. Include sections for Contact Information, Summary, Experience, Education, Skills, and Projects.
        4. Ensure proper headings for sections (e.g., <h1> for the name, <h2> for each section title).
        5. Format the content using basic CSS styles. Use a modern font (e.g., Arial or Roboto), and ensure the layout is responsive.
        6. For the CSS, include styling for margins, padding, fonts, and alignment to create a visually appealing resume.
        7. Ensure the contact information is at the top, and each section is clearly separated.
        8. Format dates, job titles, and company names clearly.
        9. For links (e.g., LinkedIn or GitHub), make them clickable.
        
        Here's the resume text:
        {pdf_text}
        """,
        max_tokens=3000
    )
    return response['choices'][0]['text']

def main():
    st.title("Resume Generator from LinkedIn PDF")
    st.write("Upload your LinkedIn PDF resume and generate an HTML resume.")

    # Input field to enter OpenAI API key
    api_key = st.text_input("Enter your OpenAI API Key", type="password")

    # File uploader for PDF file
    uploaded_pdf = st.file_uploader("Upload your LinkedIn PDF", type=["pdf"])

    if uploaded_pdf and api_key:

        pdf_text = extract_text_from_pdf(uploaded_pdf)

        with st.spinner('Generating your HTML resume...'):
            html_resume = generate_html_resume(pdf_text, api_key)

        st.subheader("Generated HTML Resume:")
        st.code(html_resume, language='html')
        st.download_button("Download HTML Resume", data=html_resume, file_name="resume.html", mime="text/html")

if __name__ == "__main__":
    main()
