# Copyright (c) 2020 Krailerk M.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## Import RegEx Module
import re

## Open the configuration file
f = open("doc/hello.txt")
## Print Accessible to the configuration file
print("Accessible to the configuration file")
## Save number of point header config file
datatmp = f.readlines()
## Close the configuration file
f.close()
## Print Closed to the configuration file
print("Closed to the configuration file")

## Function for procressing data line by line
def dataprocessing(linedata = str()):
    outdata = list()
    typedata = int()
    ## Get Table Of Contents
    if re.findall(r"[tT]able [oO]f [cC]ontents" , linedata) != [] : 
        print("Type 1")
        typedata = 1
        outdata = re.findall(r"[tT]able [oO]f [cC]ontents" , linedata)
    ## Get Vulnerabilities By Plugin
    elif re.findall(r"[vV]ulnerabilities [bB]y [pP]lugin" , linedata) != [] : 
        print("Type 2")
        typedata = 2
        outdata = re.findall(r"[vV]ulnerabilities [bB]y [pP]lugin" , linedata)
    ## Get Remediations
    elif re.findall(r"[rR]emediations" , linedata) != [] :
        print("Type 3")
        typedata = 3
        outdata = re.findall(r"[rR]emediations" , linedata)
    ## Get title cases
    elif re.findall(r"[0-9]+ \([0-9]+\) - .*" , linedata) != [] :
        print("Type 4")
        typedata = 4
        outdata = re.findall(r"[0-9]+ \([0-9]+\) - .*" , linedata)
    ## Get NetID address
    elif re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}", linedata) != [] :
        print("Type 5")
        typedata = 5
        outdata = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}", linedata)
    ## Get IP address
    elif re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} \(.*\)", linedata) != [] :
        print("Type 6")
        typedata = 6
        outdata = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} \(.*\)", linedata)
    ## Get Host
    elif re.findall(r"^ *[hH]ost", linedata) != [] :
        print("Type 7")
        typedata = 7
        outdata = re.findall(r"[hH]ost", linedata)
    ## Get Risk Factor
    elif re.findall(r"^ *[rR]isk [fF]actor", linedata) != [] :
        print("Type 8")
        typedata = 8
        outdata = re.findall(r"[rR]isk [fF]actor", linedata)
    ## Get Page
    elif re.findall(r"[pP]age [0-9]\*+.", linedata) != [] :
        print("Type 9")
        typedata = 9
        outdata = re.findall(r"[pP]age [0-9]", linedata)
    ## Get Risk Critical
    elif re.findall(r"^ *[cC]ritical", linedata) != [] :
        print("Type 10")
        typedata = 10
        outdata = re.findall(r"[cC]ritical", linedata)
    elif re.findall(r"^ *[hH]igh", linedata) != [] :
        print("Type 11")
        typedata = 11
        outdata = re.findall(r"[hH]igh", linedata)
    elif re.findall(r"^ *[mM]edium", linedata) != [] :
        print("Type 12")
        typedata = 12
        outdata = re.findall(r"[mM]edium", linedata)
    elif re.findall(r"^ *[lL]ow", linedata) != [] :
        print("Type 13")
        typedata = 13
        outdata = re.findall(r"[lL]ow", linedata)
    ## Other data
    else:
        print("Type 0")
        typedata = 0
        ## Add data to outdata and cut space 2 poits
        outdata.append(linedata[2:])
    return typedata, outdata 

def listToString(listInPut = list()) :
    outData = str()
    for ptmp in listInPut :
        outData += ptmp 
    return outData

## CheckFunction

## Main function for store convert to list for fill in excel
def storeAllDataToList(datatype = int(), dataout = str()):
    allDataList = list()
    ## Value for check collect Vulnerabilities By Plugin parameter or not
    vulnerabilitiesSwitch = False
    ## Value for check Risk Factor or not
    riskFactorSwitch = False
    ## Value for check Hosts or not
    hostsSwitch = False
    ## List of Vulnerabilities By Plugin
    vulnerabilitiesCase = list()
    ## List of Risk Factor
    riskFactorCase = list()
    ## List of Host
    hostCase = list()
    ## Save list of Vulnerabilities By Plugin parameter 2 & 4 toghter
    if datatype == 2:
        if vulnerabilitiesSwitch == False:
            vulnerabilitiesSwitch = True
        else:
            vulnerabilitiesSwitch = False
    elif datatype == 4:
        if vulnerabilitiesSwitch == True:
            vulnerabilitiesCase.append(dataout)
        else:
            ## Set all value to default
            riskFactorSwitch = False
            hostsSwitch = False
    ## Get Risk Factor
    elif datatype == 8:
        if riskFactorSwitch == False:
            riskFactorSwitch = True
        else:
            pass
    ## Get Host
    elif datatype == 7:
        if hostsSwitch == False:
            hostsSwitch = True
        else:
            pass
    ## Collect Host
    elif datatype == 6:
        if hostsSwitch == True:
            hostCase.append(dataout)
    elif datatype >= 10 and datatype <= 13:
        if riskFactorSwitch == True:
            riskFactorCase.append(dataout)
        else:
            pass
    else:
        pass
    return allDataList

## Parameter for count line of all for show
countline = 0

## Loop for check all data
for linedata in datatmp:
    ## Count lines
    countline +=  1
    ## Print count lines
    print(countline)
    ## Save return out
    outputall = dataprocessing(linedata)
    ## Get type return
    outputdatatype = outputall[0]
    ## Get data return
    outputdata = outputall[1]

    print(storeAllDataToList(outputdatatype, outputdata))