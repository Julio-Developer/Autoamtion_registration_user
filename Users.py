# This program is used to automate the access creation process for the implementation of users and their departments.

'''
This schedule must:

- open google
- open the website
- Login
- access the departments tab
- include the departments that are inside a csv
'''

# Impoting libraries
from sys import path_hooks
from time import sleep as sl
from attr import s
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

# -----------------------------------------------

# Date of site

# Path to the chromedriver
path_webdriver = ("/home/julio/Documentos/Projeto Cical/Departamentos/chromedriver")

# Website
web_site = ("https://grupocical.xpro.me/")

# Login and password
login = ('julio@xvisiontecnologia.com.br')
password = ('xvision123')

# Date of login
camp_login = ("txtemail")
camp_password = ("txtpassword")

# Login button
btn_login = ('//*[@id="login"]/div/div/button')

# Data for adminitrative routines
adm = ('//*[@id="nav-accordion"]/li[8]/a')

# Data for users
users = ('//*[@id="nav-accordion"]/li[8]/ul/li[1]/a')

# Button to create users
btn_create_user = ('//*[@id="editable-sample_new"]')

# Camp name
camp_name = ('//*[@id="nome"]')

# Camp email
camp_email = ('//*[@id="email"]')

# Office
offc = ('//*[@id="cargo"]')

# Offices
attendant = ('//*[@id="cargo"]/option[2]')
manager = ('//*[@id="cargo"]/option[3]')
master = ('//*[@id="cargo"]/option[4]')

# Password
camp_password = ('//*[@id="senha"]')
camp_confirm_password = ('//*[@id="csenha"]')

# Button to include the user
btn_include_user = ('//*[@id="form-novousuario"]/div/div/div[3]/button[2]')
# -----------------------------------------------

# Opening the browser
driver = wd.Chrome(path_webdriver)
sl(1)
driver.get(web_site)
sl(1)

# Login
driver.find_element('name', camp_login).send_keys(login)
sl(0.5)
# Password
driver.find_element('name', camp_password).send_keys(password)
sl(0.5)

# Login button
driver.find_element('xpath', btn_login).click()
sl(1)

# Finding the adminstrative routine
driver.find_element('xpath', adm).click()
sl(0.5)

# Finding the users
driver.find_element('xpath', users).click()
sl(0.5)

# Insert users
driver.find_element('xpath', btn_create_user).click()