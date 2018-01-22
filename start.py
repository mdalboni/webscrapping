import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

#Metodo de inserção no banco
def insertData(source,data):    
    post_link = db[source]
    titles = ["Pagina","Localização HTML","Função","URL"]
    data = dict(zip(titles,data))
    post_link.insert_one(data).inserted_id
    
def webcrawler(url):
    try:
        browser.get(url)
        WebDriverWait(browser,8).until(EC.visibility_of_element_located((By.CLASS_NAME,"portalheader")))               
        mainitems =["conteudo","consultas","links","informacoes","nav_portal","menu-apoio-item"]
        links =[]
        for key in mainitems:
            print("Procurando por "+key+" em: "+url)
            complist = browser.find_elements_by_class_name(key)
            filter(complist,key,links)  
        return links                                   
    except TimeoutException:
        print('Sem conexao de internet, site fora do ar ou problemas no carregamento')     
    except Exception as ex:
        print('Algo errado não esta certo')
        print(ex)

def nextPage(url):      
    try:
        browser.get(url)
        WebDriverWait(browser,8).until(EC.visibility_of_element_located((By.CLASS_NAME,"portalheader")))               
        mainitems =["conteudo","consultas","links","informacoes","nav_portal","densa","menu-apoio-item"]
        list =[]
        for key in mainitems:
            print("Procurando por "+key+" em: "+url)
            complist = browser.find_elements_by_class_name(key)
            filter(complist,key,list)                                           
    except TimeoutException:
        print('Sem conexao de internet, site fora do ar ou problemas no carregamento')     
    except Exception as ex:
        print('NextPage: Algo errado não esta certo')
        print(ex)

def filter(complist,key,links):
    for i in range(len(complist)):
                rest = complist[i].find_elements_by_tag_name('a')
                texto = [x.text for x in rest]
                href = [x.get_attribute("href") for x in rest]
                for x,y in zip(texto,href):
                    if(len(x)>0):
                        scrapping = [url,key,x,y]
                        links.append(y)                
                        insertData("transparencia",scrapping)
    


browser= webdriver.Firefox()
url = 'https://www.portaldatransparencia.gov.br'

#Insira sua conexão com o MongoDB do atlas
client = pymongo.MongoClient("mongodb+srv://mdalboni:brasil317@cluster0-icka9.mongodb.net/brasil317")
db = client['brasil317']

#loop da lista de links retornado pelo crawler
linkslist = webcrawler(url)
for x in linkslist:    
    nextPage(x)
browser.quit()