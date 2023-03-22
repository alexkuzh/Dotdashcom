import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from pages.base import CommonOps
from utils.locators import FileDownloadLocators


class FileDownload(CommonOps):

    download_folder = 'd:/download/'

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/download'
        super().__init__(driver, url)

    def file_download(self):

        self.wait_for(FileDownloadLocators.FILE).click()
        # k = 0
        # while k < 100:
        #     if 'some-file.txt' in os.listdir(download_folder):
        #         k = 100
        #     else:
        #         time.sleep(0.5)
        #         k+=1
        try:
            WebDriverWait(self._driver, 60).until(lambda x: 'some-file.txt' in os.listdir(self.download_folder))
        except:
            return False
        return 'some-file.txt' in os.listdir(self.download_folder)

