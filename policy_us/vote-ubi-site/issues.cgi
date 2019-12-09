#!/usr/bin/python
import json
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
dist_key = form.getvalue('dist_key')
#dist_key = str("CA-12")
#dist_key = str("FL")
jsonOut = form.getvalue('json')
#jsonOut = True

#######################
# json format
#######################
#  "AK-AL": {
#    "Twitter": "@AlyseGalvin",
#    "Candidate": "Alyse Galvin",
#    "Hack": "Don Young",
#    "Hack's Party": "R",
#    "15MIN": "",
#    "M4A": "",
#    "GND": "",
#    "C4A": "",
#    "Corp": "",
#    "UBI": -1,
#    "Progressive Score": -1
#  },
###############################

def myOut(list):
  if jsonOut == 'True':
    print ("Content-Type: application/javascript\n\n")
    print(str(list))
  else:
    print("<p><table><tr><td width='150px'><b>" + list['DIST'] + "</td><td></td><tr>")
    print("<tr><td width='260px'>Candidate</td><td>" + str(list["Candidate"]) + " (" + list["Hack's Party"] + ")</td></tr>")
    print("<tr><td width='260px'>Twitter Username</td><td><a href='https://twitter.com/" + str(list["Twitter"]) + "' target='_blank'>" + str(list["Twitter"]) + "</a></td></tr>")

    val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/question-mark.png?raw=true' alt='N/A'>"
    if str(list["UBI"]) == "1":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/green-check.png?raw=true' alt='Yes'>"
    elif str(list["UBI"]) == "0":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/red-x.png?raw=true' alt='No'>"
    print("<tr><td width='260px'>UBI Caucus Member</td><td>" + str(val) + "</td></tr>")
          
    val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/question-mark.png?raw=true' alt='N/A'>"
    if str(list["15MIN"]) == "1":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/green-check.png?raw=true' alt='Yes'>"
    elif str(list["15MIN"]) == "0":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/red-x.png?raw=true' alt='No'>"
    print("<tr><td width='260px'>$15 Minimum Wage (or better)</td><td>" + str(val) + "</td></tr>") 

    val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/question-mark.png?raw=true' alt='N/A'>"
    if str(list["M4A"]) == "1":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/green-check.png?raw=true' alt='Yes'>"      
    elif str(list["M4A"]) == "0":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/red-x.png?raw=true' alt='No'>"
    print("<tr><td width='260px'>Medicare for All</td><td>" + str(val) + "</td></tr>") 
    
    val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/question-mark.png?raw=true' alt='N/A'>"
    if str(list["GND"]) == "1":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/green-check.png?raw=true' alt='Yes'>"
    elif str(list["GND"]) == "0":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/red-x.png?raw=true' alt='No'>"
    print("<tr><td width='260px'>Green New Deal</td><td>" + str(val) + "</td></tr>")

    val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/question-mark.png?raw=true' alt='N/A'>"
    if str(list["C4A"]) == "1":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/green-check.png?raw=true' alt='Yes'>"
    elif str(list["C4A"]) == "0":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/red-x.png?raw=true' alt='No'>"
    print("<tr><td width='260px'>Public College for All</td><td>" + str(val) + "</td></tr>")

    val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/question-mark.png?raw=true' alt='N/A'>"
    if str(list["No Corp"]) == "1":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/green-check.png?raw=true' alt='Yes'>"
    elif str(list["No Corp"]) == "0":
      val = "<img src='https://github.com/joezippy/OpenUBI/blob/master/project-images/red-x.png?raw=true' alt='No'>"
    print("<tr><td width='260px'>No Corporate PAC Money</td><td>" + str(val) + "</td></tr></table>")
    # print("Progressive Score                : " + str(list["Progressive Score"])) + "<p>"


def findall(v, k):
  for i in range(len(v)):
    if (k == "President"):
      myOut(v[i])
    elif (len(v[i]['DIST']) >= 2 and len(k) >=2):
      if v[i]['DIST'][:2] == k[:2]:
        myOut(v[i])
    else:
      if v[i]['DIST'] == k:
        myOut(v[i])

filename = './president.json'
pdata = json.load(open(filename))
filename = './senate.json'
sdata = json.load(open(filename))
filename = './house.json'
cdata = json.load(open(filename))

print ("Content-Type: text/html\n\n<html><head>")
print ("<meta http-equiv='content-type' content='text/html; charset=UTF-8'>")
print ("<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'>")
print ("<meta http-equiv='Pragma' content='no-cache'>")
print ("<meta http-equiv='Expires' content='0'>")
print ("<link rel='stylesheet' href='style.css'>")
print ("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print ("</head><body bgcolor='white'>")
print("<h2>President</h2>")
results = findall(pdata,"President")
print("<h2>Senate</h2>")
results = findall(sdata,dist_key)
print("<h2>House</h2>")
results = findall(cdata,dist_key)
print("</body></html>")




