

# 電腦\HKEY_CLASSES_ROOT\MSEdgeHTM\shell\open\command
# "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --single-argument %1
 
# msedge.exe --remote-debugging-port=9222 --user-data-dir="D:\01_firmware\web-crawler\profile" --single-argument %1

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.edge.options import Options
edge_op = Options()

edge_op.add_experimental_option("debuggerAddress","127.0.0.1:9222")
web = Edge(options=edge_op)
web.get('edge://version/')