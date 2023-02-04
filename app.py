from flask import Flask, flash, request, redirect, url_for, render_template
import shutil
import urllib.request
import os
from werkzeug.utils import secure_filename
import argparse
import matplotlib.pyplot as plt
from colorizers import *
from colorizers.model import generator

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# load colorizers
colorizer_eccv16 = eccv16(pretrained=True).eval()
colorizer_siggraph17 = siggraph17(pretrained=True).eval()
colorizer_temp=generator(pretrained=False).eval()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    file.filename = "test.png"
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')

        # default size to process images is 256x256
        # grab L channel in both original ("orig") and resized ("rs") resolutions
        img = load_img("./static/uploads/"+filename)
        (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))

        # colorizer outputs 256x256 ab map
        # resize and concatenate to original L channel
        img_bw = postprocess_tens(tens_l_orig, torch.cat((0*tens_l_orig,0*tens_l_orig),dim=1))
        out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
        out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())

        temp=postprocess_tens(tens_l_orig, colorizer_temp(tens_l_rs).cpu())

        plt.imsave('static/uploads/eccv16.png', out_img_eccv16)
        plt.imsave('static/uploads/siggraph17.png', out_img_siggraph17)
        plt.imsave('static/uploads/temp.png', temp)

        return render_template('index.html', filename=filename,output_sigg='./siggraph17.png',output_eccv='./eccv16.png')
    # else:
    #     flash('Allowed image types are - png, jpg, jpeg, gif')
    #     return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/display_sigg/<output_sigg>')
def display_sigg(output_sigg):
    return redirect(url_for('static', filename='uploads/' + output_sigg), code=301)
    
@app.route('/display_eccv/<output_eccv>')
def display_eccv(output_eccv):
    return redirect(url_for('static', filename='uploads/' + output_eccv), code=301)

if __name__ == "__main__":
    app.run()
