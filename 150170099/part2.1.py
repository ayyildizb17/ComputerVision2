#BUSE AYYILDIZ 150170099

import pickle
import matplotlib.pyplot as plt
import torch
import cv2
import numpy as np

#2.1
with open('stylegan3-t-ffhq-1024x1024.pkl', 'rb') as f:
    a = pickle.load(f)

gan = a["G_ema"]
gan.eval()

for param in gan.parameters():
    param.requires_grad = False

z = torch.randn(1,512)
t = torch.randn(1,512)

img = gan(z,0).numpy().squeeze()
img = np.transpose(img,(1,2,0))

img2 = gan(t,0).numpy().squeeze()
img2 = np.transpose(img2,(1,2,0))

img[img>1] = 1
img[img<-1] = -1

img2[img2>1] = 1
img2[img2<-1] = -1

img = 255*(img+1)/2
img2 = 255*(img2+1)/2


cv2.imwrite('test1.png', img[:,:,[2,1,0]])
cv2.imwrite('test2.png', img2[:,:,[2,1,0]])



