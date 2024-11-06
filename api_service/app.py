import logging
from flask import Flask, jsonify, request 

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        # Uncomment the next line to log to a file as well
        # logging.FileHandler("app.log")
    ]
)

app = Flask(__name__)

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return "Welcome to the Flask API!"

@app.route('/api/data', methods=['GET'])
def get_data():
    app.logger.info("GET request received at /api/data")
    data = {"message": "This is a GET request response"}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    content = request.json
    app.logger.info(f"POST request received at /api/data with data: {content}")
    response = {"received": content}
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)