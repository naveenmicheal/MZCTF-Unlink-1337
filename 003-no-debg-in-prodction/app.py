from flask import Flask, render_template, Response, request,make_response, redirect, url_for
import os


app = Flask(__name__)
os.environ['WERKZEUG_DEBUG_PIN'] = '1337-7331'
@app.route('/')
def hello_world():
	resp = make_response(render_template('flag.html'), 200)
	# resp.headers.extend({'X-Powered-By': 'AT-5000'})

	resp.headers.add_header("Debug-Pin","1337-7331")
	resp.headers.add_header("Shell-Page-Location","/shell")
	# raise Exception()
	return resp

@app.route('/shell')
def do():
	raise Exception()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333', debug=True)


# 
# https://help.semmle.com/wiki/display/PYTHON/Flask+app+is+run+in+debug+mode