from selenium.webdriver.common.by import By


class LoginLocators(object):
    FORM_USERNAME = (By.ID, "username")
    FORM_PASSWORD = (By.ID, "password")
    FORM_SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    FORM_ALERT = (By.ID, "flash")
    LOGOUT_BTN = (By.CLASS_NAME, "button")


class CheckBoxesLocators(object):
    FORM_CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes > input")


class ContexMenuLocators(object):
    CONTEXT_MENU = (By.LINK_TEXT, "Context Menu")
    CONTEXT_BOX = (By.ID, "hot-spot")


class DragAndDropLocators(object):
    COLUMNS_1 = (By.ID, "column-a")
    COLUMNS_2 = (By.ID, "column-b")


class DropDownLocators(object):
    DD_MENU = (By.ID, "dropdown")
    OPTION1 = (By.XPATH, "//*[@id='dropdown']/option[2]")
    OPTION2 = (By.XPATH, "//*[@id='dropdown']/option[3]")


class DynamicContentLocators(object):
    IMG = (By.XPATH, "//*[@id='content']/div[3]/div[1]/img")
    TXT = (By.XPATH, "//*[@id='content']/div[3]/div[2]")


class DynamicControlLocators(object):
    DYNAMIC_CONTROL = (By.LINK_TEXT, "Dynamic Controls")
    CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    INPUT_TEXT = (By.XPATH, "//input[@type='text']")
    STATE_CHANGE = (By.ID, "message")


class DynamicLoadingLocators(object):
    BUTTON = (By.TAG_NAME, "button")
    TEXT = (By.ID, "finish")


class FileDownloadLocators(object):
    FILE = (By.LINK_TEXT, "some-file.txt")


class FileUploadLocators(object):
    FILE = "d:\download\some-file.txt"
    CHOOSE_FILE_BUTTON = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILE = (By.ID, "uploaded-files")
    DND_ZONE = (By.CSS_SELECTOR, "#drag-drop-upload > div > div.dz-details > div")
    INPUT_DND_ZONE = (By.XPATH,"//input[@class='dz-hidden-input']")


class FloatingMenuLocators(object):
    MENU = (By.ID, "menu")


class IframeLocators(object):
    IFRAME = "mce_0_ifr"
    TEXT_BODY = (By.ID, "tinymce")


class MouseHoverLocators(object):
    FIGURE1 = (By.XPATH, "//*[@id='content']/div/div[1]")
    FIGURE2 = (By.XPATH, "//*[@id='content']/div/div[2]")
    FIGURE3 = (By.XPATH, "//*[@id='content']/div/div[3]")
    FIG_CAPTIONS = (By.CLASS_NAME, "figcaption")


class JavaScriptAlertLocators(object):
    BUTTON_ALERT = (By.XPATH, "//button[contains(text(),'Click for JS Alert')]")
    BUTTON_CONFIRM = (By.XPATH, "//button[contains(text(),'Click for JS Confirm')]")
    BUTTON_PROMPT = (By.XPATH, "//button[contains(text(),'Click for JS Prompt')]")
    RESULT = (By.ID, "result")
    TXT_ALERT = "You successfuly clicked an alert"
    TXT_CONFIRM_YES = "You clicked: Ok"
    TXT_CONFIRM_CANCEL = "You clicked: Cancel"
    TXT_PROMPT = "You entered: "


class NewWindowLocators(object):
    LINK = (By.LINK_TEXT, "Click Here")
    TEST_TEXT = "New Window"


class NotificationLocators(object):
    LINK = (By.LINK_TEXT, "Click here")
    FLASH = (By.ID, "flash")
    # unsucceSSful
    MESSAGES = ["Action successful", "Action unsuccesful, please try again"]
