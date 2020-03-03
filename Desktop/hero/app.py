from flask import Flask,render_template,request,make_response
import pdfkit

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index1.html')


@app.route('/success',methods=['GET','POST'])
def pdf():
	if request.method == 'POST':
		config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf')
		render = render_template('index1.html')
		pdf = pdfkit.from_string(render, False, configuration=config)

		response = make_response(pdf)
		response.headers['Content-Type'] = 'application/pdf'
		response.headers['Content-Disposition'] = 'attachment; filename=summary.pdf'

		return response


if __name__ == '__main__':
	app.run(debug=True)
