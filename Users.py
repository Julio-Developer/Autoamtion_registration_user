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
from time import sleep as sl
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import pandas as pd

# -----------------------------------------------

# Date of site

# Path to the chromedriver
path_webdriver = ("/home/julio/Documentos/Projeto Cical/Users/chromedriver")

# Website
web_site = ("https://grupocical.xpro.me/")

# Login and password
login = ('julio@xvisiontecnologia.com.br')
password = ('xvision123')

# Date of login
camp_login = ('//*[@id="login"]/input')
camp_password = ('//*[@id="exampleInputPassword2"]')

# Login button
btn_login = ('//*[@id="login"]/div/div/button')

# Data for adminitrative routines
adm = ('//*[@id="nav-accordion"]/li[9]/a')

# Data for users
users = ('//*[@id="nav-accordion"]/li[9]/ul/li[1]/a')

# Button to create users
btn_create_user = ('//*[@id="editable-sample_new"]')

# Camp name
camp_name_usr = ("nome")

# Camp email
camp_email_usr = ("email")

# Office
offc = ('//*[@id="cargo"]')

# Offices
attendant = ('//*[@id="cargo"]/option[2]')
supervisor = ('//*[@id="cargo"]/option[5]')
master = ('//*[@id="cargo"]/option[4]')

# Password
camp_password_usr = ('//*[@id="senha"]')
camp_confirm_password_usr = ('//*[@id="csenha"]')

# Button to include the user
btn_include_user = ('//*[@id="form-novousuario"]/div/div/div[3]/button[2]')
# -----------------------------------------------

# Opening the browser
driver = wd.Chrome(path_webdriver)
sl(1)
driver.get(web_site)
sl(1)

# Login
driver.find_element('xpath', camp_login).send_keys(login)
sl(1)
# Password
driver.find_element('xpath', camp_password).send_keys(password)
sl(1)

# Login button
driver.find_element('xpath', btn_login).click()
sl(1)

# Finding the adminstrative routine
driver.find_element('xpath', adm).click()
sl(1)

# Opening the users tab
sheet = pd.read_excel('/home/julio/Documentos/Projeto Cical/Users/Usuarios.xlsx')

# Structure of insert data
count = 0
for i, nome in enumerate(sheet['nome']):
    total = 4
    count += 1
    email = sheet.loc[i, 'email']
    office = sheet.loc[i, 'cargo']
    password = sheet.loc[i, 'senha']
    sl(0.5)

    # Finding the users
    driver.find_element('xpath', users).click()
    sl(1)
    driver.find_element('xpath', btn_create_user).click()
    sl(1)

    # Creating the user
    driver.find_element('name', camp_name_usr).send_keys(nome)
    sl(0.5)
    driver.find_element('name', camp_email_usr).send_keys(email)
    sl(0.5)
    driver.find_element('xpath', offc).click()
    sl(0.5)

    # Selecting the office
    if office == 'Atendentes':
        driver.find_element('xpath', attendant).click()
    elif office == 'Supervisor':
        driver.find_element('xpath', supervisor).click()
    elif office == 'Master':
        driver.find_element('xpath', master).click()
    sl(0.5)

    # Password
    driver.find_element('xpath', camp_password_usr).send_keys(password)
    sl(0.5)
    driver.find_element('xpath', camp_confirm_password_usr).send_keys(password)
    sl(0.5)

    # Insert users
    driver.find_element('xpath', camp_confirm_password_usr).send_keys(Keys.ENTER)
    sl(1)
    # checking what has already been registered what is missing
    print(f'{count}/{total}')
    print(f'{nome} - {email} - {office} - {password}')