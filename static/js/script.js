// Global variables
let currentHumanizedText = '';

// DOM elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const processingSection = document.getElementById('processingSection');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');
const originalText = document.getElementById('originalText');
const humanizedText = document.getElementById('humanizedText');
const errorMessage = document.getElementById('errorMessage');

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    setupDragAndDrop();
    setupFileInput();
});

function setupDragAndDrop() {
    uploadArea.addEventListener('dragover', function(e) {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', function(e) {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', function(e) {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });

    uploadArea.addEventListener('click', function() {
        fileInput.click();
    });
}

function setupFileInput() {
    fileInput.addEventListener('change', function(e) {
        if (e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });
}

function handleFile(file) {
    // Validate file type
    const allowedTypes = ['.pdf', '.doc', '.docx', '.txt'];
    const fileExtension = '.' + file.name.split('.').pop().toLowerCase();
    
    if (!allowedTypes.includes(fileExtension)) {
        showError('Please select a valid file type (PDF, DOC, DOCX, or TXT)');
        return;
    }

    // Validate file size (16MB max)
    if (file.size > 16 * 1024 * 1024) {
        showError('File size must be less than 16MB');
        return;
    }

    uploadFile(file);
}

function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    // Show processing section
    showProcessing();

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showResults(data.original, data.humanized);
            currentHumanizedText = data.humanized;
        } else {
            showError(data.error || 'An error occurred while processing your resume');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showError('An error occurred while uploading your file. Please try again.');
    });
}

function showProcessing() {
    uploadArea.style.display = 'none';
    processingSection.style.display = 'block';
    resultsSection.style.display = 'none';
    errorSection.style.display = 'none';
}

function showResults(original, humanized) {
    uploadArea.style.display = 'none';
    processingSection.style.display = 'none';
    resultsSection.style.display = 'block';
    errorSection.style.display = 'none';

    originalText.textContent = original;
    humanizedText.textContent = humanized;
}

function showError(message) {
    uploadArea.style.display = 'none';
    processingSection.style.display = 'none';
    resultsSection.style.display = 'none';
    errorSection.style.display = 'block';

    errorMessage.textContent = message;
}

function resetApp() {
    uploadArea.style.display = 'block';
    processingSection.style.display = 'none';
    resultsSection.style.display = 'none';
    errorSection.style.display = 'none';

    // Reset file input
    fileInput.value = '';
    
    // Reset text content
    originalText.textContent = '';
    humanizedText.textContent = '';
    currentHumanizedText = '';
}

function downloadText() {
    if (!currentHumanizedText) {
        showError('No humanized text available for download');
        return;
    }

    // Create blob and download
    const blob = new Blob([currentHumanizedText], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'humanized_resume.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

// Alternative download method using server endpoint
function downloadTextServer() {
    if (!currentHumanizedText) {
        showError('No humanized text available for download');
        return;
    }

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            humanized_text: currentHumanizedText
        })
    })
    .then(response => {
        if (response.ok) {
            return response.blob();
        }
        throw new Error('Download failed');
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'humanized_resume.txt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    })
    .catch(error => {
        console.error('Download error:', error);
        showError('Failed to download file. Please try again.');
    });
}

// Utility functions
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function validateFile(file) {
    const allowedTypes = ['.pdf', '.doc', '.docx', '.txt'];
    const fileExtension = '.' + file.name.split('.').pop().toLowerCase();
    
    if (!allowedTypes.includes(fileExtension)) {
        return { valid: false, error: 'Please select a valid file type (PDF, DOC, DOCX, or TXT)' };
    }
    
    if (file.size > 16 * 1024 * 1024) {
        return { valid: false, error: 'File size must be less than 16MB' };
    }
    
    return { valid: true };
}