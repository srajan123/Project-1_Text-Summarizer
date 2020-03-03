from flask import Flask,render_template,request
from temp_nltk import url_rize

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def index():
	mess = 'I LOVE PYTHON!'
	return render_template('index1.html',msg=mess)

@app.route('/success',methods=['GET','POST'])
def analyze():
	if request.method == 'POST':
		dec = ' (Summarized Form)'
		key = 'Key Points'
		rawtext = request.form['raw']
		typesum = request.form['typesum']
		
	return render_template('index2.html')

if __name__ == '__main__':
	app.run(debug=True)
