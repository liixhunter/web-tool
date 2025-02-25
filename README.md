# URL Status Checker

This project allows you to check the HTTP status codes of URLs listed in a text file. If the status code is **200** (OK), the URL is saved to an output file.

## Features

- Reads a text file containing a list of URLs.
- For each URL, the script makes a **HEAD** HTTP request (using `curl`) and retrieves the HTTP status code.
- If the status code is **200**, the URL is saved to an output file.
- The output file contains all URLs that returned a **200** status.

## Prerequisites

- Python 3.x installed on your machine.
- The `curl` command should be available in your terminal (pre-installed on most UNIX systems).

## Installation

1. Clone this repository or download the Python script to your machine.

```bash
git clone <REPOSITORY_URL>
cd <project_directory>
