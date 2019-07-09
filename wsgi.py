import flask, os, pprint

application = flask.Flask(__name__)

@application.route('/favicon.ico')
def favicon():
  print("favicon()")
  return flask.send_from_directory(os.path.join(application.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@application.route("/")
def root():
  print("root()")
  print("request:")
  pprint.pprint(request)
  print("request.args:")
  pprint.pprint(request.args)
  return "<Response></Response>"

if __name__ == "__main__":
  application.run()
