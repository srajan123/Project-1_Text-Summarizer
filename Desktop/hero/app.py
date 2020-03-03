from flask import Flask,render_template,make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
	render = render_template('index1.html')
	pdf = pdfkit.from_string(render,False)

	response = make_response(pdf)
	response.headers['Content-Type'] = 'application/pdf'
	response.headers['Content-Disposition'] = 'attachment; filename=out.pdf'

	return response

if __name__ == '__main__':
	app.run(debug=True)
