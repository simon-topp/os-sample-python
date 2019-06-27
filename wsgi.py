from flask import Flask
application = Flask(__name__)

@application.route("/")
def helloJoe():
    return "Hello Joey!"

@application.route("/bob")
def helloBob():
    return "Hello Bob!!!"

@application.route("/bob2")
def helloBob():
    return "Hello Bob2!!!"

if __name__ == "__main__":
    application.run()
