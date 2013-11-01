import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi World!'

@app.route('/loop', defaults={"a":0, "b":100})

def endless_loop(a, b):
    count = a
    array = []
    while (count < b):
       print 'The count is:', count
       array.append(count)
       count += 1
    print "Good bye!"



if __name__ == '__main__':
  port = int(os.environ.get('PORT',5001))
  app.run(host='0.0.0.0', port=port)



