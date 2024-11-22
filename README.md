# README: Twilio Flask Voice Application

This project is a Flask-based application that integrates Twilio for in-browser calls. It uses the Twilio Voice SDK to handle token generation and call handling. The app is also configured to use Ngrok for exposing a local development server to the internet.

---

## Features

- Generate Twilio Access Tokens for browser-based voice calls.
- Handle incoming and outgoing calls.
- Update Twilio's Voice URL dynamically using Ngrok.
- Simple web interface for initiating calls.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or later**: [Download Python](https://www.python.org/downloads/)
- **Pip (Python package manager)**: Included with Python installation.
- **Ngrok**: [Download Ngrok](https://ngrok.com/download)
- A **Twilio account**: [Sign up for Twilio](https://www.twilio.com/try-twilio)
- **Twilio API Credentials**: Account SID, Auth Token, API Key SID, API Key Secret, TwiML App SID, and a Twilio phone number.
- `.env` file to store environment variables.

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/eersnington/twilio-browser-calls.git
cd twilio-browser-calls
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root with the following variables:
```
TWILIO_ACCOUNT=your_account_sid
TWILIO_API_KEY_SID=your_api_key_sid
TWILIO_API_KEY_SECRET=your_api_key_secret
TWIML_APP_SID=your_twiml_app_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_NUMBER=your_twilio_phone_number
NGROK_AUTH_TOKEN=your_ngrok_auth_token
```

### 5. Run the Application
```bash
python app.py
```

## Deployment Notes
- The application uses ngrok to create a public URL for Twilio webhook
- Ensure your Twilio TwiML Application is configured with the generated ngrok URL

## Requirements
- Flask
- Twilio
- python-dotenv
- pyngrok

## Troubleshooting
- Verify all environment variables are correctly set
- Check Twilio account permissions and credentials
- Ensure ngrok is installed and authenticated
