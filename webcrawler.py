

# 電腦\HKEY_CLASSES_ROOT\MSEdgeHTM\shell\open\command
# "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --single-argument %1
 
# msedge.exe --remote-debugging-port=9222 --user-data-dir="D:\01_firmware\web-crawler\profile" --single-argument %1

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.edge.options import Options
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) edge/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}

edge_op = Options()
edge_op.use_chromium = True
edge_op.add_argument("--headless")

# Define a custom user agent
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) edge/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
edge_op.add_argument(f"--user-agent={my_user_agent}")
edge_op.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
web = Edge(options = edge_op)
# web.get('https://members.myactivesg.com/auth?redirect=%2Fprofile')
# web.get('https://www.python.org')
web.get('https://members.myactivesg.com/cart')
# search_bar = web.find_element(By.NAME, "q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(web.current_url)

# web.get('edge://version/')
# Get user Agent with execute_script
# driver_ua = web.execute_script("alert(\"alert via selenium\")")
# driver_ua = web.execute_script("return navigator.userAgent")
# print("User agent:")
# print(driver_ua)


# navigate().to("https://www.browserstack.com/selenium")