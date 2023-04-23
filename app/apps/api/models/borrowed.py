from datetime import datetime

from apps import db


class Borrowed(db.Model):

    __tablename__ = 'borrowed'

    # Primary key
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)

    # Properties
    quantity = db.Column(db.Integer, nullable=False, default=1)
    returned = db.Column(db.Integer, nullable=False, default=0)
    estimated_return_date = db.Column(db.Integer, nullable=False, default=int(datetime.now().timestamp()))

    # Timestamps
    created_at_ts = db.Column(db.Integer, default=int(datetime.now().timestamp()))
    updated_at_ts = db.Column(db.Integer, default=int(datetime.now().timestamp()), onupdate=int(datetime.now().timestamp()))

    # Relationships
    product = db.relationship('Product', backref='Borrowed')
    user = db.relationship('Users', backref='Borrowed')