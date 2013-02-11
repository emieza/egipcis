# -*- coding: utf-8 -*-

from pyramid.security import (
    Allow,
    Everyone,
    )
    
    
class Egipcis():
    __name__ = None
    __parent__ = None
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:sacerdots', 'sacerdots'),
                (Allow, 'group:farao', 'master')
            ]

