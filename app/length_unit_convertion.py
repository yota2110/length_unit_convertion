from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_unit = request.form.get('from_unit')
        to_unit = request.form.get('to_unit')
        value = float(request.form.get('value'))

        result = convert_units(from_unit, to_unit, value)
        return render_template('length_unit_convertion.html', result=result, from_unit=from_unit, to_unit=to_unit, value=value)

    return render_template('length_unit_convertion.html')

def convert_units(from_unit, to_unit, value):
    units = {
        'm': 1,
        'cm': 0.01,  # 1メートル = 100センチメートル
        'mm': 0.001,
        # 他の単位も追加
    }

    try:
        result = value * units[from_unit] / units[to_unit]
        return round(result, 2)
    except KeyError:
        return "Invalid units"

if __name__ == '__main__':
    app.run(debug=True)
