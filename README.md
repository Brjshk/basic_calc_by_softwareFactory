# Calculator Application

## Overview
The Calculator Application is a web-based tool for performing basic arithmetic operations.

## Features
- Addition, subtraction, multiplication, and division
- Numeric keypad for input
- Immediate result display
- Clear button to reset input

## Technology Stack
- **Backend**: Python, FastAPI
- **Frontend**: HTML, JavaScript

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   uvicorn backend.main:app --reload
   ```

## API Endpoints
- **POST /calculate**: Perform a calculation
- **GET /health**: Check if the service is running
