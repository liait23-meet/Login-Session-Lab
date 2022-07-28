from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		try:
			message = request.form['message']
			login_session['message'] = message
			name = request.form['name']
			login_session['name'] = name
			age = request.form['age']
			login_session['age'] = age
			return render_template('thanks.html')
		except:
			return render_template('error.html')
	else:
		return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', message = login_session['message'], name  =login_session['name'] , age =  login_session['age']) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)