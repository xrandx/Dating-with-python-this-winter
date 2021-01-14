from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def get_books(douban_id):
    book_names = set()
    driver = webdriver.Chrome(r'C:\Users\kevty\winter_lesson\chromedriver.exe')
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 30, 0.5)
    url = "https://book.douban.com/people/{0}".format(douban_id)
    driver.get(url)
    sleep(0.2)
    url = "https://book.douban.com/people/{0}/collect".format(douban_id)
    driver.get(url)

    paginator = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "paginator")))
    pages = paginator[0].find_elements_by_xpath(".//*")
    for i in pages:
        print(i.text)
    page_count = len(pages) - 4

    for p in range(page_count):
        elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "info")))
        for elem in elements:
            tmp = elem.find_elements_by_xpath(".//*")
            book_names.add(str(tmp[1].text).strip())
        next = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "next")))
        next[0].click()
        sleep(0.5)
    return book_names


# 共同的看过的书
class DoubanBook:
    def __init__(self, douban_id):
        self.douban_id = douban_id
        self.book_names = get_books(douban_id)

    def save(self):
        temp = ""
        for book in self.book_names:
            temp += "{0}\n".format(book)

        with open(self.douban_id + "_books.txt", "w", encoding="utf-8") as f:
            f.write(temp)

    @staticmethod
    def find_mutual_books(a, b):
        return a.book_names & b.book_names


def main():
    my_books = DoubanBook("cul8")
    my_books.save()
    ohter_books = DoubanBook("sunflower1988")
    ohter_books.save()
    print(DoubanBook.find_mutual_books(my_books, ohter_books))



if __name__ == '__main__':
    main()
