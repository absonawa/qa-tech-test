from selenium import webdriver


class challenge1():

    def findIndex(self):

        driver = webdriver.Firefox()
        driver.get("http://localhost:3000/")
        driver.maximize_window()
        driver.find_element_by_xpath("//span[text()='Render the Challenge']").click()

        # Find number of rows
        rows = driver.find_elements_by_css_selector("tbody > tr")
        count = len(rows)
        print("Row count ",count)
        # Find index for each row
        for j in range(1, count+1):
            print("Row number: ", j)
            path = "tr:nth-of-type("+str(j)+ ") > td"
            elements = driver.find_elements_by_css_selector(path)

            # convert row into list
            list = []
            for element in elements:
                list.append(element.text)
            count = len(list)

            # half of list sum
            sum = 0
            for i in range(0, count):
                sum = sum + int(list[i])
            mid = sum / 2

            # Find index as per requirement
            sum = 0
            for i in range(0, count):
                sum = sum + int(list[i])
                if (mid > sum):
                    index = list[i]
            value = list.index(index) + 1
            print('Index value is ', value)
            cpath = "//div[text()='submit challenge " + str(j) + "']//following::input[1]"
            driver.find_element_by_xpath(cpath).send_keys(value)
        driver.find_element_by_xpath("//div[text()='Your Name']//following::input[1]").send_keys("Abhishek Sonawa")
        driver.find_element_by_xpath("//span[text()='Submit Answers']").click()

obj = challenge1()
obj.findIndex()
