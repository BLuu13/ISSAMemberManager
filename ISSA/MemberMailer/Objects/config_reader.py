__author__ = 'Sebastian'

import xml.etree.ElementTree as ET
import os
import sys

class ConfigReader():

    data_file = "E:/Users/Sebastian/Desktop/sample_config2.xml"

    if os.path.exists(data_file) is not True:
        sys.exit("Error: Path is incorrect or file does not exist")

    else:
        # Read from an xml file
        tree = ET.parse(data_file)
        root = tree.getroot()

        print("------------------------------")
        print("Printing Root Element...")
        print("------------------------------")
        print(root.tag)

        print("------------------------------")
        print("Printing Parent Elements...")
        print("------------------------------")
        for child in root:
                print(child.tag)

        print("------------------------------")
        print("Printing Children Elements...")
        print("------------------------------")
        for child in root:
            for children in child:
                print("Key:", children.tag, "-> Value:", children.text)
