_author__ = 'Sebastian'

import xml.etree.ElementTree as ET
import os # can use this to find a path on local hard drive
import sys

class ConfigReader():

    # data_file = "E:/Users/Sebastian/Desktop/sample_config2.xml
    config_location = '.\config\membermailer.xml'

    def __init__(self):
        try:
            self.config = ET.parse(self.config_location)
            self.read_config()
            # 2 methods below could be called apart from initialization
            # They are placed there right now just for testing purposes
            self.print_root()
            self.print_parent() 
        except ET.ParseError as error:
            # todo: something to pull down generic membermailer.xml from web
            sys.exit("Error: Path is incorrect or file does not exist")

    def read_config(self):
        self.root = self.config.getroot()
      # self.database - get db file location from config

    def print_root(self):
        print("------------------------------")
        print("Printing Root Element...")
        print("------------------------------")
        print(self.root.tag)

    def print_parent(self):
        print("------------------------------")
        print("Printing Parent Elements...")
        print("------------------------------")
        for child in self.root:
                print(child.tag)
    
    def print_children(self):
        print("------------------------------")
        print("Printing Children Elements...")
        print("------------------------------")
        for child in self.root:
            for children in child:
                print("Key:", children.tag, "-> Value:", children.text)

