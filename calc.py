from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def result():

    # point calculation
    X = request.form.get("X", type=float, default=0)
    B = request.form.get("B", type=float, default=0)
    L = request.form.get("L", type=float, default=0)
    S = request.form.get("S", type=float, default=0)
    BL = request.form.get("BL", type=float, default=0)
    BS = request.form.get("BS", type=float, default=0)
    LS = request.form.get("LS", type=float, default=0)

        
    entry = (X*1) + (B*0.25) + (L*0.35) + (S*0.45) + (BL*0.65) + (BS*0.75) + (LS*0.85)

    return render_template('form.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
