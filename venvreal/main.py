from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")
print(titles)
titles_list = []
for title in reversed(titles):
    titles_list.append(title.getText())
    print(title.getText())
    with open("movies.txt", "a") as file:
        file.write(f"{title.getText()}\n")



# article = soup.find_all(class_="titleline")
# article_upvote = soup.find_all(name="span", class_="score")
# #article_link = article.
# print(article)
# #print(article_link)
# article_texts = []
# article_links = []
# for article_tag in article:
#     article_text = article_tag.getText()
#     article_texts.append(article_text)
#     article_url = article_tag.get("href")
#     article_links.append(article_url)
#
# article_upvotes = []
# highest = 0
# for score in soup.find_all(name="span", class_="score"):
#     score_check = int(score.getText().split()[0])
#     article_upvotes.append(score_check)
#     if score_check > highest:
#         highest = score_check
#
# print(f"{article_texts}\n{article_links}\n{article_upvotes}\n")
# # another way to get the highest number in a list of int is to do
# # max(articles_upvotes)
# article_upvotes_index = article_upvotes.index(highest)
# print(f"{article_texts[article_upvotes_index]}\n{article_links[article_upvotes_index]}\n{article_upvotes[article_upvotes_index]}\n")
