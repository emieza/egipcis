# -*- coding: utf-8 -*-

from pyramid.view import (
    view_config,
    forbidden_view_config,
)
from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
)
from .security import USERS
from pyramid.security import (
    remember,
    forget,
    )

@view_config(route_name='home', renderer='main.mako')
def my_view(request):
    return { 'project':'egipcis', 'page':"home", 'logged_in':authenticated_userid(request) }

@view_config(route_name='keops', renderer='keops.mako', permission='master')
def pg1_view(request):
    return { 'project':'egipcis', 'page':"Keops", 'logged_in':authenticated_userid(request) }

@view_config(route_name='temple', renderer='temple.mako', permission='sacerdot')
def pg2_view(request):
    return { 'project':'egipcis', 'page':"Temple", 'logged_in':authenticated_userid(request) }

@view_config(route_name='cairo', renderer='cairo.mako', permission='view')
def admin_view(request):
    return { 'project':'egipcis', 'page':"El Cairo", 'logged_in':authenticated_userid(request) }


@view_config(context='.models.Egipcis', name='login',
             renderer='templates/login.pt')
@forbidden_view_config(renderer='templates/login.pt')
def login(request):
    login_url = request.resource_url(request.context, 'login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        if USERS.get(login) == password:
            headers = remember(request, login)
            return HTTPFound(location = came_from,
                             headers = headers)
        message = 'Failed login'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        )

@view_config(context='.models.Egipcis', name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.resource_url(request.context),
                     headers = headers)
                     
