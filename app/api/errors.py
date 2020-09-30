from . import api
from flask import request, render_template
from json import dumps

@api.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = dumps({'error': 'not found'})
        response.status_code = 404
        return response
    else: 
        return render_template('404.html'), 404
    
@api.app_errorhandler(401)
def unauthorized():
    return '登陆错误'