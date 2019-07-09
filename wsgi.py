import flask, os, pprint

application = flask.Flask(__name__)

@application.route('/favicon.ico')
def favicon():
  print("favicon()")
  return flask.send_from_directory(os.path.join(application.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@application.route("/", methods = ['POST'])
def root():
  print("root()")
  print("request:")
  pprint.pprint(flask.request)
  print("request.args:")
  pprint.pprint(flask.request.args)
  print("request.values:")
  pprint.pprint(flask.request.values)
  print("request.headers:")
  pprint.pprint(flask.request.headers)
  return "<Response></Response>"



if __name__ == "__main__":
  application.run()
