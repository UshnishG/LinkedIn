# Resume Generator from LinkedIn PDF

## Overview

This application allows users to upload their LinkedIn PDF resume and convert it into a clean, modern HTML format. Utilizing OpenAI's GPT-4 API, the tool processes the resume text from the PDF and generates an HTML version with semantic HTML5 elements and basic CSS styling.

## Features

- **Upload PDF Resume**: Users can upload a LinkedIn PDF resume.
- **Generate HTML Resume**: Converts the resume text into a structured HTML format.
- **Download HTML File**: Provides an option to download the generated HTML resume.
- **API Integration**: Utilizes OpenAI’s GPT-4 for HTML generation.

## Requirements

- Python 3.7+
- `streamlit` library
- `PyMuPDF` library (`fitz` module)
- `openai` library

## Installation

1. Clone the repository or download the code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python libraries. It’s recommended to use a virtual environment:

   ```bash
   pip install streamlit pymupdf openai
   ```

3. Obtain an OpenAI API key from [OpenAI](https://beta.openai.com/signup/) and set it up for your usage.

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

   Make sure to replace `app.py` with the name of your script if it’s different.

2. Open the application in your web browser. You should see a form to upload your LinkedIn PDF resume and input your OpenAI API key.

3. Upload your PDF resume and enter your API key.

4. Click "Upload" to start the conversion process. The application will extract the text from the PDF, send it to the OpenAI API, and generate the HTML resume.

5. Once the HTML resume is generated, you can view it directly in the application and download it by clicking the "Download HTML Resume" button.

## Code Overview

- **`extract_text_from_pdf(pdf_file)`**: Extracts text from the uploaded PDF file using PyMuPDF (`fitz`).
- **`generate_html_resume(pdf_text, api_key)`**: Sends the extracted text to the OpenAI API to generate HTML content.
- **`main()`**: Manages the Streamlit interface, including file upload, API key input, and displaying the generated HTML resume.

## Troubleshooting

- **Invalid API Key**: Ensure you have entered a valid OpenAI API key. Check if your API key has the correct permissions and is not expired.
- **PDF Parsing Issues**: Ensure that the PDF file is not encrypted and is in a compatible format.

## Contact

For any questions or issues, please reach out to [your-email@example.com](mailto:your-ghosalushnish@gmail.com).