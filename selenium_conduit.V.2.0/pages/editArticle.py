import time
from pages.basePage import BasePage


class EditArticle(BasePage):

    edit_btn = '[class="btn btn-outline-secondary btn-sm"]'
    art_body = '[placeholder="Write your article (in markdown)"]'
    publish_btn = '[type="button"]'

    def edit_existing_article(self, text):

        edit_button = self.find_element(self.edit_btn)
        edit_button.click()

        article_body_field = self.find_element(self.art_body)
        article_body_field.clear()
        article_body_field.send_keys(text)

        publish_article_btn = self.find_element(self.publish_btn)
        publish_article_btn.click()

        time.sleep(0.5)

    def verify_edited_article(self):
        article_body_field = self.find_element(self.art_body)
        assert article_body_field == 'Edited'
