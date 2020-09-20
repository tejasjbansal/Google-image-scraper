import os
from flask import Flask ,request,render_template,url_for
from flask_cors import CORS, cross_origin
import imagescraper
app = Flask(__name__)


@app.route("/")
@cross_origin()
def index():
   return render_template('index.html')

@app.route("/result",methods=['POST'])
@cross_origin()
def showingImages():
    if request.method=='POST':
        query = request.form['content']
        imagescraper.main(query)
        return render_template("result.html",query=query)
    

port = int(os.getenv("PORT"))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
    #app.run(host='127.0.0.1', port=5000, debug=True)





