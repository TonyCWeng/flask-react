import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

# initiate extensions
db = SQLAlchemy()
toolbar = DebugToolbarExtension()

def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    
    # attach extensions
    db.init_app(app)
    toolbar.init_app(app)

    # Need to place import statement here to avoid issue of circular imports
    # as users is importing db from project and we require users_blueprint
    # All import statements outside of functions get run first, so we are
    # first instantiating db, which users then import. 
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    
    return app
