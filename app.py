from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#Make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#Set a secret key
app.config["SECRET_KEY"] = 'your secret key'

#Function to request student data from the api
#Input: url
#Output: JSON student data
def get_student_data(url):
    #make a request
    response = requests.get(url)
    #convert format to JSON
    response_json = response.json()
    return response_json

#Create route for site index. Will display all student data
@app.route('/', methods = ['GET'])
def index():
    #Make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    student_data = get_student_data(url)
    return render_template('index.html', student_data=student_data)

#Create a route for the majors search page
@app.route('/majors', methods=['GET', 'POST'])
def majors():

    #Make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    student_data = get_student_data(url)
    major_list = []

    #Write code that gets the unique majors from the student_data list
    for students in student_data:
        if students['major'] not in major_list:
            major_list.append(students['major'])
    
    if request.method == 'POST':
        #Get the form data
        major = request.form['major'].strip()
        #Create list to store results
        results_list = []

        #Validate form data
        if not major:
            flash("You must select a major.")
        else:
            #get students with selected major and place in results list
            for students in student_data:
                if students['major'] == major:
                    results_list.append(students)
            return render_template('majors.html', major_list = major_list, results_list = results_list)

    return render_template('majors.html', major_list = major_list)

#run the flask application
app.run(port = 5007)