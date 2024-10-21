from app import app  # Import the Flask app from your main app file

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)
