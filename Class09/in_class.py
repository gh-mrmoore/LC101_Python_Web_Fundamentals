#this is run before anything else is done
@app.before_request
def require_login():
    allowed_routes = ['login', 'register']   #have to be careful how to handle this if splitting GET and POST methods
    if request.endpoint not in allowed_routes and 'email' not in session:
        return redirect('/login')





