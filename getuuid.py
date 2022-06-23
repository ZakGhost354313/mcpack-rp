#!/usr/bin/env python3
import httplib2
def main(): print(httplib2.Http().request(uri="https://www.uuidtools.com/api/generate/v4/count/"+str(input('how many?(#)  ')),method='GET'))
if __name__ == "__main__": main()