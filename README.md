# AI Test Case Generator

An AI-powered tool that automatically generates structured software test cases from user requirements.

This project helps QA engineers and developers quickly create meaningful test cases by simply providing a feature requirement in plain English.

---

# Overview

AI Test Case Generator analyzes software requirements and produces structured test cases including:

* Test Case Title
* Test Steps
* Expected Results
* Positive and Negative Scenarios

The generated test cases can also be exported into an Excel file, making it easy to share with QA teams or upload into test management systems.

This project demonstrates how AI can assist in **software testing, requirement analysis, and QA automation workflows**.

---

# Features

* Generate test cases from natural language requirements
* AI-powered requirement understanding
* Export test cases to Excel
* Simple command-line interface
* Modular Python architecture
* Easy to extend for automation testing

---

# Example

## Input Requirement

User should be able to login using email and password.

## Generated Output

Test Case 1
Title: Verify login with valid credentials

Steps:

1. Navigate to login page
2. Enter valid email
3. Enter valid password
4. Click login

Expected Result:
User should successfully login and be redirected to the dashboard.

---

Test Case 2
Title: Verify login with invalid password

Steps:

1. Enter valid email
2. Enter incorrect password
3. Click login

Expected Result:
System should display an error message.

---

# Project Architecture

Requirement Input
↓
AI Prompt Builder
↓
AI Model (Gemini/OpenAI)
↓
Response Parser
↓
Structured Test Cases
↓
Excel Export

---

# Project Structure

ai-testcase-generator

main.py
Entry point of the application

ai_client.py
Handles communication with the AI API

parser.py
Parses AI response into structured test cases

export_excel.py
Exports test cases into Excel format

requirements.txt
Python dependencies

README.md
Project documentation

---

# Tech Stack

Python
AI API (Gemini / OpenAI)
Pandas
OpenPyXL
Command Line Interface

---

# Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/ai-testcase-generator.git

Navigate to project folder

cd ai-testcase-generator

Create virtual environment

python -m venv venv

Activate virtual environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

---

# Configuration

Add your AI API key inside the project.

Example:

API_KEY = "your_api_key_here"

You can use:

Gemini API
OpenAI API

---

# Run the Project

python main.py

Enter your requirement when prompted.

Example:

Enter software requirement:
User should be able to login using email and password.

The tool will generate test cases and export them to an Excel file.

---

# Output

The generated test cases will be saved as:

test_cases.xlsx

This Excel file can be used for:

Manual testing documentation
Automation test planning
QA review

---

# Future Improvements

Planned enhancements for this project:

Generate Selenium automation scripts
Generate API test cases automatically
AI-based test data generation
Web UI interface
Integration with test management tools
Support for multiple AI models
Self-healing test automation ideas

---

# Learning Objectives

This project demonstrates:

AI-assisted software testing
Requirement to test-case generation
Python-based automation tooling
AI integration in QA workflows

---

# Author

Amol Shankpal

QA Automation Lead
6+ Years Experience in QA Automation
Manual Testing | Selenium | API Testing | Database Testing | AI in Testing

---

# License

This project is open source and available for educational and learning purposes.
