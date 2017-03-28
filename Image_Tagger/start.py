

from flask import Flask, current_app, render_template, jsonify
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

onlyfiles = [f for f in listdir('../FlaskApp/static/FOTOIN') if isfile(join('../FlaskApp/static/FOTOIN', f))]
how_many_picture = len(onlyfiles)
file_counter = -1
session_finished = '/static/session_end.jpg'

text_file = open("../FlaskApp/static/tag_dataset.txt", "w")


@app.route('/')
def homepage():
    return  render_template('prompt_pict.html', picture_shown ='/static/session_start.jpg' )


@app.route('/get_data/<type_of_trash>', methods=['GET'])
def get_data_plastic(type_of_trash):

    global file_counter , text_file

    print(type_of_trash)
    
    file_counter += 1 
    print(file_counter)

    if file_counter == how_many_picture:
        file_counter = -1
        text_file.close()
        return session_finished

    else:
        text_file.write("static/FOTOIN/" + onlyfiles[file_counter] + ',' + str(type_of_trash) + '\n' )

        return  "static/FOTOIN/" + onlyfiles[file_counter]



if __name__ == "__main__":
    app.run()
