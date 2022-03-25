from application import app, db_NoSQL
from flask import render_template, request, json, Response, flash, redirect
from application.models import User, Courses, Enrollment
from application.forms import LoginForm, RegistrationForm
courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]


# current_year = datetime.datetime.now().year

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True )

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm
    if form.validate_on_submit:
        if request.form.email == 'terry@brooksjr.com':
        flash("You have successfully logged in")
        return redirect(url_for(TBD)))
    else:
        return render_template("login.html", login=True,title='Login',form=form() )

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    return render_template("courses.html", courseData=courseData, courses = True, term=term )

@app.route("/register")
def register():
    form = RegistrationForm
    return render_template("register.html", title='Register', register=True, form=form())

@app.route("/enrollment", methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form['title']
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data={"id":id,"title":title,"term":term})    

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    
    return Response(json.dumps(jdata), mimetype="application/json")


@app.route('/user')
def user():
    users = User.objects.all()
    return render_template('users.html', users=users)

