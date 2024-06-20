import xml.sax
from xml.sax.xmlreader import AttributesImpl

class PeopleHandler(xml.sax.ContentHandler):
    
    def startElement(self, name, attrs):
        self.current = name
        print("Print",name,"Print")
        if name == "employee":
            print(f"-- Employee {attrs['id']} --")

    def characters(self, content):
        if self.current == "firstname":
            self.firstname = content
        elif self.current == "title":
            self.title = content
        elif self.current == "division":
            self.division = content
        elif self.current == "room":
            self.room = content

    def endElement(self, name):
        if self.current == "firstname":
            print(f"Name: {self.firstname}")
        elif self.current == "title":
            print(f"Title: {self.title}")
        elif self.current == "division":
            print(f"Division: {self.division}")
        elif self.current == "room":
            print(f"Room: {self.room}")
        self.current = ""


handler = PeopleHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('employee.xml')