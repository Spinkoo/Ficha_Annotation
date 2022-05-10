import json
import matplotlib.pyplot as plt

from labelme import utils
import numpy as np
import cv2 
from glob import glob


def main():


    jsons = glob('*.json')

    for json_file in jsons :

        data = json.load(open(json_file))
        img = utils.img_b64_to_arr(data['imageData'])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgpath = json_file.replace('json', 'png')
        cv2.imwrite('data/'+imgpath, img)


if __name__ == '__main__':
    main()
