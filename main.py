import requests
from bs4 import BeautifulSoup


class NewsAggregator:
    def __init__(self):
        self.user_preferences = {}
        self.bookmarked_articles = []

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.search_news()
            elif choice == '2':
                self.view_bookmarks()
            elif choice == '3':
                self.update_user_preferences()
            elif choice == '4':
                self.update_bookmarks()
            elif choice == '5':
                self.exit_program()
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("=== Topic-Based News Aggregator ===")
        print("1. Search News")
        print("2. View Bookmarks")
        print("3. Update User Preferences")
        print("4. Update Bookmarks")
        print("5. Exit")

    def search_news(self):
        query = input("Enter your search query: ")
        optimized_query = self.optimize_query(query)
        news_articles = self.get_news_articles(optimized_query)
        filtered_articles = self.filter_articles(news_articles)
        ranked_articles = self.rank_articles(filtered_articles)
        personalized_articles = self.personalize_articles(ranked_articles)
        self.display_articles(personalized_articles)

    def optimize_query(self, query):
        return query

    def get_news_articles(self, query):
        news_articles = []
        url = f"https://example.com/search?query={query}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            articles = soup.find_all("article")
            for article in articles:
                title = article.find("h2").text.strip()
                summary = article.find("p").text.strip()
                author = article.find("span", class_="author").text.strip()
                date = article.find("span", class_="date").text.strip()
                url = article.find("a")["href"]
                article_data = {
                    "title": title,
                    "summary": summary,
                    "author": author,
                    "date": date,
                    "url": url
                }
                news_articles.append(article_data)
        return news_articles

    def filter_articles(self, news_articles):
        filtered_articles = news_articles
        return filtered_articles

    def rank_articles(self, news_articles):
        ranked_articles = news_articles
        return ranked_articles

    def personalize_articles(self, news_articles):
        personalized_articles = news_articles
        return personalized_articles

    def display_articles(self, news_articles):
        for index, article in enumerate(news_articles, start=1):
            print(f"{index}. {article['title']}")
            print(f"   Summary: {article['summary']}")
            print(f"   Author: {article['author']}")
            print(f"   Date: {article['date']}")
            print(f"   URL: {article['url']}")
            print()
        
        option = input("Enter the number of the article to bookmark (0 to skip): ")
        if option != '0':
            article_index = int(option) - 1
            self.bookmark_article(news_articles[article_index])

    def bookmark_article(self, article):
        if article not in self.bookmarked_articles:
            self.bookmarked_articles.append(article)
            print("Article bookmarked successfully!")
        else:
            print("Article is already bookmarked.")

    def view_bookmarks(self):
        if self.bookmarked_articles:
            print("=== Bookmarked Articles ===")
            for index, article in enumerate(self.bookmarked_articles, start=1):
                print(f"{index}. {article['title']}")
                print(f"   Summary: {article['summary']}")
                print(f"   Author: {article['author']}")
                print(f"   Date: {article['date']}")
                print(f"   URL: {article['url']}")
                print()
        else:
            print("No articles bookmarked.")

    def update_user_preferences(self):
        preference = input("Enter your news preference: ")
        self.user_preferences = {"preference": preference}
        print("User preferences updated successfully!")

    def update_bookmarks(self):
        if self.bookmarked_articles:
            print("=== Bookmarked Articles ===")
            for index, article in enumerate(self.bookmarked_articles, start=1):
                print(f"{index}. {article['title']}")
                print(f"   Summary: {article['summary']}")
                print(f"   Author: {article['author']}")
                print(f"   Date: {article['date']}")
                print(f"   URL: {article['url']}")
                print()

            option = input("Enter the number of the article to remove (0 to skip): ")
            if option != '0':
                article_index = int(option) - 1
                del self.bookmarked_articles[article_index]
                print("Article removed from bookmarks successfully!")
        else:
            print("No articles bookmarked.")

    def exit_program(self):
        print("Exiting the program... Goodbye!")


if __name__ == "__main__":
    news_aggregator = NewsAggregator()
    news_aggregator.run()