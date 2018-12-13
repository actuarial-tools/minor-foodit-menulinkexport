import configparser
import logging
import logging.handlers as handlers
import time

#Logging
logger = logging.getLogger('Minor FoodIT')
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logHandler = handlers.RotatingFileHandler('log\\app.log', maxBytes=1000000, backupCount=10)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

class ConfigureData(object):
    """
    Example file format c:\\tomorrow.ini
    """
    def __init__(self,filename=None):
        self.config = configparser.ConfigParser()
        if filename is not None and filename.endswith(".ini"):
            self.config.read(filename)

    def getSection(self):
        return self.config.sections()

    """
        Usage as below
        Name = ConfigSectionMap("SectionOne")['name']
    """
    def ConfigSectionMap(self,section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1