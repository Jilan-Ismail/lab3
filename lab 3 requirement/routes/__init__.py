from .tasks import tasks_bp

def register_routes(app):
    app.register_blueprint(tasks_bp, url_prefix='/tasks')
