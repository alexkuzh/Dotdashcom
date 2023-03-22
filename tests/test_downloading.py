from pages.fileDownload import FileDownload


def test_download_file(driver):
    page = FileDownload(driver)
    page.wait_page_loaded()
    assert page.file_download()


