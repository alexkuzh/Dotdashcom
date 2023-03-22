from pages.base import CommonOps
from utils.locators import FileUploadLocators


class FileUpload(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/upload'
        super().__init__(driver, url)

    def upload_file_button(self):
        self.find(FileUploadLocators.CHOOSE_FILE_BUTTON).send_keys(FileUploadLocators.FILE)
        self.find(FileUploadLocators.UPLOAD_BUTTON).click()
        msg = self.wait_for(FileUploadLocators.UPLOADED_FILE)
        return msg.text

    def upload_drag_n_drop_file(self):
        self.find(FileUploadLocators.INPUT_DND_ZONE).send_keys(FileUploadLocators.FILE)
        msg = self.wait_for(FileUploadLocators.DND_ZONE)
        return msg.text
