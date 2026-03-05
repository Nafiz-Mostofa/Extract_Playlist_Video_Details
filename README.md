# YouTube Playlist Scraper 📺🐍

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-webdriver-green.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-orange.svg)
![Pandas](https://img.shields.io/badge/pandas-data_extraction-red.svg)

Automate YouTube playlist scraping! This Python script uses Selenium to bypass dynamic JavaScript loading, BeautifulSoup to parse video links, and Pandas to instantly export the extracted data into a clean Excel and CSV file. 
Designed with broadcast automation and efficient workflow management in mind, this tool helps you quickly extract video data without manual copy-pasting.

## 📑 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#️-installation)
- [How to Use](#-how-to-use)
- [Contributing](#-contributing)
- [License](#️-license)
- [Author](#-author)

## ✨ Features
* **Dynamic Web Scraping:** Uses Selenium WebDriver in headless mode to render JavaScript-heavy YouTube pages without opening a visible browser window.
* **Accurate Parsing:** Utilizes BeautifulSoup to specifically target and extract video titles and URLs via the `video-title` ID.
* **Automated Data Export:** Seamlessly formats the scraped data and saves it directly to Excel and CSV file (UTF-8 encoded to support emojis and international characters).
* **Lightweight & Fast:** Optimized with implicit waits to ensure the page loads correctly before data extraction begins.

## 📋 Prerequisites
Ensure you have the following installed on your system:
* **Python 3.x**
* **Google Chrome** (The script uses the Chrome WebDriver in the background)

## 🛠️ Installation
1. **Clone this repository to your local machine:**
   ```bash
   git clone https://github.com/Nafiz-Mostofa/Extract_Playlist_Video_Details.git

2. **Navigate to the project directory:**
   ```bash
   cd [project_clone_path]
   
3. **Install the required Python dependencies:**
   ```bash
   pip install selenium beautifulsoup4 pandas openpyxl
   ```
   This may not work on many Windows systems. For that, you will need to open your Command Prompt by running it as administrator. Then copy and paste the code below.
   ```bash
   py -m pip install selenium beautifulsoup4 pandas openpyxl

## 💻 How to Use
1. Open the Python script in your preferred code editor.
2. Locate the playlist_link variable at the bottom of the script.
3. Replace the placeholder URL with the actual YouTube playlist URL you want to scrape:
   playlist_link = "[https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID_HERE](https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID_HERE)"
4. Run the script from your terminal:
   ```bash
   py Script.py
   ```
   If you change the file name [Script.py], than you should use the exact new_file_name.py. Otherwise, project will not run.
5. Check your project folder. You will find a newly generated .xlsx and .csv files containing the extracted data.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute to improving the script.<br><br>
**Disclaimer: This script is intended for educational purposes and personal workflow automation. Please be mindful of YouTube's Terms of Service regarding automated access and rate limits.**

## ⚖️ License
This project is open-source.

## 👤 Author
Github: https://github.com/Nafiz-Mostofa <br>
Linkedin: https://www.linkedin.com/in/nafizmostofa/