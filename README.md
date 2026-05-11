# Community Learning
Website allowing for easier access to learning new topic, hobbies, etc. 

## Gemini Track:
Using Gemini to learn something new is sometimes hard to navigate as it is only able to answer your questions with any helpful additional information. Our website utilized the Gemini 2.5 Flash API to generate information regarding any topic that the user inputs and organizes that information into an educational layout similar to that of the modules on Canvas that organizes the topic along with providing additional youtube links for more information.


### Frontend

<ul>Technologies: HTML, CSS </ul>  
<ul>Logic: JavaScript (Fetch API)</ul>

### Backend

<ul>Framework: Python / Flask</ul>
<ul>Middleware: Flask-CORS (Cross Origin Resource Sharing)</ul>
<ul>Security: Python Dotenv</ul>

### Integration 
<ul>Brain: Gemini 2.5 Flash</ul>
<ul>YouTube Data API v3</ul>

### Media Integration: 
```
YouTube Data API v3
```
### Environment: 
```
Python Dotenv for secure credential management
```

## Getting started

### Installation
```
# Clone the repository
git clone https://github.com/communitylearning/communitylearning.github.io.git
cd communitylearning.github.io/backend

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.\.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

## Dependencies
```
pip install flask flask-cors python-dotenv google-genai google-api-python-client svglib
```

## Environment configuration
Create .env in /backend
```
GEMINI_API_KEY=your_gemini_api_key_here
YOUTUBE_API_KEY=your_youtube_api_key_here
```

## Running application
```
python app.py
```
Runs on port
```
http://127.0.0.1:5000
```
