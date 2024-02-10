from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name') 
    template = f'''
        <h1>Welcome {name}!</h1>
    '''
    return render_template_string(template)

if __name__ == '__main__':
   app.run(debug=True)

# flask run 
# http://127.0.0.1:5000/?name=%3Cscript%3Ealert(%22xss%22)%3C/script%3E