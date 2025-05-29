from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# PATH to your chromedriver.exe (adjust this to where you saved it)
CHROMEDRIVER_PATH = r"C:\Users\Vinc\chromedriver\chromedriver.exe"



def fetch_live_status(hbl_number, headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print(f"🔍 Searching for HBL: {hbl_number}")
        driver.get("https://ftn.fedex.com/app/quickfind/QuickFindProto.jsp")

        time.sleep(2)  # Let the page load

        # Find the HBL/HAWB input field and enter the number
        input_box = driver.find_element(By.NAME, "searchNumber")
        input_box.send_keys(hbl_number)
        input_box.send_keys(Keys.RETURN)

        time.sleep(3)  # Wait for results to load

        # Try to pull any result text
        result_text = driver.page_source

        if "No records found" in result_text:
            print("🚫 No records found for that HBL.")
        else:
            print("✅ Results retrieved. Here's a preview:")
            print("-" * 40)
            print(result_text[:1000])  # Just preview the first 1000 chars

    except Exception as e:
        print("⚠️ Error during scraping:", e)
    finally:
        driver.quit()

# Test it
if __name__ == "__main__":
    hbl = input("Enter a real HBL/HAWB number: ").strip()
    fetch_live_status(hbl)
