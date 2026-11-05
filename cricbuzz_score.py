
from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:

    # Open browser
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        # Open Cricbuzz
        page.goto(
            "https://www.cricbuzz.com/",
            wait_until="domcontentloaded"
        )

        print("Waiting for live score...")

        # Wait until a score appears on the page
        score = page.locator(
            "text=/\\d+\\/\\d+/"
        ).first

        score.wait_for(state="visible", timeout=30000)

        # Get score text
        score_text = score.inner_text()

        print("Live Cricket Score:")
        print(score_text)

        # Save screenshot
        page.screenshot(path="score.png")

        print("Screenshot saved: score.png")

    except TimeoutError:
        print("No live match found or score did not load.")

        # Save screenshot even if no score is found
        page.screenshot(path="score.png")

    finally:
        browser.close()
