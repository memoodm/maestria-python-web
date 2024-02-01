from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/home',methods = ['GET'])
def main():
	return render_template('home.html')

@app.route('/submit-form',methods = ['POST'])
def submit():
	return redirect(f"/results?temperatura={request.form['temperatura']}&irradiancia={request.form['irradiancia']}")

@app.route('/results',methods = ['GET'])
def result():
	temperatura = int(request.args.get('temperatura'))
	irradiancia = int(request.args.get('irradiancia'))
	return render_template('result.html',
		temperatura=temperatura,
		irradiancia=irradiancia)

if __name__ == '__main__':
   app.run(debug = True)