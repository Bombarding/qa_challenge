# QA Challenge
> QA Challenge Three - Tutorial

This text will be for the continuation, implementation and walkthrough of provided items

## Prerequisites

```
Python v2.7.9 is installed
Python has been added to the path on either linux or windows system
Pip is available and has been added to the path on either linux or windows system
Selenium IDE is available as a firefox or chrome plugin
```

## Required Packages

```python
Please run the following commands on your prefered Command line interface:
Linux/Windows:
pip install -U pytest
pip install -U pytest-cov
pip install -U coverage
pip install -U selenium

Linux:
pip install -U PyVirtualDisplay

Once they are installed please run the command: py.test -v --cov
This command will determine if all the required packages are installed properly
```

## Expanding the code

```
Due to the nature of pytest, we will be using a two file approach. Each script must be in its own allocated folder and include the following:
__init__.py
script.py
test_script.py

In order for py test to correctly determine which is the test file, `test_` is appended to the front of the secondary script. When looking at the scripts, the first script(script.py) is considered the logic script. Here we will build the logic for the webdriver to navigate the application. The second script(test_script.py) is the paramter script, and allows for coverage to complete the unit tests and map how much of the logic is being used. 
```

## Looking at the code

For the linux code, we will be focusing on the following lines:

```python
from pyvirtualdisplay import Display
def start_up(application_url):
    global web_driver, d
    d = Display(visible=0, size=(1920, 1080))
    d.start()
    web_driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
    web_driver.get(application_url)
```

Since we are assuming that we will not be running this code on a desktop linux environment, but rather a minimal installation with just CLI, this code must use pyvirtualdisplay. Other implementations have used Xvfb, but both will draw a headless window for geckodriver to use and navigate the application. As long as the firewall rules allow this instance type to reach out to the internet, then simply making the geckodriver executable by everyone will allow this to run properly. 

The same can also be said for the windows code, however, it is not using pyvirtualdisplay:

```python
def start_up(driver_location, application_url):
    global web_driver
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("start-maximized") #=> Runs System in Maximized Browser, for Debugging
    #browser_options.add_argument("--headless") #=> Runs System in Headless or Browserless Mode, for Jenkins
    web_driver = webdriver.Chrome(driver_location, options=browser_options)
    web_driver.get(application_url)
```

In order to obtain the relative xPaths, ids, names and CSS of the application, we are using Selenium IDE as a firefox extension. Navigate to the chrome store and search for `selenium` and apply the plugin. once done, select the plugin, create a new test, enter the test URL of the application, and begin recording. Any recording paramaters generated from Selenium IDE, will be in the `test_` file.

![](https://i.gyazo.com/29d0a81131dcb7774d25ad6c74a6a7ce.png)
