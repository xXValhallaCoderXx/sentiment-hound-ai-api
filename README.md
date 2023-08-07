## Local Virtual Env
- Create VENV: python3 -m venv venv/
- Start VENV: source venv/bin/activate
- Start App: uvicorn main:app --reload
- pip3 install -r requirements.txt 

## Development 

Start Development Server
- docker-compose -f docker-compose.dev.yml up