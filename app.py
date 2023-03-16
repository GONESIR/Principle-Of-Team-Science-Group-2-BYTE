from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
faq_dictionary = {}

@app.route('/')
def index():

    return render_template('index.html', home_active=True)


@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/contact')
def contact():
    return render_template('contact.html', contact_active=True)


@app.route('/about')
def info():
    faq_listofQuestions = ["What is BYTE?", "Why to join BYTE?", "How much does it cost to get trained?", \
        "Who runs BYTE?","Is BYTE for or not-for profit organization?"]
    faq_listofAnswers = ["BYTE stands for Bioinformatics Youth Training Enthusiasts"  \
        ,"BYTE provides educational services in the emerging field of Bioinformatics.", "You will benefit from world class education absolutely free!!" \
            , "We are group of Bioinformaticians and Software developers." , "BYTE is a 501(c)(3) non-profit organization."]  
    for i in range(5):
        faq_dictionary[faq_listofQuestions[i]] = faq_listofAnswers[i] 
    return render_template('about.html', about_active=True, faq_dictionary = faq_dictionary)

@app.route('/profile')
def prof():

    return render_template('profile.html')