import os
import requests
from flask import Flask, jsonify, render_template,request
app = Flask(__name__) # creating the app

API_KEY = os.environ['API_KEY']
# single / for the home
@app.route("/")  # adding directory for the next exactly function
def index(): # any func name
    return render_template("index.html")


# /convert will not be seen in browser
@app.route("/convert", methods = ["POST"]) 
def convert(): 
    
    # get from html the input
    currency = request.form.get("currency")  # gettinng from the form the text in input with id "currency"
    url = "https://api.currencyapi.com/v3/latest"
    headers = {'apikey': API_KEY ,'base_currency': 'USD' , 'currencies':'EUP'}

    response = requests.request("GET", url, headers=headers)
  
    if response.status_code != 200:
        return jsonify({"success": False})
    

    data = response.json() # getting the json from the api 


    if currency not in data['data']:
        return jsonify({'success': False})
    
    
    return jsonify({"success": True, "rate" : data['data'][currency]['value']})  # it equals the value 
