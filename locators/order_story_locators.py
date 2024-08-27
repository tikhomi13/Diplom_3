from selenium.webdriver.common.by import By

class OrderStoryLocators:

    ORDER_HISTORY_WINDOW = (By.XPATH, ".//div[@class='OrderHistory_orderHistory__qy1VB']")

    ORDERS_STORY_SELECTED = (By.XPATH, ".//a[contains(@class, 'Account_link_active') and @href='/account/order-history']")


