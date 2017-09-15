import csv

filename = '2_1.csv'

data = []

try:
    with open( filename ) as f:
	reader = csv.reader(f)

    header = reader.next()

    data = [row for row in reader]

    except:	
	print "Error "
        
        sys.exit(-1)

    if header:
       print header
       print '=============='

    for datarow in data:
        print datarow