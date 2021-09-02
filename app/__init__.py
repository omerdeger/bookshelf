from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    @app.route('/')
    def index():
        return '''
        <a href="/auth">Auth</a>
        <a href="/bookshelf">Bookshelf</a>
        '''
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    from .bookshelf import bookshelf as bookshelf_blueprint
    app.register_blueprint(bookshelf_blueprint, url_prefix='/bookshelf')

    return app
