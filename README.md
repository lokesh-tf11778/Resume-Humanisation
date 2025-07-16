# Resume Humanizer

Transform AI-generated resumes into 100% human-written content that passes AI detection tools.

## 🚀 Features

- **Multi-format Support**: Process PDF, DOC, DOCX, and TXT files
- **AI Pattern Detection**: Identifies and replaces AI-generated language patterns
- **Human Language Conversion**: Converts to natural, human-like vocabulary
- **Personal Touch**: Adds authentic personal elements and variations
- **Modern UI**: Beautiful, responsive web interface
- **Real-time Processing**: Instant feedback and results
- **Download Support**: Export humanized resumes as text files

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Resume-Humanisation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data** (required for text processing)
   ```bash
   python -c "import nltk; nltk.download('punkt')"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and go to `http://localhost:5000`

## 📁 Project Structure

```
Resume-Humanisation/
├── app.py                 # Main Flask application
├── resume_processor.py    # File processing and text extraction
├── resume_humanizer.py    # AI to human text conversion
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── css/
│   │   └── style.css     # Styling and responsive design
│   └── js/
│       └── script.js     # Frontend functionality
└── uploads/              # Temporary file storage (auto-created)
```

## 🔧 How It Works

### 1. File Processing
- Extracts text from PDF, Word documents, and text files
- Handles various document formats and structures
- Cleans and normalizes extracted text

### 2. AI Pattern Detection
The application identifies common AI-generated patterns:
- **Corporate Buzzwords**: "utilized", "leveraged", "implemented"
- **Action Verbs**: "orchestrated", "spearheaded", "pioneered"
- **Result Phrases**: "resulted in", "led to", "achieved"
- **Collaboration Terms**: "collaborated with", "partnered with"

### 3. Human Language Conversion
Replaces AI patterns with natural alternatives:
- "utilized" → "used", "employed", "applied"
- "leveraged" → "used", "took advantage of"
- "implemented" → "put in place", "set up", "started"
- "orchestrated" → "organized", "arranged", "planned"

### 4. Natural Variations
- Adds personal pronouns occasionally
- Uses contractions naturally
- Includes sentence connectors
- Varies sentence structure
- Adds human qualifiers

## 🎯 Usage

1. **Upload Resume**: Drag and drop or click to upload your resume
2. **Processing**: The system extracts text and humanizes it
3. **Review**: Compare original vs humanized versions side-by-side
4. **Download**: Save the humanized resume as a text file

## 🔍 AI Detection Features

The application specifically targets:

### Vocabulary Patterns
- Replaces formal, AI-typical words with natural alternatives
- Uses varied, human-like vocabulary
- Avoids repetitive corporate language

### Sentence Structure
- Breaks up overly long sentences
- Adds natural connectors and transitions
- Varies sentence complexity

### Personal Elements
- Adds occasional personal pronouns
- Uses contractions naturally
- Includes human-like qualifiers

## 📊 Technical Details

### Dependencies
- **Flask**: Web framework
- **PyPDF2**: PDF text extraction
- **python-docx**: Word document processing
- **NLTK**: Natural language processing
- **textstat**: Readability analysis
- **spacy**: Advanced text processing

### API Endpoints
- `GET /`: Main application interface
- `POST /upload`: File upload and processing
- `POST /download`: Download humanized text

### File Size Limits
- Maximum file size: 16MB
- Supported formats: PDF, DOC, DOCX, TXT

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set up a production WSGI server (Gunicorn, uWSGI)
2. Configure environment variables
3. Set up reverse proxy (Nginx, Apache)
4. Enable HTTPS

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🔒 Security Features

- File type validation
- File size limits
- Secure file handling
- Temporary file cleanup
- Input sanitization

## 🧪 Testing

### Manual Testing
1. Upload various file formats
2. Test with different AI-generated content
3. Verify humanization quality
4. Check download functionality

### Sample Test Cases
- PDF with AI-generated content
- Word document with corporate language
- Text file with formal vocabulary
- Mixed content types

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:
1. Check the console for error messages
2. Verify file format and size
3. Ensure all dependencies are installed
4. Check NLTK data is downloaded

## 🔄 Updates

The application is regularly updated to:
- Improve AI pattern detection
- Add new human language alternatives
- Enhance processing algorithms
- Update security measures

---

**Note**: This tool is designed to help make resumes appear more human-written. Always review and customize the output to ensure it accurately represents your experience and skills.