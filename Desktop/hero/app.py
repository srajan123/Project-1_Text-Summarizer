from flask import Flask,render_template,request,make_response
from temp_nltk import url_rize
import pdfkit

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
	return render_template('index1.html')

dic={}
@app.route('/success',methods=['GET','POST'])
def analyze():
	if request.method == 'POST':
		key = 'Key Points'
		rawtext = request.form['raw']
		typesum = request.form['typesum']
		protext = url_rize(rawtext,typesum)
		dic['para']  = protext[0]
		dic['title'] = protext[1]
		dic['lists'] = protext[2]
		dic['key'] 	 = key
	return render_template('index2.html',rawe=protext[0],title=protext[1],lists=protext[2],key=key)

@app.route('/pdf',methods=['GET','POST'])
def pdf():
	if request.method == 'POST':
		render = render_template('pdf.html',para=dic['para'],title=dic['title'],lists=dic['lists'],key=dic['key'])
 		config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf')
		pdf = pdfkit.from_string(render, False, configuration=config)
		response = make_response(pdf)
		response.headers['Content-Type'] = 'application/pdf'
		response.headers['Content-Disposition'] = 'attachment; filename=summary.pdf'

		return response


if __name__ == '__main__':
	app.run(debug=True)
