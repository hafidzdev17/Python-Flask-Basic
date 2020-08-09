from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/file')
def file():
    fruits = ['Mango', 'Apple', 'Orange']
    return render_template('file.html', fruits=fruits)
    # return "route about :"+ url_for('about')
    # return redirect(url_for('about'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
