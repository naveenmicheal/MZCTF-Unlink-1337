from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
# app.config['SECRET_KEY'] = '112345678'
TEMPLATES_AUTO_RELOAD = True


@app.route('/')
def flagpage():
	# print(request)
	data = request.cookies.get("Admin")
	if data == 'True':
		return render_template('flag.html',flag = """mzctf{"AcC3p7-CoOK135-whA73v3R"}""")
	else:
		return render_template('flag.html', flag = 'mmmm But Looks Like You are not a Admin!')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333', debug=True)
