import sys
import os
import base64


#tested on python 2.7 should also work in python 3.x
#drop in same folder as base64 images.txt files
#decodes base 64 string and resaves as jpeg with same file name as b64
#useful for decoding bulk base64 provided by the client

if(__name__ == '__main__'):
    for filename in os.listdir(os.curdir):	
		#print(filename)
		b64file = open(filename, 'rb').read()
		imgData = base64.b64decode(b64file)
		file_name = os.path.splitext(filename)
		fname = file_name[0]
		fext = '.jpg'
		imgFile = open(fname + fext, 'wb')
		imgFile.write(imgData)
		print('done')
    else:
        print('No file specified!')
