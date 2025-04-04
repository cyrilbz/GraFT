#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 08:57:59 2023

@author: pgf840
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import skimage.io as io

from graft.main import create_all, create_all_still
from graft.utilsF import get_tiff_path
from graft import utilsF

# Get the directory containing this script.
base_path = os.path.dirname(os.path.abspath(__file__))

plt.close('all')

SIGMA = 1.0  # tubeness filter width
SMALL = 50.0  # cluster removal  


if __name__ == '__main__':
    ###############################################################################
    #
    # load in and run functions
    #
    ###############################################################################

    ######################
    # timeseries

    # img_o = io.imread(get_tiff_path("timeseries.tif"))
    # maskDraw = np.ones((img_o.shape[1:3]))
    # create_all(pathsave=os.path.join(base_path, "timeseries"),
    #            img_o=img_o,
    #            maskDraw=maskDraw,
    #            size=6,eps=200,thresh_top=0.5,sigma=SIGMA,small=SMALL,angleA=140,overlap=4,max_cost=100,
    #            name_cell='in silico time')

    ######################
    # one image
    img_still = io.imread("kinza_bending/actin_original.tif")
    # img = io.imread(get_tiff_path("timeseries.tif"))
    # img_still = img_o[0]
    # maskDraw = np.ones((img.shape[1:3]))
    maskDraw = io.imread("kinza_bending/mask.tif")/255
    binmask = maskDraw>0 # create binary mask
    masked_im = img_still*binmask
    outputdir = "kinza_bending/output/"   
    
    create_all_still(pathsave=outputdir,
                img_o=masked_im,
                maskDraw=maskDraw,
                size=6,eps=200,thresh_top=0.75,sigma=SIGMA,small=SMALL,angleA=140,overlap=4,
                name_cell='in silico still')
