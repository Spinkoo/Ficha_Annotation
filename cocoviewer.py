#!C:\Users\Wail\AppData\Local\Programs\Python\Python39\python.exe

import argparse
import json
import matplotlib.pyplot as plt

from labelme import utils
import numpy as np
import cv2 
from glob import glob


def main():


    jsons = glob('../compressed/m/*.json')

    for json_file in jsons :

        data = json.load(open(json_file))
        img = utils.img_b64_to_array(data['imageData'])
        lbl, lbl_names = utils.labelme_shapes_to_label(img.shape, data['shapes'])
        lbl_viz = lbl * (255 / len(lbl_names))
        lbl_viz = np.array([lbl_viz])
        lbl_viz = lbl_viz.transpose()
        lbl_viz = np.concatenate([lbl_viz, lbl_viz, lbl_viz], axis = 2)


        if 'Dumpster' not in lbl_names:
            continue
        print(lbl_names)
        lbl_viz = utils.draw_label(lbl, img, lbl_names)

        cv2.imshow('',cv2.resize(lbl_viz,(512, 512)))
        if cv2.waitKey(10) == ord('q'):
            break


if __name__ == '__main__':
    main()
