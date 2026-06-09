from flask import Flask
from app.manager import wpp_bp

app = Flask(__name__)
app.register_blueprint(wpp_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)