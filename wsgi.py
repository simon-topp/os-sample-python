import flask, os, pprint, requests, jwt, json, base64

application = flask.Flask(__name__)

endpoint = 'https://extapigwservice-demo.cidemo.sas.com/marketingGateway/events'
secret = 'MTA2NDEwYTg4bTBjODJoZmRoOG5jZjZpazhnZ2g0Mmpt'
tenantId='af5af6b8f500013eb0c9ec44'

#Generate JWT
encodedSecret = base64.b64encode(bytes(secret, encoding='utf8'))
token = jwt.encode({'clientID': tenantId}, encodedSecret, algorithm='HS256')
headers = { 
  'Content-Type': 'application/json', 
  'Authorization': 'Bearer '+ bytes.decode(token) 
}

@application.route('/favicon.ico')
def favicon():
  print('favicon()')
  return flask.send_from_directory(os.path.join(application.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@application.route('/', methods = ['POST'])
def root():
  print('root()')
  print('request:')
  pprint.pprint(flask.request)
  print('request.args:')
  pprint.pprint(flask.request.args)
  print('request.values:')
  pprint.pprint(flask.request.values)
  print('request.headers:')
  pprint.pprint(flask.request.headers)
  sender = flask.request.values.get('From')
  # remove training "+" from sender address
  customer_id = sender[1:] if sender.startswith("+") else sender
  data = {
    'eventName': 'twilio_event',
    'customer_id': customer_id,
    'SmsSid':  flask.request.values.get('SmsSid'),
    'Body': flask.request.values.get('Body').strip().lower(),
    'From': sender,
    'FromCountry': flask.request.values.get('FromCountry'),
    'SmsStatus': flask.request.values.get('SmsStatus'),
    'AccountSid': flask.request.values.get('AccountSid')
  }
  response = requests.request('POST', endpoint, data=json.dumps(data), headers=headers)
  print('response:')
  pprint.pprint(response.headers)
  print(response.text)
  return '<Response></Response>'



if __name__ == '__main__':
  application.run()

