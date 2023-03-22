from pages.base import CommonOps


class JavaScriptError(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/javascript_error'
        super().__init__(driver, url)

    def js_error(self):
        logs = self.get_logs()
        return logs[0]['message'].split(' Uncaught ')[-1]

