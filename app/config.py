from configparser import ConfigParser

class parser:

    def configTrue():
        from os import path
        if path.isfile(config.ini):
            return True

    #read config file
    def config():
        Config = configparser.ConfigParser()
        
        if parser.configTrue():
            Config.read(config.ini)
            return Config

    def localhost():
        host = parser.config()
        host = host['server']['actualyServer']
        return host

    def bbc():
        bbc = parser.config()
        bbc = bbc['server']['bbc']
        return bbc

    def drc():
        drc = parser.config()
        drc = drc['server']['drc']
        return drc

    def dev():
        dev = parser.config()
        dev = dev['server']['dev']
        return dev

    def path():
        path = parser.config()
        path = path['server']['path']
        return path

    def file():
        file = parser.config()
        file = file['server']['file']
        return file



    
        
