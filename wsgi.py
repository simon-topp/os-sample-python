from flask import Flask
application = Flask(__name__)

@application.route("/")
def helloJoe():
    return "Hello Joe!"

@application.route("/bob")
def helloBob():
    return "Hello Bob!!!"

if __name__ == "__main__":
    application.run()
