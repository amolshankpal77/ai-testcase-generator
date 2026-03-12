# AI Test Case Generator

An AI-powered tool that automatically generates software test cases from user requirements.

## Overview

This project uses AI to analyze a software requirement and generate structured test cases that QA engineers can use for manual or automation testing.

The generated test cases can also be exported to Excel for easy sharing and documentation.

## Features

- Generate test cases from plain English requirements
- AI-powered requirement analysis
- Export test cases to Excel
- Simple CLI-based interface
- Lightweight and easy to extend

## Example

Input Requirement:

User should be able to login using email and password.

Generated Output:

Test Case 1  
Title: Verify login with valid credentials  
Steps:
1. Enter valid email
2. Enter valid password
3. Click login  
Expected Result: User should login successfully.

Test Case 2  
Title: Verify login with invalid password  
Expected Result: Error message should be displayed.

## Project Structure
