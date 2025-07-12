# Email Scraper

This is a simple web scraper script written in Python that scans a specified website for email addresses. It can extract emails from the website's HTML content and also from any `mailto:` links. The script allows you to set the number of emails you want to collect and handles crawling through multiple pages of the website.

## Features
- Extracts emails from website HTML and `mailto:` links.
- Handles relative and absolute URLs while crawling through pages.
- Limits the number of emails collected based on user input.
- Prints out all collected emails in the console.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
<pre>sudo apt install python3-pip
pip3 install requests beautifulsoup4</pre>
  

# How to Use
<pre>git clone https://github.com/requestsimple/email-scraper
cd email-scraper
python3 email_scraper.py</pre>
