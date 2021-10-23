from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/total', methods=["GET", "POST"])
def total():
    if request.method == "POST":
        mynumber1 = request.form.get("value1")
        mynumber2 = request.form.get("value2")
        mynumber3 = request.form.get("value3")
        
        return render_template('number.html', total=int(mynumber1)+int(mynumber2)+int(mynumber3))
    else:
        return render_template('number.html')

if __name__ == "__main__":
    app.run(debug=True)
