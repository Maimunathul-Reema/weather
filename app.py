from flask import Flask,render_template,request
import pickle





app = Flask(__name__)

with open ('Weather_DT.pkl','rb') as f:
    model=pickle.load(f)

#by default method get
@app.route('/')   #it is use to routing path for url
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')
    
@app.route('/result',methods=['POST','GET'])
def result():
    Minimum_Temperature=float (request.form.get('mintemp'))
    Maximum_Temperature=float(request.form.get('maxtemp'))
    RainFall=float(request.form.get('rainfall'))
    Evaporation=float( request.form.get('evaporation'))
    Sunshine=float(request.form.get('sunshine'))
    Wind_Gust_Speed=float(request.form.get('windgustspeed'))
    WindSpeed9am=float(request.form.get('windspeed9'))
    WindSpeed3pm=float(request.form.get('windspeed3'))
    Humidity9am=float(request.form.get('humidity9'))
    Humidity3pm=float(request.form.get('humidity3'))
    Pressure9am=float(request.form.get('pressure9'))
    Pressure3pm=float(request.form.get('pressure3'))
    Cloud9am=float(request.form.get('cloud9'))
    Cloud3pm=float(request.form.get('cloud3'))
    Temperature9am=float(request.form.get('temperature9'))
    Temperature3pm=float(request.form.get('temperature3'))

    input=[[Minimum_Temperature, Maximum_Temperature, RainFall, Evaporation, Sunshine, Wind_Gust_Speed,WindSpeed9am,
                                                 WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temperature9am,Temperature3pm]]
         
    predict=model.predict(input)
    print(predict)

    predict= [1, 0]  # Example output from a model

    rain_today = "Yes" if predict[0] == 1 else "No"
    rain_tomorrow = "Yes" if predict[1] == 1  else "No"

    return render_template('result.html', rain_today=rain_today, rain_tomorrow=rain_tomorrow)



if __name__=='__main__':
    app.run(debug=True)