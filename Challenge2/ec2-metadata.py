## This code is for getting the EC2 Metadata, fetching the Metadata from DHCP Server

import urllib.request

metadata_json = urllib.request.urlopen('http://169.254.169.254/latest/dynamic/instance-identity/document').read().decode()

## For Printing EC2 Metadata in JSON Format

print ("Metadata in JSON Format==> \n"+metadata_json)

print ("--------------------------- To Retrieve data key individually please select the metadata index --------------------------------")


metadata = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/').read().decode()

metalist = metadata.split('\n')

### Printing MetaList which is Metadata in a list and asking options to the Users so that he can get the particular key value.

count =1

for key in metalist:
    print ('index=> {0}, key=> {1}'.format(count,key))
    count += 1

## Index No. will give the Metadata value, for exiting either press 0 or any negative value i.e. -1 

index = int(input ('Enter the metadata index:'))
while index>0:
    if (index > 25):
        print ('Invalid Index, for exit please press 0 or any negative value i.e. -1')
    else:
        result = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/'+metalist[index-1]).read().decode()
        print (result)
    index = int (input ('Enter the metadata index:'))

print ("Exiting the Program Byee!!")
