from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from routes import register_routes

app = Flask(__name__)

# Register your routes
register_routes(app)

# Swagger setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'  # Path to the Swagger YAML file

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Task API"}  # Optional config
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
