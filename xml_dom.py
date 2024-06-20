import xml.dom.minidom

domtree = xml.dom.minidom.parse('employee.xml')
group = domtree.documentElement

people = group.getElementsByTagName('employee')

for employee in people:
    print(f"--Employee {employee.getAttribute('id')}--")
    name = employee.getElementsByTagName('firstname')[0].childNodes[0].nodeValue
    title = employee.getElementsByTagName('title')[0].childNodes[0].nodeValue
    division = employee.getElementsByTagName('division')[0].childNodes[0].nodeValue
    room = employee.getElementsByTagName('room')[0].childNodes[0].nodeValue

    print(f"Name: {name}")
    print(f"Title: {title}")
    print(f"Division: {division}")
    print(f"room: {room}")

people[0].getElementsByTagName('firstname')[0].childNodes[0].nodeValue = "Hans"
people[0].setAttribute("id","100")

domtree.writexml(open('employee.xml','w'))