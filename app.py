import sys

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# from model import Issue
# , Rooms, Peoples, Personal, TypeObr
from werkzeug.debug import console

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ind_orig = db.Column(db.Boolean)
    ref_orig = db.Column(db.Integer)
    room_id = db.Column(db.String)
    people_id = db.Column(db.String)
    type_id = db.Column(db.String)
    text = db.Column(db.Text)
    worker_id = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Issue %r>' % self.id


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/table', methods=['POST', 'GET'])
def table():
    tasks = Issue.query.order_by(Issue.timestamp.desc()).all()

    if request.method == "POST":
        ind_orig = True
        room_number = request.form['room_number']
        type_obr = request.form['type_obr']
        text = request.form['text']
        worker_id = request.form['worker_id']

        task = Issue(ind_orig=ind_orig, room_id=room_number, type_id=type_obr,
                     text=text, worker_id=worker_id)

        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/table')

        except:
            return 'При добавлении статьи произошла ошибка!'

    else:
        return render_template('table.html', tasks=tasks)


@app.route('/table_all', methods=['POST', 'GET'])
def table_all():
    tasks = Issue.query.order_by(Issue.timestamp.desc()).all()

    if request.method == "POST":
        ind_orig = True
        room_number = request.form['room_number']
        type_obr = request.form['type_obr']
        text = request.form['text']
        worker_id = request.form['worker_id']

        task = Issue(ind_orig=ind_orig, room_id=room_number, type_id=type_obr,
                     text=text, worker_id=worker_id)

        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/table_all')

        except:
            return 'При добавлении статьи произошла ошибка!'

    else:
        return render_template('table_all.html', tasks=tasks)


@app.route('/task/<int:id_task>/del')
def task_delete(id_task):
    task = Issue.query.get_or_404(id_task)
    tasks = Issue.query.all()

    try:
        print('try', file=sys.stderr)
        if task.ind_orig:
            print('ind_orig', file=sys.stderr)
            for el in tasks:
                print('el', file=sys.stderr)
                if el.ref_orig == id_task:
                    print('ifel', file=sys.stderr)
                    del_task = Issue.query.get_or_404(el.id_task)
                    db.session.delete(del_task)
                    db.session.commit()

        db.session.delete(task)
        db.session.commit()
        return redirect('/table')
    except:
        return "При удалении статьи произошла ошибка!"


@app.route('/task/<int:id_task>', methods=['POST', 'GET'])
def task_detail(id_task):
    task = Issue.query.get_or_404(id_task)
    tasks = Issue.query.order_by(Issue.timestamp.desc()).all()

    if request.method == "POST":
        ind_orig = False
        ref_orig = id_task
        room_id = task.room_id
        type_obr = request.form['type_obr']
        text = request.form['text']
        worker_id = request.form['worker_id']

        task = Issue(ind_orig=ind_orig, ref_orig=ref_orig, room_id = room_id,
                     type_id=type_obr, text=text, worker_id=worker_id)

        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/table')

        except:
            return 'При добавлении статьи произошла ошибка!'

    else:
        return render_template('task_detail.html', task=task, tasks=tasks)


if __name__ == "__main__":
    app.run()
