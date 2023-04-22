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

@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index', API_GENERATOR=len(API_GENERATOR))


@blueprint.route('/<template>')
# @login_required
def route_template(template):
    try:
        model = None
        if not template.endswith('.html'):
            model = template
            template += '.html'
        else:
            model = template.split('.')[0]
            
        # Detect the current page
        segment = get_segment(request)

        # Find the key based on the value in API_GENERATOR
        key = 'users'
        # key = [key for key, value in API_GENERATOR.items() if value == model][0]
        
        g_resp = requests.get('https://www.google.com')
        print(f'Response code: {g_resp.status_code}')


        # Request data from API
        api_endpoint = current_app.config["API_ENDPOINT"]
        api_url = urljoin(api_endpoint, key)
        
        try:
            response = requests.get(api_url, timeout=1)
            response.raise_for_status()
            data = response.json()
            return render_template("home/" + template, 
                                   segment=segment, 
                                   API_GENERATOR=API_GENERATOR, 
                                   model=model, 
                                   template=template, 
                                   data=data)
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

    # except:
        # return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
