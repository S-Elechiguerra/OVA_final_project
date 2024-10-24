from flask import Flask

# Initialize Flask app
def create_app():
    app = Flask(__name__)

    # Register routes
    from .routes import predict_bp
    app.register_blueprint(predict_bp)

    return app