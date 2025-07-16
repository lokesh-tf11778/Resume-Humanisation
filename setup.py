#!/usr/bin/env python3
"""
Setup script for Resume Humanizer
Automates the installation and setup process
"""

import os
import sys
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def install_requirements():
    """Install required packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        sys.exit(1)

def download_nltk_data():
    """Download required NLTK data."""
    print("📚 Downloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        print("✅ NLTK data downloaded successfully")
    except Exception as e:
        print(f"❌ Error downloading NLTK data: {e}")
        print("You can manually download it later with: python -c \"import nltk; nltk.download('punkt')\"")

def create_directories():
    """Create necessary directories."""
    directories = ['uploads', 'templates', 'static/css', 'static/js']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("✅ Directories created successfully")

def check_dependencies():
    """Check if all dependencies are properly installed."""
    print("🔍 Checking dependencies...")
    required_packages = [
        'flask', 'PyPDF2', 'docx', 'nltk', 'textstat'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed")
    return True

def main():
    """Main setup function."""
    print("🚀 Resume Humanizer Setup")
    print("=" * 40)
    
    # Check Python version
    check_python_version()
    
    # Create directories
    create_directories()
    
    # Install requirements
    install_requirements()
    
    # Download NLTK data
    download_nltk_data()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nTo run the application:")
    print("  python app.py")
    print("\nThen open your browser to: http://localhost:5000")
    print("\nFor more information, see README.md")

if __name__ == "__main__":
    main()