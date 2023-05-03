from datetime import datetime

from apps import db


class Product(db.Model):

    __tablename__ = 'product'

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Properties
    article_number = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_when_bought = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    EAN = db.Column(db.String(255))
    url = db.Column(db.String(255))
    
    # Timestamps
    created_at_ts = db.Column(db.Integer, default=int(datetime.now().timestamp()))
    updated_at_ts = db.Column(db.Integer, default=int(datetime.now().timestamp()), onupdate=int(datetime.now().timestamp()))

    # Foreign keys
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('productCategory.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)

    # Relationships
    manufacturer = db.relationship('Manufacturer', backref='product')
    category = db.relationship('ProductCategory', backref='product')
    vendor = db.relationship('Vendor', backref='product')
