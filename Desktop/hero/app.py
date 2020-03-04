from flask import Flask,render_template,request,make_response
from temp_nltk import url_rize
import pdfkit
import re

app = Flask(__name__)
config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf')


@app.route('/')
def index():
	return render_template('index1.html')

#dic=""
@app.route('/success',methods=['GET','POST'])
def analyze():
	if request.method == 'POST':
		global dic
		key = 'Key Points'
		rawtext = request.form['raw']
		typesum = request.form['typesum']
		protext = url_rize(rawtext,typesum)
		#dic = protext[0]
	return render_template('index2.html',rawe=protext[0],title=protext[1],lists=protext[2],key=key)

@app.route('<rawe>/<title>/<lists>/<key>',methods=['GET','POST'])
def pdf(rawe,title,lists,key):
	if request.method == 'POST':
		#dic2 = dic
		pre = re.sub(r'\'s','!s',lists)
		pre = re.sub(r'[\'\[\]\"]','`',pre)
		pre = re.sub(r'`,\s`','~',pre)
		pre = re.sub(r'!','\'',pre)
		pre = re.sub(r'``','',pre)
		pre = re.sub(r'`','"',pre)
		final = pre.split('~')
		render = render_template('pdf.html',para=rawe,title=title,lists=final,key=key)
		pdf = pdfkit.from_string(render, False, configuration=config)

		response = make_response(pdf)
		response.headers['Content-Type'] = 'application/pdf'
		response.headers['Content-Disposition'] = 'attachment; filename=summary.pdf'
	return response


if __name__ == '__main__':
	app.run()
