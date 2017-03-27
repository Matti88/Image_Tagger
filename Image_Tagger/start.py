from flask import Flask, current_app, render_template, jsonify

app = Flask(__name__)

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('/home/matteo/Desktop/FlaskApp/static/FOTOIN') if isfile(join('/home/matteo/Desktop/FlaskApp/static/FOTOIN', f))]
file_counter = 0


@app.route('/')
def homepage():
    return  render_template('prompt_pict.html', picture_shown = onlyfiles[0] )


@app.route('/get_data/<type_of_trash>', methods=['GET'])
def get_data_plastic(type_of_trash):
    global file_counter
    print(type_of_trash)
    
    file_counter += 1 

    return  "static/FOTOIN/" + onlyfiles[file_counter]



if __name__ == "__main__":
    app.run()