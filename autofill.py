from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

idAdmin = "itpeeps_pemira"
passAdmin = "itpemira"

driver_path = ".\webdriver\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://pemira.km.itb.ac.id/login/nonina")

field_id = driver.find_element_by_id("username")
field_pass = driver.find_element_by_id("password")
login_btn = driver.find_element_by_class_name("details-btn")

field_id.send_keys(idAdmin)
field_pass.send_keys(passAdmin)
login_btn.click()

time.sleep(2)
if('profil' in driver.current_url):
    driver.get("https://pemira.km.itb.ac.id/admin/users")
    cnka_username = "paparoy"
    cnka_pass = "hehe123"
    cnka_nama = "andiko"
    cnka_url_foto = "#"
    cnka_email = "andiko@gmail.com"
    cnka_noHp = "123456789"
    cnka_fakultas = "akmil"
    cnka_jurusan = "manajemen perang"
    try:
        field_cnka_username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/input[1]")))
        field_cnka_pass = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/input[2]")))
        field_cnka_repass = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/input[3]")))
        field_cnka_nama = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/input[4]")))
        field_cnka_url_foto = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/input[5]")))
        field_cnka_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/input[6]")))
        field_cnka_noHp = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/input[7]")))
        field_cnka_fakultas = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/input[4]")))
        field_cnka_jurusan = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/input[5]")))
        btn_submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]/button")))

        field_cnka_username.send_keys(cnka_username)
        field_cnka_pass.send_keys(cnka_pass)
        field_cnka_repass.send_keys(cnka_pass)
        field_cnka_nama.send_keys(cnka_nama)
        field_cnka_url_foto.send_keys(cnka_url_foto)
        field_cnka_email.send_keys(cnka_email)
        field_cnka_noHp.send_keys(cnka_noHp)
        field_cnka_fakultas.send_keys(cnka_fakultas)
        field_cnka_jurusan.send_keys(cnka_jurusan)
        btn_submit.click()

    except Exception as e:
                print(e)