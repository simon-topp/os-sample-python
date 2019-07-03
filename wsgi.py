import flask, os

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
  print("favicon()")
  return flask.send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def helloJoe():
  print("helloJoe()")
  return "Hello Joe 33!"

@app.route("/bob")
def helloBob():
  print("helloBob()")
  return "Hello Bob 33!!"

@app.route("/bob1")
def helloBob1():
  print("helloBob1()")
  return "Hello Bob 33 !1!"

@app.route("/bob2")
def helloBob2():
  print("helloBob2()")
  return "Hello Bob 33 !2!"

if __name__ == "__main__":
  app.run()
