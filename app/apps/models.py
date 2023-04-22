# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db

class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_when_bought = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    EAN = db.Column(db.String(255))
    created_at = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.Integer, nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    manufacturer = db.relationship('Manufacturer', backref='products')
    category = db.relationship('ProductCategory', backref='products')
    vendor = db.relationship('Vendor', backref='products')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.Integer, nullable=False)

class Borrow(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    returned = db.Column(db.Integer, nullable=False, default=0)
    estimated_return_date = db.Column(db.Integer, nullable=False, default=0)
    borrowed_at = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref='borrows')
    user = db.relationship('User', backref='borrows')

class Ordered(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), primary_key=True)
    ordered = db.Column(db.Integer, nullable=False, default=0)
    delivered = db.Column(db.Integer, nullable=False, default=0)
    ordered_at = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref='orders')
    vendor = db.relationship('Vendor', backref='orders')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
