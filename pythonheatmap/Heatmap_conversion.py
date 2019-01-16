
import os
import cv2
import matplotlib.pyplot as plt

PATH = './PNG_images/'

files = os.listdir(PATH)
for file in files:
    print file
    img = cv2.imread(os.path.join(PATH, file), 0)
    # print img.shape

    fig, ax = plt.subplots()
    # im = ax.imshow(img, cmap=plt.cm.hot, interpolation='none')
    im = ax.imshow(img, cmap=plt.cm.jet, interpolation='none')
    cbar = fig.colorbar(im, extend='max')
    # cbar.cmap.set_over('green')
    # plt.show()
    # plt.save('img1.png')
    save_file = '%s_heatmap.png' % file[:-4]
    print save_file
    plt.savefig(os.path.join(PATH, save_file))
