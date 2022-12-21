from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('j.html')

@app.route('/info')
def info():
    return "<h1>Hello 12345 Django</h1>"

@app.route('/int/<name>')
def int(name):
    return "last char of a name = {}".format((name[-1]))



@app.route('/friend/<name>')
def friend(name):
    return "<h1>My friend name is {}</h1>".format(name)

if __name__=='__main__':
    app.run(debug=True)