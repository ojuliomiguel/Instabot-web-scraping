from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class InstaBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\\Users\\JulioMiguel\\geckodriver')
        
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name ='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name ='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(4)
        
    def curtirFotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
                
        for i in range(0):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        
        pics_class = driver.find_elements_by_css_selector('div[class="Nnq7C weEfm"]')
        posts = [elem.find_elements_by_tag_name('a') for elem in pics_class] #Matriz 11 X 3
        posts_hrefs = []
        
        #links dos posts added em posts_hrefs
        for i in range(len(posts)):
            for j in range(3):
                posts_hrefs.append(posts[i][j].get_attribute('href'))
        
        print('Qtde_elementos: {}'.format(len(posts_hrefs)))

        #Curtir os posts
        for i in range(len(posts)):
            driver.get(posts_hrefs[i])
            sectionButtons = driver.find_element_by_css_selector('section[class="ltpMr Slqrh"]')
            likeButton = sectionButtons.find_element_by_css_selector('button[class="wpO6b "]')
            likedButton = likeButton.find_element_by_css_selector('svg[class="_8-yf5 "]').get_attribute('aria-label')
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                if(likedButton not in ('Unlike', 'Descurtir')):
                    likeButton.click()
                    time.sleep(10)
            except Exception as e:
                time.sleep(5)

    def unfollow(self):
        driver = self.driver
        driver.get('https://www.instagram.com/' + self.username[1:])
        following = driver.find_elements_by_css_selector('ul[class="k9GMp "]')[0].find_elements_by_tag_name('li')
        following[2].find_element_by_css_selector('a[class="-nal3 "]').click()
        time.sleep(3)

        followersList = driver.find_elements_by_css_selector('div[class="PZuss"]')[0].find_elements_by_tag_name('li')
        divfollowers = driver.find_element_by_css_selector('div[class="isgrP"]').click()
        actionChain = webdriver.ActionChains(self.driver)

        for i in range(9):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            followersList = driver.find_elements_by_css_selector('div[class="PZuss"]')[0].find_elements_by_tag_name('li')
            print(len(followersList)) 

        seguidor = 0
        minutos = 0
        #armazenar as referências de cada bnt dos users ou ver outras soluções
        
        for i in range(7):
            for j in range(10):
                time.sleep(1)
                followersList[seguidor].find_element_by_css_selector('button[class="sqdOP  L3NKy    _8A5w5    "]').click()
                seguidor += 1
                time.sleep(1)
                driver.find_element_by_css_selector('button[class="aOOlW -Cab_   "]').click()
            
            minutos += 5
            print('Seguidores removidos: {} nos primeiros {} minutos'.format(seguidor, minutos))
            time.sleep(300)
        

