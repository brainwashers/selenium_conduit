from pages.login import LoginPage
from tests.testCase import TestCase
from pages.readArticle import ReadArticle
from pages.editArticle import EditArticle

USER = {
    'username': 'enixan25',
    'email': 'enixan25@gmail.com',
    'password': 'Enixan25',
    'text': 'Edited'
}


class TestLoginFlow(TestCase):

    def test_login_as_registered_user(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login_as_registered_user(USER)

        read_article = ReadArticle(self.driver)
        read_article.open_existing_article()

        edit_article = EditArticle(self.driver)
        edit_article.edit_existing_article(USER['text'])