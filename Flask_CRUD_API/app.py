from flask import Flask
from laptops_blueprint import laptops_blueprint

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(laptops_blueprint)

if __name__ == '_main_':
    app.run(debug=True)