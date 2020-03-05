from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/flag', methods = ['POST','GET'])
def flag():
	if request.method =='POST':
		name = request.form['username']
		passw = request.form['password']
		print('{} {}'.format(name, passw))
		if name == 'root' and passw == 'iamroot':
				return render_template('flag.html')
		else:
			return '<center><h1>Wrong Password</h1></center>'		
	else:
		return 'METHOD NOT ALLOWED'	
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333', debug=True)
