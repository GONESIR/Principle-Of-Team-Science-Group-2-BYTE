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
    faq_listofQuestions = ["What is BYTECYCLE?", "What BYTECYCLE offers?", "Is it true that I can stay up to date with the latest tech and Bioinformatics news?", \
        "Who runs BYTECYCLE?","Is BYTECYCLE a for or not-for profit organization?"]
    faq_listofAnswers = ["BYTECYCLE LLC is a company that connects communites to the cloud. "  \
        ,"BYTECYCLE provides cloud services through some of the top cloud providers at a lowered rate.", "Yes BYTECYCLE takes advantage of the the cloud service to provide education, media and the latest in science to keep you updated." \
            , "We are group of Bioinformaticians and Software developers." , "BYTECYCLE is an LLC service company."]  
    for i in range(5):
        faq_dictionary[faq_listofQuestions[i]] = faq_listofAnswers[i] 
    return render_template('about.html', about_active=True, faq_dictionary = faq_dictionary)

@app.route('/profile')
def prof():

    return render_template('profile.html')