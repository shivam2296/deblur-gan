import cv2
import numpy as np
from PIL import Image

join():
	img = 'FRAMES/frame1.jpg'
	img = Image.open(img)
	x, y = img.size
	x=int(x)
	y=int(y)
	dim=512
	frames=1
	src='deblurPATCHES'
	ext='.jpg'
	dest='DEBLUR_FRAMES'

	x=x+dim-1
	y=y+dim-1
	k=1
	frame_num=1

	while(frame_num<=frames):
		im1 = cv2.imread(src+'/Patch'+str(k)+ext)
		k=k+1

		for i in range(2,int(x/dim)+1):
			im2 = cv2.imread(src+'/Patch'+str(k)+ext)
			im1	 = np.concatenate((im1, im2), axis=1) 
			k=k+1

		for j in range(2,int(y/dim)+1):
			im2=cv2.imread(src+'/Patch'+str(k)+ext)
			k=k+1
			for i in range(2,int(x/dim)+1):
				im3 = cv2.imread(src+'/Patch'+str(k)+ext)
				im2	 = np.concatenate((im2, im3), axis=1)
				k=k+1
			im1=np.concatenate((im1,im2),axis=0)

		cv2.imwrite(dest+'/frame'+str(frame_num)+'.png',im1)
		frame_num=frame_num+1

	print('Deblurred image saved in DEBLUR_FRAMES')

if __name__ == "__main__":
	join()
