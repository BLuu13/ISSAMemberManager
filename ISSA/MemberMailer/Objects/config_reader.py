import xml.etree.ElementTree as ET

_author__ = 'Sebastian'


class ConfigReader():

    config_location = '.\config\membermailer.xml'

    def __init__(self):
        try:
            self.config = ET.parse(self.config_location)
            self.root = self.config.getroot()

        except FileNotFoundError as error:
            print("FileNotFoundError: {0}".format(error))
            # not sure if should do sys.exit() here vs print

        except ET.ParseError as error:
            print("ParseError: {0}".format(error))

    # Only use this method if you want to override default file
    # otherwise, you can just call ConfigReader() and it
    # will automatically read default xml file path
    def read_config(self, file):
        self.config = ET.parse(file)
        self.root = self.config.getroot()

    #def create_config(self):
    #def write_config(self):
    
    def print_root(self):
        print(self.root.tag)

    def print_parent(self):
        for self.child in self.root:
                print(self.child.tag)

    def print_children(self):
        for self.child in self.root:
            for self.children in self.child:
                print("Key:", self.children.tag, "-> Value:", self.children.text)


# Testing config_reader class
# Still not sure how to write unit tests yet

# Instantiate ConfigReader class
test_reader = ConfigReader()

# pass in an xml file to override default
data_file = "E:\\Users\Sebastian\Desktop\sample_config2.xml"
test_reader.read_config(data_file)
print("---------------------------------")
print("Printing out root elements...")
print("---------------------------------")
test_reader.print_root()
print()
print("---------------------------------")
print("Printing out parent elements...")
print("---------------------------------")
test_reader.print_parent()
print()
print("---------------------------------")
print("Printing out children elements...")
print("---------------------------------")
test_reader.print_children()