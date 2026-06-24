from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/home",methods=["GET","POST"])
def home():
    name=""
    age=""
    symptoms=""
    message=""
    if request.method=="POST":
         name=request.form.get("patient","").upper()
         age=request.form.get("age","")
         symptoms=request.form.get("symptoms","")
         message= "Data recorded. Please consult a doctor."

    return render_template("index.html",name=name,age=age,symptoms=symptoms,message=message)

if __name__ == "__main__":
     app.run(debug=True)