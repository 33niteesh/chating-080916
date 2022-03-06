from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def on_load():
    file=open("msg.txt","r")
    msg=file.readline()
    return render_template("index.html",msg=msg)
@app.route('/send',methods=['POST'])
def send():
    file=open("msg.txt","w")
    if request.method == 'POST':
        msg=request.form.get("message")
        file.write(msg)
        return render_template("index.html",msg=msg)
if __name__ == '__main__':
    app.run()