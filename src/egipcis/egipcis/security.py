# -*- coding: utf-8 -*-

USERS = {   'tutankamon':'tutan123',
            'ramfis':'ramfis123',
            'radames':'radames123',
            'aida':'aida123',
        }
        
GROUPS = {  'tutankamon':['group:farao','group:sacerdots'],
            'ramfis':['group:sacerdots'],
        }

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])

