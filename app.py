from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if request.form.get('action1') == 'Home':
            return render_template('index.html') # do something
        elif  request.form.get('action2') == 'Product':
            return render_template('index.html#product-section') # do something
        elif  request.form.get('action3') == 'Top Loader':
            return render_template('index.html#toploader-secton') # do something
        elif  request.form.get('action4') == 'Front Loader':
            return render_template('index.html#frontloader-section') # do something
        elif  request.form.get('action5') == 'Q&A':
            return render_template('index.html#qna-section') # do something
        else:
            pass # unknown
    elif request.method == 'GET':
        pass
    return render_template("index.html")

 

if __name__ == '__main__':
    app.run()