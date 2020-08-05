import os
import requests

logfile = os.path.join(os.getcwd(), 'logfile.txt')
with open('baseurl.txt', 'r') as file:
    baseurl = file.read().replace('\n', '').strip()

year = 2011
month = 1

outputdir = os.path.join(os.getcwd(), 'output')
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

while (year < 2021 or (year == 2020 and month < 8)):
    if month < 10:
        url = ('%s-%s-0%s.xml' % (baseurl, year, month))
    else:
        url = ('%s-%s-%s.xml' % (baseurl, year, month))
    with open(logfile, 'a') as file:
        file.write('Fetching: ' + url + '\n')
    print('Fetching: %s' % url)
    response = requests.get(url)

    if response.status_code == 200:
        with open(logfile, 'a') as file:
            file.write('Request successful\n')
        print('Request successful')
        if month < 10:
            filename = os.path.join(outputdir, ('xbrlrss-%s-0%s.xml' % (year, month)))
        else:
            filename = os.path.join(outputdir, ('xbrlrss-%s-%s.xml' % (year, month)))
        with open(filename, 'wb') as file:
            print('Writing file %s' % filename)
            file.write(response.content)
        year = year+1 if month == 12 else year 
        month = 1 if month == 12 else month+1
        if year == 2020 and month == 8:
            break
    else:
        with open(logfile, 'a') as file:
            file.write('Request failed for file ' + url + ' with status code ' + response.status_code + '\n')
        print('Request failed for file ' + url + ' with status code ' + response.status_code + '\n')       