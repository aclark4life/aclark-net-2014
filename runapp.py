from paste.deploy import loadapp
from waitress import serve
import os


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6543))
    app = loadapp('config:production.ini', relative_to='.')
    serve(app, host='0.0.0.0', port=port, expose_tracebacks=True)
