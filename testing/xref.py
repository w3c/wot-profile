from configparser import DuplicateOptionError

mypath="inputs/results"

from os import listdir
from os.path import isfile, join
import csv


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

contributorList=[]
assertionDict={}
assertionList = []
allAssertions={}
descriptions={}

for file in onlyfiles:
    if file.endswith(".csv"):
        print ("Processing: " + file)
        contrib = file.split(".")[0]
        contributorList.append(contrib)
        with open(join(mypath,file), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            assertionDict[contrib]={}
            for row in reader:
                assertionId=row['ID']
                if (row.get('Assertion')):
                    descriptions[assertionId]=row['Assertion']
                if (row.get('Description')):
                    descriptions[assertionId]=row['Assertion']
                status=row['Status']
                assertionDict[contrib][assertionId]=status
                # add the assertion to the list of all assertions, allocate if necessary
                if (not assertionId in allAssertions):
                    assertionList.append(assertionId)
                    allAssertions[assertionId] = 0
                if (status=="pass"):
                    allAssertions[assertionId] = allAssertions[assertionId]+1

# write csv 

index = 0
with open('assertion-totals.csv', 'w', newline='') as csvfile:
    fieldnames = ['Index', 'ID','Total'] + contributorList + ['Description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for assertionId in assertionList:
        row = {}
        row["Index"]=index
        index=index+1
        row["ID"]=assertionId
        row["Description"]=descriptions[assertionId]
        row["Total"]=allAssertions[assertionId]
        for contrib in contributorList:
            if (assertionDict[contrib].get(assertionId)):
                row[contrib] = assertionDict[contrib][assertionId]
            else:
               row[contrib] = "XXXX"


        print (row)
        writer.writerow(row)
 