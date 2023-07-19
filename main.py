from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

path = "C:/Users/noorn/Documents/SCHOOL/Development/chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)

URL = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
driver.get(URL)

detailed_view = driver.find_element(By.ID, "list-view-option-detailed")
detailed_view.click()

show_name_class = "ipc-title__text"
names = driver.find_elements(By.CLASS_NAME, show_name_class)
show_names = []
for name in names:
    show_names.append(name.text)
show_names = show_names[2:252]
tv_show_names = []
for name in show_names:
    name = name.split(". ")[1]
    tv_show_names.append(name)

details_class = "sc-14dd939d-5"
details_results = driver.find_elements(By.CLASS_NAME, details_class)
details = []
for detail in details_results:
    details.append(detail.text)
years = []
num_episodes = []
ratings = []
for item in details:
    item = item.split("\n")
    if len(item) == 3:
        years.append(item[0])
        num_episodes.append(item[1].split(" ")[0])
        ratings.append(item[2])
    else:
        years.append(item[0])
        num_episodes.append(item[1].split(" ")[0])
        ratings.append("N/A")

type_class = "aPntv"
type_results = driver.find_elements(By.CLASS_NAME, type_class)
types = []
for t in type_results:
    types.append(t.text)

score_class = "ipc-rating-star"
score_results = driver.find_elements(By.CLASS_NAME, score_class)
scores = []
for score in score_results:
    scores.append(score.text)
scores = scores[0::2]

vote_class = "fsmPsX"
vote_results = driver.find_elements(By.CLASS_NAME, vote_class)
votes = []
for vote in vote_results:
    votes.append(vote.text)
num_votes = []
for vote in votes:
    vote = vote.split("s")[1]
    num_votes.append(vote)

driver.quit()

# DATA COLUMNS:
# 1. Name (tv_show_names)
# 2. Year (years)
# 3. No. Episodes (num_episodes)
# 4. Rating (ratings)
# 5. Type of TV Series (types)
# 6. Score out of 10 (scores)
# 7. No. Votes (num_votes)

column_names = ["Show Name", "Years", "No. Episodes", "Ratings", "Show Type", "Score out of 10", "No. Votes"]
rows = zip(tv_show_names, years, num_episodes, ratings, types, scores, num_votes)
with open("shows.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(column_names)
    for row in rows:
        writer.writerow(row)
