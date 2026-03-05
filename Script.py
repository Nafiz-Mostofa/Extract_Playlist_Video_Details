from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_youtube_playlist_to_excel(playlist_url, output_filename="playlist_data.xlsx"):
    # Configure Chrome options to run in the background (headless mode)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs browser without UI
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--mute-audio")

    print("Launching browser and loading the page...\n")

    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Navigate to the YouTube playlist URL
        driver.get(playlist_url)

        # Wait for 5 seconds to allow JavaScript to load the dynamic content
        time.sleep(5)

        # Extract the fully loaded HTML source code from the browser
        html_source = driver.page_source

    finally:
        # Ensure the browser is closed after getting the source code
        driver.quit()

    # --- Begin parsing with BeautifulSoup ---
    print("Parsing data...\n")
    soup = BeautifulSoup(html_source, 'lxml')

    # Find all <a> tags with id="video-title"
    video_tags = soup.find_all('a', id='video-title')

    if not video_tags:
        print("No video links found. The page might not have loaded completely.")
        return

    # Create an empty list to store the extracted data
    scraped_data = []

    # Loop through the tags, extract the href attribute, and build the full URLs
    for index, tag in enumerate(video_tags, start=1):
        href = tag.get('href')

        # Ensure the href attribute is not empty
        if href:
            # Combine the relative path with the YouTube base URL
            full_link = f"https://www.youtube.com{href}"

            # Extract the video title, defaulting to 'No Title' if not found
            title = tag.get('title', 'No Title')

            # Append the title and link as a dictionary to our list
            scraped_data.append({
                # "Serial": index,
                "Video Title": title,
                "Video Link": full_link
            })

    # --- Save data to Excel ---
    if scraped_data:
        print("Saving data to Excel file...\n")

        # Convert the list of dictionaries into a Pandas DataFrame
        df = pd.DataFrame(scraped_data)

        # Save the DataFrame to an Excel file without the index column
        df.to_excel(output_filename, index=False)

        print(
            f"Success! {len(scraped_data)} videos have been saved to '{output_filename}'.")

    # --- Save data to CSV ---
    if scraped_data:
        print("Saving data to CSV file...\n")

        # Convert the list of dictionaries into a Pandas DataFrame
        df = pd.DataFrame(scraped_data)

        # Ensure the filename has a .csv extension instead of .xlsx
        csv_filename = output_filename.replace('.xlsx', '.csv')

        # Save the DataFrame to a CSV file without the index column
        # 'utf-8-sig' encoding prevents text corruption for special characters or emojis in video titles
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

        print(
            f"Success! {len(scraped_data)} videos have been saved to '{csv_filename}'.")


# Replace this with your actual YouTube playlist link
playlist_link = "https://www.youtube.com/playlist?list=PL4TtBB4Zl9EyLI5HZalFzFqeaCXuWTia5"

# Call the function and specify the Excel file name
scrape_youtube_playlist_to_excel(
    playlist_link, "Python_Automation_Video_Link.xlsx")
