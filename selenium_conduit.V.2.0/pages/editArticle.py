import time
from pages.basePage import BasePage


class EditArticle(BasePage):

    edit_btn = '[class="btn btn-outline-secondary btn-sm"]'
    art_body = '[placeholder="Write your article (in markdown)"]'
    publish_btn = '[type="button"]'
    check = '[class="col-xs-12"]'

    def edit_existing_article(self, user_data):

        edit_button = self.find_element(self.edit_btn)
        edit_button.click()

        article_body_field = self.find_element(self.art_body)
        time.sleep(1)
        article_body_field.clear()
        time.sleep(1)
        article_body_field.send_keys(user_data['text'])
        time.sleep(1)
        publish_article_btn = self.find_element(self.publish_btn)
        publish_article_btn.click()

        time.sleep(5)

    def verify_edited_article(self, userdata):
        article_body_field = self.find_element(self.check)
        assert article_body_field.text == userdata['text']
