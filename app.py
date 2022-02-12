from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = "43c9a8a18af798652b75ddfb289307385577398efb29ec2d"

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template("home.html", messages=messages)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.run()
