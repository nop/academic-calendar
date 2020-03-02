import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://www.lonestar.edu/academic-calendar'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

year = soup.select("body > section.content-well-section.section-light > div > div:nth-child(2) > div.col-lg-9.col-md-8 > div > h2:nth-child(1)")
events = soup.select("table > tbody > tr > td")
elist = list()
for i in range(0, len(events), 2):
	name = events[i].get_text()
	date = events[i+1].get_text()
	elist.append((name,date))

file = open("out.ics", "w")
file.write(
"""BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:LSC Academic Calendar
X-WR-TIMEZONE:America/Chicago
X-WR-CALDESC:http://www.lonestar.edu/academic-calendar\n"""
)

# BEGIN:VEVENT
# DTSTART;VALUE=DATE:20200309
# DTEND;VALUE=DATE:20200316
# DTSTAMP:20200302T200334Z
# UID:044q9e1omvsv9b7e74ffvgagcq@google.com
# CREATED:20200302T195351Z
# DESCRIPTION:
# LAST-MODIFIED:20200302T200232Z
# LOCATION:
# SEQUENCE:0
# STATUS:CONFIRMED
# SUMMARY:Spring Break (Offices Closed)
# TRANSP:TRANSPARENT
# END:VEVENT
for e in elist:
	file.write("BEGIN:VEVENT\n")
	file.write(e[0] + "\n")
	file.write("END:VEVENT\n")

file.write("END:VCALENDAR")