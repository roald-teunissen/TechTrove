# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from urllib.parse import urljoin

import requests
from apps.config import API_GENERATOR
from apps.home import blueprint
from flask import current_app, flash, render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import http
from datetime import datetime


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index', API_GENERATOR=len(API_GENERATOR))

def get_vendors_data(data):
    all_vendors = data['data']
    vendor_count = len(all_vendors)
    # product_data = requests.get(url=urljoin(current_app.config["API_ENDPOINT"], 'product')).json()['data']
    
    # join vendor data with product data
    # print(type(product_data))
    # print(data)
    # print(type(data[0]))
    # request product data and join with vendor data
    # product = requests.get(url=urljoin(current_app.config["API_ENDPOINT"], 'product'))
    
    # return render_template("home/" + template, 
    #                     segment=get_segment(request), 
    #                     API_GENERATOR=API_GENERATOR, 
    #                     model=model_name, 
    #                     template=template, 
    #                     data=result)
    print('vendor_count:', vendor_count)
    return {'all_vendors': all_vendors, 'vendor_count': vendor_count}

def get_manufacturers_data(data):
    return data

def get_users_data(data):
    return data

template_data_functions = {
    'vendor': get_vendors_data,
    'manufacturer': get_manufacturers_data,
    'users': get_users_data,
}

@blueprint.route('/<template>')
# @login_required
def route_template(template):
    try:
        model_name = template if not template.endswith('.html') else template[:-5]
        api_url = urljoin(current_app.config["API_ENDPOINT"], model_name)

        try:
            response = requests.get(url=api_url, timeout=1)
            response.raise_for_status()
            
            # Convert timestamp to datetime for created_at and updated_at
            result = response.json()
            for item in result['data']:
                if 'created_at_ts' in item and 'updated_at_ts' in item:
                        item['created_at_dt'] = datetime.fromtimestamp(item['created_at_ts']).strftime('%Y-%m-%d %H:%M')
                        item['created_at_dt'] = datetime.fromtimestamp(item['updated_at_ts']).strftime('%Y-%m-%d %H:%M')

            # Call child function to add more data
            result = template_data_functions[model_name](result)
            
            return render_template("home/" + template, data=result)
            
        except requests.exceptions.HTTPError as error:
            status_code = error.response.status_code
        except requests.exceptions.ConnectionError:
            status_code = 500
        except requests.exceptions.Timeout:
            status_code = 408
        except requests.exceptions.RequestException:
            status_code = 408
        error_message = "API error: " + http.HTTPStatus(status_code).phrase

        print('API url:', api_url)
        print('Error: ', error_message)
        return render_template('home/page-error.html', status_code=status_code, status_text=error_message), status_code

    except TemplateNotFound:
        return render_template('home/page-error.html', status_code=404, status_text=http.HTTPStatus(404).phrase), 404


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
