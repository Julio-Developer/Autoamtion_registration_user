# -*- encoding: utf-8 -*-

# This programas modifies the passwords of the users.

# Impoting libraries
from importlib.resources import path
from lib2to3.pgen2 import driver
from time import sleep as sl
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import pandas as pd


# Date of site

# Acessing the file
file = pd.read_excel('/home/julio/Documentos/Projeto Cical/Users/senha.xlsx')

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

# Camp find user
camp_find_user = ('//*[@id="usuarios-table_filter"]/label/input')

# Button to modify the password
modify_password = ('//*[@id="usuarios-table"]/tbody/tr/td[6]/a[1]/i')

# Password
camp_password_usr = ('//*[@id="nsenha"]')
camp_confirm_password_usr = ('//*[@id="ncsenha"]')

# Button modify password
btn_modify_password_usr = ('//*[@id="form-novasenha"]/div/div/div[3]/button[2]')
# --------------------------------

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

# Finding the users
driver.find_element('xpath', users).click()
sl(1)

for i, nome in enumerate(file['nome']):
    password = file.loc[i, 'senha']
    total = 76
    # Finding the user
    driver.find_element('xpath', camp_find_user).send_keys(nome)
    sl(0.5)

    # Changing the password
    driver.find_element('xpath', modify_password).click()
    sl(0.5)

    # New password
    driver.find_element('xpath', camp_password_usr).send_keys(password)
    sl(0.5)
    driver.find_element('xpath', camp_confirm_password_usr).send_keys(password)
    sl(0.5)
    
    # Button to modify the password
    driver.find_element('xpath', btn_modify_password_usr).click()
    sl(0.5)
    driver.find_element('xpath', users).click()
    sl(0.5)

    # how many are the users
    print(f'{i}/{total}')
    print(f'Nome: {nome} - senha: {password}')
    print('Restante: ', total - i)