from flask import Flask, render_template

# from auth import auth


current_user = {
    'name':'Omer',
    'surname':'deger',
    'mail':'mail@me.com'
}


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @app.route('/hello')
    def hello():
        return render_template('hello.html')

    @app.route('/about')
    def user_name():
        name = current_user['name']
        return f'welcome {name}'

    return app
