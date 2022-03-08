from flask import Flask, render_template, request, jsonify, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/taxCalc', methods=['POST', 'GET'])
def taxCalc():
    response = {}
    data = request.get_json()
    if data.get('income'):
        income = float(data['income'])
        status = data['status']
        npwp = data['npwp']

        #status buat ptkp
        if status == 'TK0':
            ptkp = 54000000
        elif status == 'TK1':
            ptkp = 58500000
        elif status == "TK2":
            ptkp = 63000000
        elif status == "K0":
            ptkp = 58500000
        elif status == "K1":
            ptkp = 63000000
        elif status == "K2":
            ptkp = 67500000
        else:
            ptkp = 72000000
        
        posFee = income * 0.05
        if posFee > 6000000:
            posFee = 6000000

        regSub = ptkp + posFee
        
        pkp = income - regSub
        
        if pkp >= 0 and pkp <= 60000000:
            result = (pkp * 0.05) / 12
        elif pkp > 60000000 and pkp <= 250000000:
            result = ( (60000000 * 0.05) + ( (pkp - 60000000) * 0.15 ) ) / 12
        elif pkp > 250000000 and pkp <= 500000000:
            result = ( (60000000 * 0.05) + ( (250000000 - 60000000) * 0.15 ) + ( (pkp - 250000000) * 0.25 ) ) / 12
        elif pkp > 500000000 and pkp <= 5000000000:
            result = ( (60000000 * 0.05 ) + ( (250000000 - 60000000) * 0.15 ) + ( (500000000 - 250000000) * 0.25 ) + ( (pkp - 500000000) * 0.3) ) / 12
        elif pkp > 5000000000:
            result = ( (60000000 * 0.05 ) + ( (250000000 - 60000000) * 0.15 ) + ( (500000000 - 250000000 ) * 0.25) + ( (5000000000 - 500000000) * 0.3 ) +  ( (pkp - 5000000000) * 0.35) ) / 12
        else:
            result = 0

        if npwp == 'n':
            result = result + (result * 0.2)
        
        response = {'status': 200, 'result': result, 'pkp': pkp, 'regsub': regSub, 'posfee': posFee, 'ptkp': ptkp}
    else:
        response = {'status': 500, 'result': 'Error'}
    return jsonify(response)
