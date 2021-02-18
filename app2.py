from flask import render_template,Flask,request
app = Flask(__name__)
@app.route('/')
def upload():
    return render_template("upload.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template("success.html", name=f.filename)


if __name__ == '__main__':
    app.run()