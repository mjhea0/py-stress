import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return loop(100)

def loop(num):
	x = 1
	array = []
	for x in range(0,n):
	    array.append(x)
	    x +=1
	return array


if __name__ == '__main__':
  port = int(os.environ.get('PORT',5001))
  app.run(host='0.0.0.0', port=port)