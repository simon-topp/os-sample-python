from flask import Flask
from pprint import pprint

application = Flask(__name__)

@application.route("/")
def helloJoe():
    pprint.pprint("helloJoe()")
    pprint.pprint(application)
    return "Hello Joe!"

@application.route("/bob")
def helloBob():
    return "Hello Bob!!!"

@application.route("/bob2")
def helloBob2():
    return "Hello Bob2!!!"

if __name__ == "__main__":
    application.run()
