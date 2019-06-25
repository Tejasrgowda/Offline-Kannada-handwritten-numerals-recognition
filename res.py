import cv2
import glob
lst=glob.glob('*.[jJ][pP][gG]')
for a in lst:
	result=cv2.imread(a,2)
	res=cv2.resize(result,(100,100))
	cv2.imwrite(a,res)
