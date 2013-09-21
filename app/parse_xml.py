from app import db, models
from xml.dom import minidom
from dateutil.parser import parse

xmldoc = minidom.parse('uppsala_brott_2010-2012.xml')
eventlist = xmldoc.getElementsByTagName('event') 

print len(eventlist)
print eventlist[0].getElementsByTagName('date')[0].childNodes[0].data

#print eventlist[0].attributes['date'].value
for event in eventlist:
    
    e = models.Crime(
        title = event.getElementsByTagName('title')[0].childNodes[0].data,
        description = event.getElementsByTagName('description')[0].childNodes[0].data,
        place = event.getElementsByTagName('place')[0].childNodes[0].data,
        date = parse(event.getElementsByTagName('date')[0].childNodes[0].data),
        longitude = event.getElementsByTagName('lng')[0].childNodes[0].data,
        latitude = event.getElementsByTagName('lat')[0].childNodes[0].data,
    )
    db.session.add(e)

db.session.commit()
