from flask import Flask

application = Flask(__name__)

@application.route("/")
def helloJoe():
  print("helloJoe()")
  return "Hello Joe !"

@application.route("/bob")
def helloBob():
  print("helloBob()")
  return "Hello Bob !!"

@application.route("/bob1")
def helloBob1():
  print("helloBob1()")
  return "Hello Bob !1!"

@application.route("/bob2")
def helloBob2():
  print("helloBob2()")
  return "Hello Bob !2!"

if __name__ == "__main__":
  application.run()
