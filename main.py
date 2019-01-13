import os
from PIL import Image
import pytesseract
from serial import Serial
import base64
import speech_recognition as sr
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import time
import threading

"""app = Flask(__name__)

UPLOAD_FOLDER = "C:/Users/Diptanshu Mittal/Desktop/website"
ALLOWED_EXTENSIONS = set(['txt', 'wav','jpg','pnj'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    



@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        #sr=Serial('COM3',9600)
        file=request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        j=file.filename
        text=''
        if j.find(".wav")!=-1:
            r = sr.Recognizer()
            audio = j
            with sr.AudioFile(audio) as source:
                audio= r.record(source)
            try:
                text =r.recognize_google(audio)
            except Exception as e:
                print (e)
            contents = text
            return render_template("password.html")
            for i in contents:
                sr.write(str.encode(i))
        elif j.find(".jpg")!=-1:
            im=Image.open(j)
            contents=pytesseract.image_to_string(im, lang="eng")
            contents = file1.read()
            return render_template("password.html",name=contents)
            for i in contents:
                sr.write(str.encode(i))
            
        elif j.find(".txt")!=-1:
            file1 = open(j,"r")
            contents = file1.read()
            return render_template("password.html",name=contents)
            #for i in contents:
            #sr.write(str.encode('a'))
            #print(sr.readline())
        


if __name__=='__main__':
    app.run(debug=True)"""
import os
import base64
import speech_recognition as sr
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "C:/Users/Diptanshu Mittal/Desktop/website"
ALLOWED_EXTENSIONS = set(['txt', 'wav','jpg','pnj'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    



@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        sr=Serial('COM3',9600)
        file=request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        j=file.filename
        text=''
        if j.find(".wav")!=-1:
            r = sr.Recognizer()
            audio = j
            with sr.AudioFile(audio) as source:
                audio= r.record(source)
            try:
                text =r.recognize_google(audio)
            except Exception as e:
                print (e)
            contents = text
            return render_template("password.html",name=contents)
            for i in contents:
                sr.write(str.encode(i))
        elif j.find(".txt")!=-1:
            file1 = open(j,"r")
            contents = file1.read()
            #download_thread = threading.Thread()
            #download_thread.start()
            for i in contents:
                sr.write(str.encode(i))
                time.sleep(2)
            return render_template("password.html",name=contents)
            

        else:
            im=Image.open(j)
            contents=pytesseract.image_to_string(im, lang="eng")
            contents=contents.upper()
            for i in contents:
                sr.write(str.encode(i))
                time.sleep(2)
            return render_template("password.html",name=contents)
            
if __name__=='__main__':
    app.run(debug=True)

