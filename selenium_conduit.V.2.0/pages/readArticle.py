import time
from pages.basePage import BasePage


class ReadArticle(BasePage):

    article_link = '[href="#article/test-conduit-pqzalw"]'

    def open_existing_article(self, userdata):

        open_my_feed = self.find_element_by_text(userdata['username'], 'a')
        open_my_feed.click()

        time.sleep(0.5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        open_article = self.find_element(self.article_link)
        open_article.click()

        time.sleep(0.5)



