# WebCrawler

This is a multithread chatroom project built with C++ using sockets and mutexes.


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

* Python 3.5 or above
 
## Installation

1. Clone the repository or download the source code to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required dependencies using pip:

 ```bash   

pip install -r requirements.txt

```
## Usage

To use the WebCrawler, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Use the following command to run the script:

```bash

python3 main.py -w <website_url> -o <output_folder>

Replace `<website_url>` with the URL of the website you want to crawl and `<output_folder>` with the folder where you want to save the extracted data.

```
3. The script will start crawling the website and extracting data. The extracted data will be saved in the specified output folder.


## Options

The WebCrawler supports the following command-line options:

- `-h`, `--help`: Show the help message and exit.
- `-w`, `--website`: The website URL to crawl.
- `-o`, `--output`: The output folder where the extracted data will be saved.

## Example

Here's an example of how to use the WebCrawler:

```bash

python3 main.py -w https://example.com -o data/

```

In this example, we specify the target website URL as `https://example.com` and the output folder as `data/`. The script will start crawling the website and save the extracted data in the `data/` folder.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more information.

