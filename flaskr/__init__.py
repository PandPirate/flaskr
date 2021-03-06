import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flasker.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    # 注册auth蓝图
    from . import auth, filemanager, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(filemanager.bp)
    app.register_blueprint(blog.bp)


    # 主页
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')
    return app





