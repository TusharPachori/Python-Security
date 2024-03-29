import zipfile
import optparse
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print ('[+] Found password ' + password + '\n')
    except: pass

def main():
    # Adding command line argments
    parser = optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
    # File to be cracked
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    # Dictionary for list of passwords
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    # Exit if file or dictionary not provided
    if (options.zname == None) | (options.dname == None):       # 
        print (parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        # New Thread for each password for concurrent cracking
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()
