# Input String:
# inputobj =  {"a":{"b":{"c":"d"}}}
inputobj = {"x":{"y":{"z":"a"}}}

# list for appending the key values in the Keylist variable
keylist = []

## Function which call the dictionary and iterate it and get the keys and value from the nested dictionary

def getkeyvalue(nestedobj,keylist):
    # Getting first key in dictionary
    nkey = list(nestedobj.keys())[0]
    value = list (nestedobj.values())[0] ## Getting the value in dictionary
    keylist.append(nkey) ## appending all the keys in keylist from the nested dictionary
    ## Checking with if condition iterate till the last nested dictionary
    if (type(value) is dict):
        ## iterating the nested dictionary object for getting the last value and for making list of keys
        getkeyvalue(value,keylist)
    ## Iterating last dictionary and printing key with '/' and printing Value
    else:
        reskey = ''
        for item in keylist:
            if item == keylist[-1]:
                reskey += item
            else:
                reskey += item + '/'
        print ("Key -> {}, Value -> {}".format(reskey,value))


getkeyvalue(inputobj,keylist)