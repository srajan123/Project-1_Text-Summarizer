from flask import Flask,render_template,request,make_response
from temp_nltk import url_rize
import pdfkit
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def index():
	mess = 'I LOVE PYTHON!'
	return render_template('index1.html',msg=mess)

@app.route('/success',methods=['GET','POST'])
def analyze():
	if request.method == 'POST':
		render = render_template('index1.html')
		config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf')
		pdf = pdfkit.from_string(render, False, configuration=config)

		response = make_response(pdf)
		response.headers['Content-Type'] = 'application/pdf'
		response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

		return response

if __name__ == '__main__':
	app.run(debug=True)
