from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

handle = ['C-_-Devil_Code', 'infinito_', 'Sizzlk', 'Mystic_AN', 'G.O.K.U_Instinct', 'Code_with_guitar', 'fake_name', 'sharma2908', '_AbRn_', 'Palak137', 'hope_09', 'beastslayer123', 'RKansujia', 'Rockrun', 'Sehrawat_27', '_007CodeSpine', 'jhonsnow456', 'Arkenite03', 'rahul11134', 'ninja-nick-s', 'code-fox', 'RDX_2.O', 'RKansujia', 'Deepak_23', 'kumaraayush33548@gmail.com', 'Gopu_GPS', '_Np_nG', 'null_pointer_1', 'Decoder_j', '_hecxoc', 'Dense-Eclipse', '_Stack_2.0_', '_bagga', 'sashae', 'TheHavoc', 'bheron_4407', 'enlightrahulrm333', '_Cheeku', 'i_arushi_r', 'A_after_B', 'cnarte', 'devilbro', 'Night_Fury007', 'shivam_2310', '_hagemaru', 'Brainic', 'irshad2001', 'ajaysinghrr77', 'ducut', 'pinocchio_007', 'raviii_36', 'Arry_23', 'Py21Coder_J_V', '__J.HIND__', 'kevin_debruyne', 'I_Am_Vengeance4699', '__Brahmastra__']

chrome_driver_path = "C:\VAAB-progm\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://codeforces.com/")

log_in_1="termi.9929@gmail.com"
pass_1="L8R3?+n//T-Sp%d"

log_in_2="termi9.929@gmail.com"
pass_2=",$XTE8_p5ajmSWb"

time.sleep(2)

enter=driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/a[1]')
enter.click()

time.sleep(2)

print('done')

mail=driver.find_element_by_xpath('//*[@id="handleOrEmail"]')
mail.send_keys(log_in_2)

passw=driver.find_element_by_xpath('//*[@id="password"]')
passw.send_keys(pass_2)

login=driver.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input')
login.click()


for i in handle:
    time.sleep(2)
    name=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[5]/form/input[2]')
    name.send_keys(i)
    name.send_keys(Keys.ENTER)
    try:
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[6]/div[1]/div/a/img').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[5]/div[2]/div/h1/img').click()
    except:
        print(i)
        continue



