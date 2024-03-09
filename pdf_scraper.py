import pdfplumber
import pandas as pd
import re
import matplotlib.pyplot as plt


### LG Spechsheet

path = "~\Documents\ModuleSpecSheets\LG\LG-NeON-R-360-375-specsheet.pdf"

# Variables to scrape: VOC, ISC, cell type
patterns = [r"voc.*?\d+\.*\d*", r"isc.*?\d+\.*\d*"]


with pdfplumber.open(path) as pdf:
    i = 0
    for page in pdf.pages:

        im = page.to_image(resolution=300)

        table_settings = {
            "vertical_strategy": "text",
            "horizontal_strategy": "lines_strict",
            "min_words_vertical": 3,
        }

        im.debug_tablefinder(table_settings)

        im.save("~\Documents\\" + str(i) + ".png", format="PNG")

        i += 1


print("done")
