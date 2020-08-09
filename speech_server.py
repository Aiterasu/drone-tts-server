from flask import Flask, render_template, Response, request, redirect, url_for
import json
import base64
import requests
import os
import hashlib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('remote.html')

@app.route("/say", methods=['POST'])
def say():
    tosay = request.form.get('tosay');
    output_hash = hashlib.sha256(tosay.encode('utf-8')).hexdigest()
    output_name = output_hash + ".mp3"

    if not os.path.exists(os.path.join("output", output_name)):
        inputjson = {'audioConfig': {   "audioEncoding": "LINEAR16",
                                    "pitch": 0,
                                    "speakingRate": 1},
                'input': {'text': tosay},
                'voice': {'languageCode': 'en-US', 'name': 'en-US-Wavenet-E'}}

        headers = {'Authorization': "Bearer " + os.getenv('GCLOUD_KEY'), 'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post('https://texttospeech.googleapis.com/v1/text:synthesize', json=inputjson, headers=headers)

        j = response.json()
        mp3_data = base64.b64decode(j["audioContent"])

        fout = open(output_name, "wb")
        fout.write(mp3_data)
        fout.close()

        # Robotize and move to output folder
        os.system("sox " + output_name + " output/" + output_name +" echo .5 .5 20 .5")
        os.remove(output_name)

    os.system("mplayer output/" + output_name)

    return render_template('remote.html', said=tosay);