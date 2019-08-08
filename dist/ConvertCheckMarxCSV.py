#!/usr/bin/python
import csv , json
import sys

if ( len(sys.argv) > 2 ):
    
  csvFilePath = sys.argv[1]
  jsonFilePath = sys.argv[2]

  arr = []

  with open (csvFilePath) as csvFile:
    csvReader = csv.reader(csvFile)
    print(csvReader)
    i = 0
    print("[")
    for csvRow in csvReader:
        arr.append(csvRow)
        print("{ id :" + str(i) + ", \"issue\": \"" + str(csvRow[0])  + "\" } ")
        i = i + 1
        print('-------------------------------------------------------------')
#    jsondata = json.dumps(arr)


   # with open(jsonFilePath, "w") as jsonFile:
      #jsonFile.write(json.dumps(arr, indent = 4))
#      {
  #"engineVersion" : "1.0-SNAPSHOT",
  #"scanDate" : "2017-04-18T23:31:42.136Z",
  #"buildServer" : "server01",
  #"findings" : [ {
    #"uniqueId" : "fda2eaa2-7643-4fc5-809e-3eb6957e1945",
    #"category" : "Cross-site Scripting",
    #"fileName" : "file-fda2eaa2-7643-4fc5-809e-3eb6957e1945/00000001.bin",
    #"vulnerabilityAbstract" : "Cross-site Scripting found in file-fda2eaa2-7643-4fc5-809e-3eb6957e1945/00000001.bin",
    #"lineNumber" : 103,
    #"confidence" : 4.968653,
    #"impact" : 200.69,
    #"priority" : "Critical",
    #"categoryId" : "a101",
    #"customStatus" : "OPEN",
    #"artifact" : "artifact-fda2eaa2-7643-4fc5-809e-3eb6957e1945/00000001.jar",
    #"description" : "Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy. Cross-site scripting carried out on websites accounted for roughly 84% of all security vulnerabilities documented by Symantec as of 2007.[1] Their effect may range from a petty nuisance to a significant security risk, depending on the sensitivity of the data handled by the vulnerable site and the nature of any security mitigation implemented by the site's owner.",
    #"comment" : "This should be fixed",
    #"buildNumber" : "300.3837014436722",
    #"lastChangeDate" : "2017-04-16T21:31:42.092Z",
    #"artifactBuildDate" : "2017-04-17T22:31:42.092Z",
    #"textBase64" : "RXhhbXBsZSBvZiBhIHRleHQgZW5jb2RlZCBpbiB0aGUgb3JpZ2luYWwgc2NhbiB0byBCYXNlNjQuIApGcm9tIFdpa2lwZWRpYTogCgpDb21wdXRlciBzZWN1cml0eSwgYWxzbyBrbm93biBhcyBjeWJlciBzZWN1cml0eSBvciBJVCBzZWN1cml0eSwgaXMgdGhlIHByb3RlY3Rpb24gb2YgY29tcHV0ZXIgc3lzdGVtcyBmcm9tIHRoZSB0aGVmdCBvciBkYW1hZ2UgdG8gdGhlaXIgaGFyZHdhcmUsIHNvZnR3YXJlIG9yIGluZm9ybWF0aW9uLCBhcyB3ZWxsIGFzIGZyb20gZGlzcnVwdGlvbiBvciBtaXNkaXJlY3Rpb24gb2YgdGhlIHNlcnZpY2VzIHRoZXkgcHJvdmlkZS4gCgpDeWJlciBzZWN1cml0eSBpbmNsdWRlcyBjb250cm9sbGluZyBwaHlzaWNhbCBhY2Nlc3MgdG8gdGhlIGhhcmR3YXJlLCBhcyB3ZWxsIGFzIHByb3RlY3RpbmcgYWdhaW5zdCBoYXJtIHRoYXQgbWF5IGNvbWUgdmlhIG5ldHdvcmsgYWNjZXNzLCBkYXRhIGFuZCBjb2RlIGluamVjdGlvbi4gQWxzbywgZHVlIHRvIG1hbHByYWN0aWNlIGJ5IG9wZXJhdG9ycywgd2hldGhlciBpbnRlbnRpb25hbCwgYWNjaWRlbnRhbCwgSVQgc2VjdXJpdHkgaXMgc3VzY2VwdGlibGUgdG8gYmVpbmcgdHJpY2tlZCBpbnRvIGRldmlhdGluZyBmcm9tIHNlY3VyZSBwcm9jZWR1cmVzIHRocm91Z2ggdmFyaW91cyBtZXRob2RzLgo="
  #}
else:
    print('usage: ConvertCheckMarxCSV.py')
