# URL Status Checker

This project allows you to check the HTTP status codes of URLs listed in a text file. If the status code is **200** (OK), the URL is saved to an output file.

## Features

- Reads a text file containing a list of URLs.
- For each URL, the script makes a **HEAD** HTTP request (using `curl`) and retrieves the HTTP status code.
- If the status code is **200**, the URL is saved to an output file.
- The output file contains all URLs that returned a **200** status.

## Prerequisites

Before you start, make sure you have the following:

1. **Python 3.x** installed on your machine.
   - To check if you have Python installed, run the command:
     ```bash
     python3 --version
     ```
   - If you don’t have Python 3.x, you can install it from [the official Python website](https://www.python.org/downloads/).

2. **curl** installed on your system.
   - `curl` is used by the script to send HTTP requests and check the status codes.
   - If `curl` is not installed, you can install it with the following command (on Debian/Ubuntu systems):
     ```bash
     sudo apt install curl
     ```

## Installation

Follow these steps to install and set up the project:

1. **Clone the repository or download the script**:
   - To clone the repository, run:
     ```bash
     git clone <REPOSITORY_URL>
     cd <project_directory>
     ```

2. **Install the required Python dependencies**:
   - Make sure you are in the project directory where `requirements.txt` is located.
   - Install the dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

Once the setup is complete, follow these steps to use the script:

### 1. Create a text file (`links.txt`) containing the URLs you want to test, one URL per line.

Example content for `links.txt`:


### 2. Run the Python script to check the status codes of the URLs.

Run the following command in your terminal:

```bash
python3 check_status.py
