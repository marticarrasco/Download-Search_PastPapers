# IB Past Papers Downloader & Search Tool

This repository contains two separate but complementary tools designed for students and educators involved with the International Baccalaureate (IB) curriculum. The first tool automates the downloading of past IB Computer Science papers, while the second tool facilitates searching within these downloaded papers for specific text. These tools are especially useful for revision purposes, allowing for efficient access to and examination of past examination materials.

## Installation

Before running these tools, ensure you have Python installed on your system. These tools require Python 3.6 or later. You will also need to install `requests` and `PyPDF2` libraries if you haven't already. You can install these dependencies using pip:

```
pip install requests PyPDF2
```

## Tool 1: IB Past Papers Downloader

### Description

The IB Past Papers Downloader automates the process of downloading IB Computer Science past papers and their mark schemes from 2000 to 2021. It organizes the downloaded files into folders by year and session (May or November).

### Usage

To use the downloader, simply run the script without any arguments:

```python
python download_ib_papers.py
```

By default, the script downloads papers from 2000 to 2021. You can modify the `start_year` and `end_year` parameters in the script if you wish to download papers from a different range of years.

### Output

The downloaded exam papers and mark schemes are saved in the `IB_Papers` directory, organized into subfolders by year and session. If any errors occur during the download process, an `error_log.txt` file will be created in the `IB_Papers` directory listing the encountered errors.

## Tool 2: PDF Text Search Tool

### Description

This tool searches for specified text within the downloaded PDFs. It's useful for finding specific topics, questions, or information contained in the vast collection of past papers.

### Usage

Run the script and enter the text you wish to search for when prompted:

```python
python search_in_pdfs.py
```

You can modify the `directorio_base` variable in the script to change the base directory where the PDF files are located.

### Output

The script will print the paths to any PDF files that contain the specified text, allowing users to easily locate and review relevant materials.

## Contributions

Contributions to improve or extend the functionality of these tools are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
