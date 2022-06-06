
## Potential Tools:

#### 1. [PDF Plumber](https://github.com/jsvine/pdfplumber)

- Useful methods:
    - extract_text() extracts the the raw string from a page
    - extract_tables() extracts tables from a page
    - debug_tablefinder() provides a visual representation of the table finding algorithm by converting the page to an image and overlaying its determinations.

    ![]("https://cee-gitlab.sandia.gov/2022_summer_interns/spec_sheet_scraper/-/blob/main/Images/visual_table_debugger_example.png")

    - crop() returns a cropped version of the page with inputs being rectangle coordinates in range [0,1]
    - The table-related methods take the table_settings keyword argument to define custom table parameters. Here are the defaults:

    ```python
    {
        "vertical_strategy": "lines", 
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [],
        "explicit_horizontal_lines": [],
        "snap_tolerance": 3,
        "snap_x_tolerance": 3,
        "snap_y_tolerance": 3,
        "join_tolerance": 3,
        "join_x_tolerance": 3,
        "join_y_tolerance": 3,
        "edge_min_length": 3,
        "min_words_vertical": 3,
        "min_words_horizontal": 1,
        "keep_blank_chars": False,
        "text_tolerance": 3,
        "text_x_tolerance": 3,
        "text_y_tolerance": 3,
        "intersection_tolerance": 3,
        "intersection_x_tolerance": 3,
        "intersection_y_tolerance": 3,
    }
    ```
The strategy settings have a few values:

![abc]("https://cee-gitlab.sandia.gov/2022_summer_interns/spec_sheet_scraper/-/blob/main/Images/strategy_settings_pdfplumber.png")

- This library is built on [pdfminer.six](https://github.com/pdfminer/pdfminer.six), a lower level PDF library. Might be worth exploring itself
- Cons:
  - image methods require 2 packages that need special installs
  - cannot extract tables from our spec sheets in any redeemable manner without targeting th
