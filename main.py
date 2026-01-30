# -*- coding: utf-8 -*-
# @Author: llap4585
# @Project: RapidOcr-Paragraphizer
# @License: Apache-2.0
# @GitHub: https://github.com/llap4585/RapidOcr-Paragraphizer

import os
import cv2   
import numpy as np  
from rapidocr import RapidOCR  

def detect_indented_paragraphs(boxes, indent_threshold=50, line_gap_threshold=10):
    if isinstance(boxes, list):
        boxes = np.array(boxes)

    N = boxes.shape[0]
    if N == 0:
        return []


    x_mins = boxes[:, :, 0].min(axis=1)
    y_mins = boxes[:, :, 1].min(axis=1)
    base_x = np.min(x_mins)
    indented_paragraphs = []

    if x_mins[0] - base_x > indent_threshold:
        indented_paragraphs.append(0)


    for i in range(1, N):
        dy = y_mins[i] - y_mins[i-1]
        is_indented = (x_mins[i] - base_x > indent_threshold)
        prev_is_indented = (x_mins[i-1] - base_x > indent_threshold)
        
        if is_indented:
            if dy > line_gap_threshold or not prev_is_indented:
                indented_paragraphs.append(i)

    return indented_paragraphs


def preprocess_for_rapidocr(img_path, save_path=None):
    img = img_path

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    denoised = cv2.GaussianBlur(gray, (3, 3), 0)

    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(16, 16))
    enhanced = clahe.apply(denoised)
    return enhanced


def merge(indented_paragraphs, txts):
    
    if indented_paragraphs == []:
        return ''.join(txts)
        
    txts = list(txts)
    for i in indented_paragraphs:
        # Can be adjusted based on different document formats
        # txts[i]= '\n' + str(txts[i]) +'\n'
        txts[i] = '\n' + str(txts[i]) 
        result = ''.join(txts)
    
    return result

def process_single_page(page_path, output_dir):
    output_path = os.path.join(output_dir, f"{os.path.splitext(page_path)[0]}.txt")
    
    try:
        engine = RapidOCR()
        pages = cv2.imread(page_path)

        enhanced_pic = preprocess_for_rapidocr(pages)
        
        read_pages = engine(enhanced_pic, use_det=True, use_cls=False, use_rec=True)

        if read_pages.txts:
            paragraphs = merge(detect_indented_paragraphs(read_pages.boxes), read_pages.txts)

            # Real-time append for each page
            with open(output_path, "a", encoding="utf-8") as f:
                f.write(paragraphs + '\n')
                     
        f.close()
            
    except:
        print(f"Failed: {page_path} ")

if __name__ == "__main__":
    PAGE_PATH = '.png'    # Path to your input image
    TXT_OUTPUT_DIR = '.'  # Output directory for results


    if not os.path.exists(TXT_OUTPUT_DIR):
        os.makedirs(TXT_OUTPUT_DIR)

    process_single_page(PAGE_PATH, TXT_OUTPUT_DIR)

    print("Finished")