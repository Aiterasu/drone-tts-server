# Drone TTS Server

A simple Flask server to send TTS to remote drones. Use at your own risk.

Uses gcloud TTS.

## Pre-requisites

```sudo apt-get install mplayer sox libsox-fmt-all```
```pip3 install --user flask```
[gcloud SDK](https://cloud.google.com/sdk/downloads)
export GOOGLE_APPLICATION_CREDENTIALS [as in here](https://cloud.google.com/docs/authentication/getting-started)
The project must have cloud TTS enabled.

## Running
```bash
export GCLOUD_KEY=$(gcloud auth application-default print-access-token)
export FLASK_APP=speech_server.py
flask run --host=0.0.0.0
```
