from flask import Flask
from flask import Flask, request, render_template
import os
import Vote

app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def home():
    menu = os.path.join(app.config['UPLOAD_FOLDER'], 'menu.png')
    index = os.path.join(app.config['UPLOAD_FOLDER'], 'index.png')
    sect1 = os.path.join(app.config['UPLOAD_FOLDER'], 'sectiunea1.png')
    footer = os.path.join(app.config['UPLOAD_FOLDER'], 'footer.png')
    submit = os.path.join(app.config['UPLOAD_FOLDER'], 'SUBMIT.png')
    
    if len(request.args)!=0:
        string = "<p>" + str(Vote.vote(request.args['sentence'])) + "</p>"
        return render_template('index.html', menu_img = menu, index_img = index, sect1_img = sect1, footer_img = footer, submit_img = submit, data = string)

    return render_template('index.html', menu_img = menu, index_img = index, sect1_img = sect1, footer_img = footer, submit_img = submit)

@app.route('/stats.html')
def stats():
    menu = os.path.join(app.config['UPLOAD_FOLDER'], 'bara_stats.png')
    index = os.path.join(app.config['UPLOAD_FOLDER'], 'index.png')
    footer = os.path.join(app.config['UPLOAD_FOLDER'], 'footer.png')
    graph1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Capture.PNG')

    return render_template('stats.html', menu_img = menu, index_img = index, footer_img = footer, graph1_img = graph1)

if __name__ == '__main__':
    app.run(debug=True) 