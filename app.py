from application import create_app
from gevent.pywsgi import WSGIServer


app = create_app()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
