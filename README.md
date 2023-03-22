# Dotdashcom Webdriver Tests
## Prerequisites
* Docker
* Git
* Python
* Webdriver
* ChromeDriver
* IDE such as PyCharm 2022.+
## Steps
1. Pull Docker image for the-internet app:
  
    `docker pull gprestes/the-internet`
  
2. Run the following command: 

    `docker run -d -p 7080:5000 gprestes/the-internet`
  
3. Set the following BaseUrl for your tests:

   `http://localhost:7080`

4. Tests in the folder `tests`


  *    Login Success  [test_login_success.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_login_success.py)
  *    Login Failure  [test_login_failure.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_login_failure.py)
  *    CheckBoxes  [test_checkboxes.py ](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_checkboxes.py)
  *    ContextMenu  [test_contextMenu.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_contextMenu.py)
  *    Drag and Drop  [test_drag_n_drop.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_drag_n_drop.py)
  *    Dropdown  [test_dropdown.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_dropdown.py)
  *    Dynamic Content  [test_dinamicContent.py ](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_dinamicContent.py)
  *    Dynamic Controls  [test_dynamic_controls.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_dynamic_controls.py)
  *    Dynamic Loading  [test_dynamic_loading.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_dynamic_loading.py)
  *    File Download  [test_downloading.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_downloading.py)
  *    File Upload  [test_uploading.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_uploading.py)
  *    Floating Menu  [test_floating_menu.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_floating_menu.py)
  *    Iframe  [test_iframe.py ](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_iframe.py)
  *    Mouse Hover  [test_mouse_hover.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_mouse_hover.py)
  *    JavaScript Alerts  [test_js_alerts.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_js_alerts.py)
  *    JavaScript Error  [test_js_error.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_js_error.py)
  *    Open in New Tab  [test_new_window.py ](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_new_window.py)
  *    Notification Message  [test_notification.py](https://github.com/alexkuzh/Dotdashcom/blob/main/tests/test_notification.py)

5. Page Objects in the folder `pages`

6. Fixture (setUp, tearDown) [conftest.py](https://github.com/alexkuzh/Dotdashcom/blob/main/conftest.py)

7. Run test 
        * cd project_path
        * `pytest tests` if you need html report `pytest --html=report.html tests`

## Requirements
* selenium~=4.8.0
* seletools~=1.3.0
* pytest~=7.2.2