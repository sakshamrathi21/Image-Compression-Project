import sys
import subprocess
import runlength, basic, actual_jpeg, runlength, comparison, pca, colour, paper
import sys
sys.path.append('..')
from algorithms.helper import *

if __name__ == "__main__":
    # print("check")
    if len(sys.argv) < 2:
        print("Usage: python3 run.py <file_names>")
    if len(sys.argv) == 2:
        file_number = sys.argv[1]
        if file_number == "basic":
            bpp_results, rmse_results = basic.basic()
            rmse_vs_bpp_plot(bpp_results, rmse_results, get_image_paths(), plot_path='../results/basic.png')
        elif file_number == "runlength":
            bpp_results, rmse_results = runlength.runlength()
            rmse_vs_bpp_plot(bpp_results, rmse_results, get_image_paths(), plot_path='../results/runlength.png')
        elif file_number == "jpeg":
            bpp_results, rmse_results = actual_jpeg.jpeg()
            rmse_vs_bpp_plot(bpp_results, rmse_results, get_image_paths(), plot_path='../results/jpeg.png')
        elif file_number == "pca":
            bpp_results, rmse_results = pca.pca()
            rmse_vs_bpp_plot(bpp_results, rmse_results, get_image_paths(), plot_path='../results/pca.png')
        elif file_number == "colour":
            bpp_results, rmse_results = colour.colour()
            rmse_vs_bpp_plot(bpp_results, rmse_results, get_image_paths(), plot_path='../results/colour.png')
        elif file_number == "paper":
            bpp_results, rmse_results = paper.basic()
            rmse_vs_bpp_plot(bpp_results, rmse_results, get_image_paths(cartoon=True), plot_path='../results/paper.png')
        elif file_number == "dpca":
            bpp_results, rmse_results = pca.dpca()
            rmse_vs_bpp_plot(bpp_results, rmse_results, get_image_paths(), plot_path='../results/dpca.png')
        elif file_number == "cpca":
            bpp_results, rmse_results = pca.cpca()
            rmse_vs_bpp_plot(bpp_results, rmse_results, get_image_paths(), plot_path='../results/cpca.png')
        else:
            print("Invalid file name")
    elif len(sys.argv) == 3:
        algo1 = sys.argv[1]
        algo2 = sys.argv[2]
        if algo1 == "basic" and algo2 == "runlength":
            bpp_results1, rmse_results1 = basic.basic(1)
            bpp_results2, rmse_results2 = runlength.runlength(1)
            comparison.comparison(bpp_results1, rmse_results1, bpp_results2, rmse_results2, algo1, algo2)
        elif algo1 == "basic" and algo2 == "jpeg":
            bpp_results1, rmse_results1 = basic.basic(1)
            bpp_results2, rmse_results2 = actual_jpeg.jpeg(1)
            comparison.comparison(bpp_results1, rmse_results1, bpp_results2, rmse_results2, algo1, algo2)
        elif algo1 == "runlength" and algo2 == "jpeg":
            bpp_results1, rmse_results1 = runlength.runlength(1)
            bpp_results2, rmse_results2 = actual_jpeg.jpeg(1)
            comparison.comparison(bpp_results1, rmse_results1, bpp_results2, rmse_results2, algo1, algo2)
        else:
            print("Invalid file names")
