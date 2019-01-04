## puppeteer 同步接口


### 使用示例

```python
from Pypuppeteer import Webdriver
browser = Webdriver(headless=False)
browser.current_page.request("https://www.baidu.com")
print(browser.current_page.get_page_content())
browser.current_page.wait_for(60*100)
browser.current_page.close()

```