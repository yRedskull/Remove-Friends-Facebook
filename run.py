from commands import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep as sl
from selenium.webdriver.common.keys import Keys


class Run:
    def __init__(self):
        # Var
        self.html_find = None
        self.list_elements = None
        self.cmd = Commands()
        servico = Service(ChromeDriverManager().install())
        self.nv = webdriver.Chrome(service=servico)
        self.nv.maximize_window()
        self.list_friends = list()
        # lista com os nomes não retirados
        self.list_names = list()
        # lista com os nomes retirados
        self.list_del_names = list()

    def get_page(self, url):
        def request_login():
            while True:
                html_find = self.nv.find_element('tag name', 'html')
                html_class = html_find.get_attribute('class')
                if html_class.strip() != 'tinyViewport tinyWidth' and '_9dls' in html_class.strip():
                    break
                sl(2)
            return html_find

        def season_scroll():
            while True:
                # Rolando o Scroll até o final para pegar todos os amigos
                screen_init = self.nv.execute_script('return document.body.scrollHeight')
                self.cmd.scroll_down(screen_init=screen_init, nv=self.nv, html=self.html_find,
                                     Keys=Keys)

                self.list_elements = self.nv.find_elements('class name',
                                                           'x6s0dn4.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1olyfxc.x9f619'
                                                           + '.x1e56ztr.x1gefphp.xyamay9.x1pi30zi.x1l90r2v.x1swvt13')
                if len(self.list_elements) != 0 and len(self.list_elements) != 16:
                    break
                else:
                    continue
            sl(2)

        # Abrindo site no navegador Chrome
        self.nv.get(url)
        sl(5)

        # Esperando o usuário acessar sua conta no Facebook
        self.html_find = request_login()
        return season_scroll()

    def desamigar(self, list_names_nr):  # url:endereço, list_names_nr: lista de nomes que não podem ser removidos
        list_btn = self.nv.find_elements('class name',
                                         'xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x10w6t97.x1td3qas.xjbqb8w')
        # Removendo o primeiro btn que não é de nenhuma pessoa
        list_btn.pop(0)

        print(len(self.list_elements))
        remove_grupos(list_elem=self.list_elements, list_btn=list_btn)
        print(len(self.list_elements))

        for num in range(0, len(list_btn)):
            try:
                self.nv.execute_script(f'window.scrollTo(0, 100)')
                list_btn[num].click()
                sl(0.2)
                list_menuitem = self.nv.find_elements('class name', 'x1n2onr6.x16tdsg8.x1ja2u2z.x6s0dn4.x1y1aw1k'
                                                      + '.x1sxyh0.xwib8y2.xurb0ha')
                if len(list_menuitem) != 0:
                    for item in list_menuitem:
                        if item.text == 'Desamigar':
                            item.click()
                            name = self.nv.find_element('class name', 'x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv'
                                                        + '.xuxw1ft.x1120s5i')
                            if name.text[9:].strip() not in list_names_nr:
                                print(f'"{name.text[9:].strip()}" - Não está em "list_name_nr"')
                                confirm_delete = self.nv.find_element('css selector', '.x1u72gb5')
                                confirm_delete.click()
                                self.list_del_names.append(name.text[9:].strip())
                                break
                            else:
                                print(f'"{name.text[9:].strip()}" - Está em "list_name_no_remove"')
                                confirm_list = self.nv.find_elements('class name', 'x9f619.x1n2onr6.x1ja2u2z.x78zum5'
                                                                     + '.xdt5ytf.x2lah0s.x193iq5w.x1r8uery.xl9nvqe'
                                                                     + '.x17ot9bj')
                                for confirm in confirm_list:
                                    if confirm.text == 'Cancelar':
                                        confirm_cancel = confirm
                                        confirm_cancel.click()
                                        self.list_names.append(name.text[9:].strip())
                                    else:
                                        continue
                sl(0.1)
            except Exception:
                elem_split = self.list_elements[num].text.split('\n')
                print(f"Não foi possível clicar nas configurações do nome {elem_split[0]}")
        self.nv.quit()

