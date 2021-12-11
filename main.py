# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:05:06 2021
@author: HP
"""
from flask import Flask, jsonify, request
from TestResultModel import TestResult
#from TrainChatbotModel import GenerateResponse, intents
import json


app = Flask(__name__)

#response = ''

@app.route('/res', methods = ['POST'])
def testResult():
    #abc = 'Welcome to Emobot', result
    #global response
    requestData = request.data
    requestData = json.loads(requestData.decode('utf-8'))
    answers = requestData['answers']
    return jsonify(result = TestResult(answers))

#@app.route('/chat', methods = ['POST'])
#def chatResponse():
    #requestData = request.data
    #requestData = json.loads(requestData.decode('utf-8'))
    #userMessage = requestData['message']
    #return jsonify(response = GenerateResponse(intents, userMessage))

@app.route('/home', methods = ['GET'])
def home():
    return jsonify({"message" : "Welcome to EMOBOT"})

if __name__ == '__main__':
    app.run(host = "127.0.0.1",debug = False)
    
    

#[1,3,3,2,1,3,2]
