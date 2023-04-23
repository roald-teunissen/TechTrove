# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
from apps import db
from apps.authentication.models import Users


class Manufacturer(db.Model):

    __tablename__ = 'Manufacturer'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Properties
    name = db.Column(db.String(255), nullable=False)
    
class ProductCategory(db.Model):

    __tablename__ = 'ProductCategory'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Properties
    name = db.Column(db.String(255), nullable=False)

class Vendor(db.Model):

    __tablename__ = 'Vendor'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Properties
    name = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255))

class Product(db.Model):

    __tablename__ = 'Product'

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
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('Manufacturer.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('ProductCategory.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('Vendor.id'), nullable=False)

    # Relationships
    manufacturer = db.relationship('Manufacturer', backref='products')
    category = db.relationship('ProductCategory', backref='products')
    vendor = db.relationship('Vendor', backref='products')

class Borrowed(db.Model):

    __tablename__ = 'Borrowed'

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

class Ordered(db.Model):

    __tablename__ = 'Ordered'

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Foreign keys
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'))
    vendor_id = db.Column(db.Integer, db.ForeignKey('Vendor.id'))

    # Properties
    ordered = db.Column(db.Integer, nullable=False, default=0)
    delivered = db.Column(db.Integer, nullable=False, default=0)

    # Timestamps
    created_at_ts = db.Column(db.Integer, default=int(datetime.now().timestamp()))
    updated_at_ts = db.Column(db.Integer, default=int(datetime.now().timestamp()), onupdate=int(datetime.now().timestamp()))

    # Relationships
    product = db.relationship('Product', backref='Ordered')
    vendor = db.relationship('Vendor', backref='Ordered')