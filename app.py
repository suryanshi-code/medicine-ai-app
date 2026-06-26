from flask import Flask,render_template,request,redirect

app=Flask(__name__)

patients=[]
active_patient=0

@app.route("/home",methods=["GET","POST"])
def home():
    global active_patient

    if request.method=="POST":
     
         name=request.form.get("patient","").upper()
         age=request.form.get("age","")
         symptoms=request.form.get("symptoms","").upper()
         medicine=request.form.get("medicine","").upper()
         dose=request.form.get("dose","")
         time=request.form.get("time","").upper()
        
         if name and age and symptoms:
              patient={
                   "NAME": name, 
                   "AGE":age,
                   "SYMPTOMS":symptoms,
                   "MEDICINE":medicine,
                   "DOSE":dose,
                   "TIME":time

              }

              patients.append(patient)
              active_patient = len(patients) - 1

                                             
    if len(patients) == 0:
         return render_template("index.html", patient=None,patients=[])
    

    # 🔥 HANDLE CLICK
    clicked_name = request.args.get("name")

    if clicked_name:
        for i, p in enumerate(patients):
            if p["NAME"] == clicked_name:
                active_patient = i
                selected_name = p
                break
    else:
        selected_name = patients[active_patient]

    return render_template("index.html",patients=patients,patient=selected_name)

@app.route("/delete",methods=["POST"])
def delete():
     global active_patient

     if len(patients) > 0:
        patients.pop(active_patient)
     return redirect("/home")

@app.route("/add",methods=["POST"])
def add():
     global active_patient
     patient={
          "NAME": "", 
          "AGE":"",
          "SYMPTOMS":"",
          "MEDICINE":"",
          "DOSE":"",
          "TIME":""

     }
          
     patients.append(patient)

     active_patient=len(patients)-1

     return redirect("/home")


if __name__ == "__main__":
     app.run(debug=True)