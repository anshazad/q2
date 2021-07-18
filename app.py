import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    
    
    nterms = int(jsonObj["How many terms? "])


    n1, n2 = 0, 1
    count = 0

# check if the number of terms is valid
    if nterms <= 0:
    response+="<b> Please enter a positive integer </b>")
    
# if there is only one term, return n1
    elif nterms == 1:
     response+="<b>" + n1 + "</b>"
# generate fibonacci sequence
    else:
     response+="<b> fibonacci series: </b>"
     while count < nterms:
       response+="<b>" + n1 + "</b>"
       nth = n1 + n2
# update values
       n1 = n2
       n2 = nth
       count += 1
  
    
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
