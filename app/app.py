from app import create_app

# Create and run the Flask app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)