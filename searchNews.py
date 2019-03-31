import argparse


def searchFile(searchType,searchList):
    
    param =""
    finallist=[]
    counter = 0
    
    if searchType == "OR":
        
        prameter = searchList.split(",")
        
        with open("hscic-news.txt", "r") as newsfile:
            ncontent = newsfile.readlines()
            
            for x in range(len(ncontent)):
                for y in prameter:
                    if y in ncontent[x]:
                        
                        finallist.append(x)
    #    print (list(set(finallist)))
        finallist = list(set(finallist))
        finallist.sort()
        result = " ".join(str(x) for x in finallist)
        
        return result


    elif searchType == "AND" :
        prameter = searchList.split(",")
        with open("hscic-news.txt", "r") as newsfile:
            ncontent = newsfile.readlines()
            for x in range(len(ncontent)):
                for y in prameter:
                    if y in ncontent[x]:
                        counter += 1
                    else:
                        counter = 0
                    if counter == len(prameter) :finallist.append(x)

    #    print (list(set(finallist)))
        finallist = list(set(finallist))
        finallist.sort()
        result = " ".join(str(x) for x in finallist)
        #print(result)
        return result


    else:
        print ("Please enter only or/and for search type ")
        exit(1)

if __name__== '__main__':

    parser = argparse.ArgumentParser(description='Search your keyword example: searchNews.py AND A,B,C')
    parser.add_argument('searchtype', type=str, help='Search type OR and AND only ')
    parser.add_argument('Value', type=str, help='Parameter to search')
    args = parser.parse_args()
    searchFile(args.searchtype,args.Value)
    #print(searchFile(args.searchtype,args.Value))

