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
         gender=request.form.get("gender","").upper()
         symptoms=request.form.get("symptoms","").upper()
         medicine=request.form.get("medicine","").upper()
         dose=request.form.get("dose","")
         time=request.form.get("time","").upper()
         date=request.form.get("date","").upper()
         duration=request.form.get("duration","").upper()
         lab_tests=request.form.get("lab_tests","").upper()
         prescriptions=request.form.get("prescriptions","").upper()
         diagnosis=request.form.get("diagnosis","").upper()


        
         if name and age and symptoms:
              patient={
                   "NAME": name, 
                   "AGE":age,
                   "GENDER":gender,
                   "SYMPTOMS":symptoms,
                   "MEDICINES":[
                        {
                         "medname":medicine,
                         "dose":dose,
                         "time":time,
                         "duration":duration
                        }],
                    "DATE":date,
                    "LAB_TESTS":lab_tests,
                    "PRESCRIPTIONS":prescriptions,
                    "DIAGNOSIS":diagnosis
                    }
                   


              patients.append(patient)
              active_patient = len(patients) - 1

                                             
    if len(patients) == 0:
         return render_template("index.html", patient=None,patients=[])
    selected_name=None
    clicked_name = request.args.get("name")

    if clicked_name:
        for i, p in enumerate(patients):
            if p["NAME"] == clicked_name:
                active_patient = i
                selected_name = p
                break
    if selected_name is None and len(patients) > 0:
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
     return redirect("/home")


if __name__ == "__main__":
     app.run(debug=True)