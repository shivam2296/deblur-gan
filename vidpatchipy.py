from PIL import Image
import argparse


def patch():
    
    val = 512
    num = 1
    img = 'FRAMES/frame1.jpg'
    img = Image.open(img)
    width, height = img.size
    width =width+(val-1)
    height=height+(val-1)
    k=1
    for frame_num in range(1,num+1):
        img='FRAMES/frame'+str(frame_num)+'.jpg'
        img = Image.open(img)
        i=0
        
        while (i+val<=height):
            j=0
            while (j+val<=width):
                area=(j,i,j+val,i+val)
                img1=img.crop(area)
                path="PATCHES/Patch"+str(k)+".jpg"
                img1.save(path)
                k=k+1
                j=j+val
            i=i+val
        print('patched into '+str(k-1)+' parts')
    
if __name__ == "__main__":
    patch()
	
