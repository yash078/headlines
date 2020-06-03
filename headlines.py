from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_news():
    return 'Non news is good news!'


if __name__ == '__main':
    app.run(port=5000, debug=True)