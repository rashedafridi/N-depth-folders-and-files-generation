import os
parent_dir = ".\\" # directory where folder will be created
def  makeDiractory(path ,directory): # create folder in specified path with diredotory name
    directoryPath = os.path.join(path, directory)
    os.mkdir(directoryPath)
def  makeFile(path): # create test file  in specified path and write path as the content. 
    f= open(os.path.join(path ,"file.txt"),"w+")
    f.write(os.path.join(path ,"file.txt"))
    f.close()
def createFoldersAndFile(endDepth , startDepth = 0 , path = parent_dir): # recursion to create nested folder and file
    if startDepth > endDepth:
        #print("done")
        return
    else:
       for directoryName in range(0,startDepth+1):
           makeDiractory(path, str(directoryName))
           makeFile(os.path.join(path,str(directoryName)))
           createFoldersAndFile(endDepth , startDepth+1, os.path.join(path,str(directoryName))) 

def main():
    # take depth input from user
    depth = int(input ("Enter depth laval :"))
    #print(depth)
    createFoldersAndFile(depth)
if __name__ == "__main__":
    main()