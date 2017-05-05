import platform, app.config as config

def getServerName():
    whereIam = platform.node()
    if config.parser.localhost == whereIam:
        return whereIam
    elif config.parser.bbc == whereIam:
        return config.parser.bbc
    elif config.parser.drc == whereIam:
        return config.parser.drc
    elif config.parser.dev == whereIam:
        return config.parser.dev
    
    
    


