# from datetime import datetime
#
# from app import db
#
#
# class Issue(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     room_id = db.Column(db.Integer)
#     people_id = db.Column(db.String,)
#     type_id = db.Column(db.String)
#     text = db.Column(db.Text)
#     worker_id = db.Column(db.String)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Issue %r>' % self.id


# class Rooms(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     number_room = db.Column(db.String(10), nullable=False)
#     peoples = db.relationship('Peoples', backref='room', lazy=True)
#     room_id = db.relationship('Issue', backref='number_room', lazy=True)
#
#     def __repr__(self):
#         return '<Room %r>' % self.id
#
#
# class Peoples(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     telephone = db.Column(db.String(15), nullable=True)
#     email = db.Column(db.String(30), nullable=True)
#     telegram = db.Column(db.String(50), nullable=True)
#     room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
#     people_id = db.relationship('Issue', backref='name', lazy=True)
#
#     def __repr__(self):
#         return '<People %r>' % self.id
#
#
# class TypeObr(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type_obr = db.Column(db.String(10), nullable=False)
#     peoples = db.relationship('People', backref='room', lazy=True)
#     type_id = db.relationship('Issue', backref='type_id', lazy=True)
#
#     def __repr__(self):
#         return '<Type_obr %r>' % self.id
#
#
# class Personal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     position = db.Column(db.String(50), nullable=False)
#     worker_id = db.relationship('Issue', backref='worker', lazy=True)
#
#     def __repr__(self):
#         return '<Personal %r>' % self.id
#
#
# class Issue(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
#     people_id = db.Column(db.String, db.ForeignKey('name.id'))
#     type_id = db.Column(db.String, db.ForeignKey('type_obr.id'))
#     text = db.Column(db.Text, nullable=False)
#     worker_id = db.Column(db.String, db.ForeignKey('worker.id'))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Issue %r>' % self.id
