from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__)
# app.config['SECRET_KEY'] = '112345678'
app.config['FLASK_DEBUG'] = '111-222-333'
# app.secret_key = '4444444'
os.getenv('FLASK_DEBUG')
@app.route('/')
def hello_world():
	print(dir(app))
	print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
	print(app.env)
	print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
	print(app.debug)
	print('/n')
	# print(app.default_config)
	print('/n')
	print(app.config)
	raise Exception()
    # return render_template('flag.html')

# @app.route('/flagpage')
# def flagpage():
# 	flag = "here"
# 	data = requst.cookies.get("Admin")
# 	if data == 'True':
# 		return render_template('flag.html',flag = """mzctf{"AcC3p7-CoOK135-whA73v3R"}""")
# 	else:
# 		return render_template('flag.html', flag = 'mmmm But Looks Like You are not a Admin!')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333', debug=True)



# https://help.semmle.com/wiki/display/PYTHON/Flask+app+is+run+in+debug+mode