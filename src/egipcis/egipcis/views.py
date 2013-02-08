from pyramid.view import view_config


@view_config(route_name='home', renderer='main.mako')
def my_view(request):
    return {'project':'egipcis','page':"home"}

@view_config(route_name='pagina1', renderer='pagina1.mako', permission='view')
def pg1_view(request):
    return {'project':'egipcis','page':"pagina1"}

@view_config(route_name='pagina2', renderer='pagina2.mako', permission='edit')
def pg2_view(request):
    return {'project':'egipcis','page':"pagina2"}

@view_config(route_name='admin', renderer='admin.mako', permission='admin')
def admin_view(request):
    return {'project':'egipcis','page':"admin"}
