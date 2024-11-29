from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table = {i: number * i for i in range(1, 11)}
            return render_template('index.html', table=table, number=number)
        except ValueError:
            return render_template('index.html', error="Please enter a valid number")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
