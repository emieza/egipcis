# -*- coding: utf-8 -*-

from pyramid.security import (
    Allow,
    Everyone,
    )
    
    
class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:sacerdots', 'sacerdots'),
                (Allow, 'group:farao', 'master')
            ]
    def __init__(self, request):
        pass
        

