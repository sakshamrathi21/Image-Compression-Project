import sys
sys.path.append('..')
from include.common_imports import *
from algorithms.helper import *
from algorithms.advanced_helper import *

def basic(num_paths=5):
    config = Config()
    # num_paths = 1
    image_paths = get_image_paths(cartoon=True)[0:num_paths]
    # image_paths = ["../extras/DIP_project/data/im2.png"]
    # os.system("ls ../extras/data/im2.png")
    # window_sizes = [11]
    window_sizes = [3, 5, 7, 9, 11]
    # window_sizes = [7]
    
    bpp_r = []
    rmse_r = []
    i = 0
    for image_path in image_paths:
        bpp_results = []
        rmse_results = []
        for window_size in window_sizes:
            print("Window Size: ", window_size)
            size_in_bits = encode(image_path, window_size)
            rmse = decode(image_path, f"../results/try_{window_size}_{i}.png")
            print("Size in bits: ", size_in_bits)
            print("RMSE: ", rmse)
            bpp_results.append(size_in_bits)
            rmse_results.append(rmse)
        i += 1
        bpp_r.append(bpp_results)
        rmse_r.append(rmse_results)
    # print(bpp_r, rmse_r)
    return bpp_r, rmse_r

