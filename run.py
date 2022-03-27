from api.main import app
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    # コンソールで [$ uvicorn run:app --reload]でも可
    uvicorn.run(app=app, host="0.0.0.0", port=os.environ['PORT'])