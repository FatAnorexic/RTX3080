import time
from selenium import webdriver

##Using the Chromedriver to talk it webpage. Other Explorers may not need this, they might see SeleniumDoc
browser = webdriver.Chrome('C:\\Users\\Alexb\\OneDrive\\Desktop\\Coding Python\\Computat Phys\\Side Proj\\chromedriver.exe')

##Grab best buy webpage
browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
##TestBed
#browser.get("https://www.bestbuy.com/site/insignia-aaa-batteries-8-pack/5491600.p?skuId=5491600")
buyButton = False

while not buyButton:
    try:
        #time.sleep(2)
        #If this works the button is currently sold out
        addToCartButton = addButton = browser.find_element_by_class_name("btn-disabled")

        #Button Isn't open on the script
        #print("The Button isn't ready yet")

        #this refreshes the page with some delay to avoid detection
        browser.refresh()
    except:

        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        print('The buy Button was clicked')
        addToCartBtn.click()
        #time.sleep(3)
        plsWaitBtn = browser.find_element_by_class_name("overlayTrigger")
        while plsWaitBtn == True:
            time.sleep(1)
        addToCartBtn.click()
        #time.sleep(2)
        buyButton=True

while buyButton == True:
    time.sleep(2)

    goTo = addButton = browser.find_element_by_class_name("go-to-cart-button")
    goTo.click()
    goTo=False

    time.sleep(2)

    CheckOut = addButton = browser.find_element_by_class_name("btn-primary")
    CheckOut.click()

    """Auto insert the username info and password, then click the checkout button."""
    time.sleep(1)

    AddUsername = browser.find_element_by_id('fld-e')
    AddUsername.click()

    AddUsername.send_keys("email")

    AddPassword = browser.find_element_by_id('fld-p1')
    AddPassword.click()

    AddPassword.send_keys("password")

    SignIn = addButton = browser.find_element_by_class_name('cia-form__controls__submit')
    SignIn.click()
    break

