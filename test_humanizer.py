#!/usr/bin/env python3
"""
Test script for Resume Humanizer
Tests the humanization functionality with sample content
"""

import sys
import os

# Add current directory to path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from resume_humanizer import ResumeHumanizer

def test_humanization():
    """Test the resume humanization functionality."""
    print("🧪 Testing Resume Humanizer")
    print("=" * 40)
    
    # Sample AI-generated text
    sample_text = """
    PROFESSIONAL SUMMARY
    Results-driven software engineer with 5+ years of experience in developing scalable web applications. Leveraged cutting-edge technologies to implement innovative solutions that enhanced user experience and optimized system performance. Orchestrated cross-functional teams to deliver high-quality products within strict deadlines.

    EXPERIENCE
    Senior Software Engineer | TechCorp Inc. | 2021 - Present
    • Utilized React.js and Node.js to develop and maintain web applications
    • Implemented microservices architecture that resulted in 40% improvement in system performance
    • Collaborated with product managers and designers to ensure seamless user experience
    • Spearheaded the development of RESTful APIs that facilitated data integration
    • Orchestrated code reviews and mentored junior developers to enhance team productivity
    • Leveraged AWS cloud services to optimize application deployment and scalability
    """
    
    print("📝 Original AI-generated text:")
    print("-" * 30)
    print(sample_text)
    print("\n" + "="*50 + "\n")
    
    # Initialize humanizer
    humanizer = ResumeHumanizer()
    
    # Humanize the text
    print("🔄 Humanizing text...")
    humanized_text = humanizer.humanize_resume(sample_text)
    
    print("✅ Humanized text:")
    print("-" * 30)
    print(humanized_text)
    print("\n" + "="*50 + "\n")
    
    # Get readability scores
    print("📊 Readability Analysis:")
    print("-" * 30)
    scores = humanizer.get_readability_score(humanized_text)
    
    for metric, value in scores.items():
        if isinstance(value, float):
            print(f"{metric}: {value:.2f}")
        else:
            print(f"{metric}: {value}")
    
    print("\n" + "="*50 + "\n")
    
    # Test specific AI patterns
    print("🔍 Testing AI Pattern Detection:")
    print("-" * 30)
    
    ai_patterns = [
        "utilized", "leveraged", "implemented", "orchestrated",
        "spearheaded", "collaborated", "coordinated", "facilitated"
    ]
    
    for pattern in ai_patterns:
        if pattern in sample_text.lower():
            print(f"❌ Found AI pattern: '{pattern}'")
        else:
            print(f"✅ No AI pattern: '{pattern}'")
    
    print("\n" + "="*50 + "\n")
    
    # Check if humanized text has fewer AI patterns
    print("✅ Humanization Results:")
    print("-" * 30)
    
    original_ai_count = sum(1 for pattern in ai_patterns if pattern in sample_text.lower())
    humanized_ai_count = sum(1 for pattern in ai_patterns if pattern in humanized_text.lower())
    
    print(f"AI patterns in original: {original_ai_count}")
    print(f"AI patterns in humanized: {humanized_ai_count}")
    print(f"Reduction: {original_ai_count - humanized_ai_count} patterns")
    
    if humanized_ai_count < original_ai_count:
        print("🎉 Success: AI patterns reduced!")
    else:
        print("⚠️  Warning: AI patterns not significantly reduced")
    
    print("\n" + "="*50)
    print("✅ Test completed successfully!")

if __name__ == "__main__":
    test_humanization()