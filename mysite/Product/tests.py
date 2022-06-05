from time import sleep
from django.test import TestCase, Client
from faker import Faker
import urllib3
from selenium import webdriver
import unittest

from . import factories

RECORD_COUNT = 1

fake = Faker()
fake = Faker(locale="Ru_ru")

def create_fake_data():
    data = []
    for i in range(RECORD_COUNT):
        data.append({
            "category_name": fake.name()
        })
    return data

class FFirstTest(TestCase):
    def setUp(self) -> None:
        pass
    
    def test_connection(self):
        http = urllib3.PoolManager()
        url = 'http://192.168.31.211:8000/api/v1/categorylist/'
        resp = http.request('GET', url)
        self.assertEqual(resp.status, 200)
        
        
        
class FirstTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.fakes = create_fake_data()
        
    def test_append_new_category(self):
        for f in self.fakes:             
            try:
                self.client.post("/api/v1/categorylist/", f)
            except:
                self.assertTrue(False)
    
        self.assertTrue(True)
    
    def test_with_factory_boy(self):
        product = factories.ProductFactory.build()
        print(product)
        
        try:
            self.client.post("/api/v1/productlist/", product)
        except:
            self.assertTrue(False)
            
        self.assertTrue(True)

    
    def test_get_all(self):
        response = self.client.get("/api/v1/categorylist/")
        content = response.data
        print(response)
        print(content)
    
    def tearDown(self):
        pass
    

class SelenumuTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_run_check_admin(self):
        driver = webdriver.Firefox()
        driver.get('http://192.168.31.211:8000/admin')
        
        try:
            login_element = driver.find_element_by_id("id_username")
        except:
            driver.close()
            self.assertTrue(False)
            
        try:
            pass_element = driver.find_element_by_id("id_password")
        except:
            driver.close()
            self.assertTrue(False)
            
        try:
            # click_element = driver.find_element_by_xpath("input[type='submit']")
            click_element = driver.find_element_by_xpath("//input[@type='submit']")
        except:
            driver.close()
            self.assertTrue(False)
        
        sleep(2)
        login_element.send_keys('kali')
        pass_element.send_keys('kali')
        
        sleep(2)
        click_element.click()
        
        sleep(2)
        driver.close()
        self.assertTrue(True)