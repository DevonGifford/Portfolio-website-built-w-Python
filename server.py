from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home_function():
    return render_template('index.html')

# @app.route('/index.html')
# def return_home_function():
#     return render_template('index.html')

# @app.route('/works.html')
# def works_function():
#     return render_template('works.html')

# @app.route('/about.html')
# def blog():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact_function():
#     return render_template('contact.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def wrtie_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')

def wrtie_to_csv(data):
    with open('database2.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])  #get means browser wants us to get and post means save
def submit_form():
    if request.method =='POST':
        data = request.form.to_dict()
        wrtie_to_csv(data)                     #or we could use write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'