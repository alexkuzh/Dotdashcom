import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from seletools.actions import drag_and_drop


class CommonOps(object):

    _driver = None

    def __init__(self, driver, url=''):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)
        self._action = ActionChains(driver)
        self._driver.get(url)

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def wait_for_all(self, locator):
        return self._wait.until(EC.presence_of_all_elements_located(locator))

    def find(self, locator):
        return self._driver.find_element(*locator)
    
    def context_click(self, locator):
        return self._action.context_click(locator)

    def is_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def move_mouse(self, locator):
        el = self.find(locator)
        ActionChains(self._driver).move_to_element(el).perform()

    def alert(self):
        return self._wait.until(EC.alert_is_present())

    def drag_n_drop(self, source_loc, target_loc):
        source = self.wait_for(source_loc)
        target = self.wait_for(target_loc)
        drag_and_drop(self._driver, source, target)

    def get_attribute(self, locator, attr_name):
        element = self.find(locator)
        if element:
            return element.get_attribute(attr_name)
        return None

    def switch_to_frame(self, locator):
        self._driver.switch_to.frame(locator)

    def switch_to_frame_default(self):
        self._driver.switch_to.default_content()

    def refresh_page(self):
        self._driver.refresh()
        self.wait_page_loaded()

    def get_logs(self):
        return self._driver.get_log('browser')

    def wait_page_loaded(self, timeout=10, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=0):
        """ This function waits until the page will be completely loaded.
            We use many different ways to detect is page loaded or not:

            1) Check JS status
            2) Check modification in source code of the page
            3) Check that all images uploaded completely
               (Note: this check is disabled by default)
            4) Check that expected elements presented on the page
        """

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self._driver.page_source
        except:
            pass

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self._driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self._driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self._driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Wait when some element will disappear:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self._driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self._driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Ignore timeout errors

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self._driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
