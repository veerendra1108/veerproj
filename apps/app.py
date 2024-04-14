from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = round(weight / (height / 3.281)**2, 2)
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')