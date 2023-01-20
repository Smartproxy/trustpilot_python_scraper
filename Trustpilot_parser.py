import json
import requests
from bs4 import BeautifulSoup


url = "https://scrape.smartproxy.com/v1/tasks?universal="

payload = {
    "target": "universal",
    "url": "https://www.trustpilot.com/review/panaceafinancial.com",
    "headless": "html",
    "device_type": "desktop"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic AUTH"
}

def main():

    response = requests.post(url, json=payload, headers=headers)
    
    json_data = response.text
    
    parsed_data = json.loads(json_data)
    
    content = parsed_data['results'][0]['content']
    
    # strip scraped content from backslashes
    
    stripped_content = content.replace('\\','')
    
    soup = BeautifulSoup(stripped_content, "html.parser")
    
    # select review text element
    
    review_text = soup.find_all("p", class_="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn")
    
    # select review date element
    
    review_date = soup.find_all("p", class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 typography_color-black__5LYEn")
    
    # select review score element
    
    img_tags = soup.select('.star-rating_starRating__4rrcf img')
    
    reviews = []
    
    for p, d, img_tag in zip(review_text, review_date, img_tags):
        # create a dictionary for each review
        review = {
            'text': p.text,
            'date': d.text,
            'rating': img_tag['alt']
        }
        # add the review to the list
        reviews.append(review)
    
        # dump the output to .json
    with open('reviews.json', 'w') as outfile:
    	json.dump(reviews, outfile)

if __name__ == "__main__":
    main()
