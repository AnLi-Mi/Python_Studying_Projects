from flask import Flask, render_template, request, json
import requests


app=Flask(__name__)

def calc_bmi(w,h):
    return round(w/(h**2),2)

def rec(bmi):
    if bmi<18.5:
        return "You're too skinny"
    elif bmi>25:
        return "You need to loose some weight"
    else:
        return "You have correct weight"

def dog_api():

    url = 'https://random.dog/woof.json'
    parameters = {'format':'json'} 
    dog = requests.get(url, params=parameters)
    return dog.json()['url']

@app.route('/', methods=['GET', 'POST'])
def bmi():
    name = ''
    bmi= ''
    re=''
    if request.method=='POST' and 'username' in request.form:
        name = request.form.get('username')
        w = float(request.form.get('userw'))
        h = float(request.form.get('userh'))
        bmi = calc_bmi(w,h)
        re = rec(bmi)
    return render_template('bmi.html',  name=name, bmi=bmi, re=re)


@app.route('/test', methods=['GET','POST'])
def test():
    dog_pic = dog_api()
    return render_template('dogspics.html', dog_pic=dog_pic)





if __name__ == "__main__":
    app.run(debug=True)
