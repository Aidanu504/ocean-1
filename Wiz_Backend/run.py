from app import create_app
from flask_cors import CORS
import os

# create app

app = create_app()

CORS(app, supports_credentials=True, origins="https://ocean-1-1.onrender.com")

# run app with debug
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
