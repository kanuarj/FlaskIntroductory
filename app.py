from flask import * 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		name = request.form['names']
		return render_template('names.html', n=name)
	return render_template('index.html')

@app.route('/names', methods=['GET', 'POST'])
def names():
	if request.method == 'POST':
		return redirect(url_for('basic'))
	return render_template('names.html')

if __name__ == '__main__':
	app.run()