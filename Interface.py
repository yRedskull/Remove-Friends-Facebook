from tkinter import *
from tkinter.ttk import Combobox
import os
from tkinter import messagebox as mb
from run import Run
from time import sleep as sl
# Class/Def
class Interface:
    back_gr = '#242526'
    fore_gr = '#E4E6EB'
    font_si = ('Inherit', 16)

    def __init__(self):
        # Colors:
        # Preto: #242526 / #202122
        # Azul: #3982E4
        # Branco: #E4E6EB

        # Var
        self.cb_names = None
        self.frame = None
        self.list_names_nr = list()
        self.url = None
        self.lb_init = None
        self.lb_password = None
        self.lb_email = None
        self.lb_obs = None
        self.lb_url = None
        self.lb_run = None
        self.lb_list_names = None
        self.btn_next = None
        self.btn_back = None
        self.btn_remove_l_n = None
        self.btn_url = None
        self.btn_run = None
        self.btn_add_l_n = None
        self.ent_password = None
        self.ent_url = None
        self.ent_email = None
        self.nome = os.getlogin()
        self.init = f"""Olá {self.nome}, clique no botão abaixo para começarmos."""
        self.obs = f"""Esse programa serve para remover amigos no Facebook sem enrolação. 
Nenhum dos seus dados serão armazenados para fora do ambiente.
Atenção: Você precisará ter o Google Chrome instalado em sua máquina
para rodar esse programa."""

        # Tela
        self.app = Tk()

        # Pictures
        self.img_logo = PhotoImage(file='Image/logo.png').subsample(1)
        self.img_next = PhotoImage(file='Image/next.png').subsample(1)
        self.img_play = PhotoImage(file='Image/play.png').subsample(1)
        self.img_back = PhotoImage(file='Image/back.png').subsample(2)
        self.img_add = PhotoImage(file='Image/add.png').subsample(1)
        self.img_remove = PhotoImage(file='Image/remove.png').subsample(1)

        # Config
        self.app.title('Facebook - Remove Friends')
        self.app.configure(background='#242526')
        self.app.iconphoto(False, self.img_logo)

        # Resolution
        self.width_screen = self.app.winfo_screenwidth()
        self.height_screen = self.app.winfo_screenheight()
        width_plus = int((600 * self.width_screen) / 1920)
        height_plus = int((300 * self.height_screen) / 1080)
        self.app.geometry(f"600x400+{width_plus}+{height_plus}")
        self.app.resizable(False, False)

        # Run
        self.tela_init()

        self.app.mainloop()

    def tela_init(self, fog=fore_gr, bag=back_gr):

        self.frame = Frame(self.app, bg=bag)
        self.frame.pack(expand=True, fill=BOTH)
        self.lb_init = Label(self.frame, text=self.init, font=('Roboto', 16), bg=bag, fg=fog)
        self.lb_init.pack(side='top', padx=5, pady=20)

        def configbagcolor(event):
            self.btn_next.config(bg=bag)
            self.app.update()
            return event

        def configcolor(event):
            self.btn_next.config(bg='#202122')
            self.app.update()
            return event

        self.btn_next = Button(self.frame, image=self.img_play, command=self.tela_url, bg=bag, highlightthickness=0,
                               bd=0)
        self.btn_next.pack(ipady=10, ipadx=10, pady=50, padx=5)
        self.btn_next.bind('<Enter>', configcolor)
        self.btn_next.bind('<Leave>', configbagcolor)

        self.lb_obs = Label(self.frame, text=self.obs, font=('Roboto', 11), fg=fog, bg=bag)
        self.lb_obs.pack(side='bottom', ipady=2)

    def tela_url(self, bag=back_gr, fog=fore_gr):
        def voltar_tela_init():
            self.frame.destroy()
            self.btn_back.destroy()
            self.app.update()
            self.tela_init()

        def key_press_ent(event):
            if event.keysym == 'Return':
                self.tela_login()
            elif event.keysym == 'Escape':
                voltar_tela_init()
            else:
                pass

        self.frame.destroy()
        self.app.update()

        self.frame = Frame(self.app, bg=bag)
        self.frame.pack(expand=True, fill=BOTH)

        self.lb_url = Label(self.frame, text='Digite o endereço completo de sua página de Amigos no Facebook.', bg=bag,
                            fg=fog, font=('Roboto', 14))
        self.lb_url.pack(ipadx=100, ipady=20, side='top')

        self.ent_url = Entry(self.frame, bg='#E4E6EB', fg=bag, font=('Arial', 12))
        self.ent_url.pack(ipadx=160, ipady=4)
        self.ent_url.bind('<Key>', key_press_ent)
        if self.url:
            self.ent_url.insert(0, self.url)

        def configbagcolor(event):
            self.btn_url.config(bg=bag)
            self.app.update()
            return event

        def configcolor(event):
            self.btn_url.config(bg='#202122')
            self.app.update()
            return event

        self.btn_url = Button(self.frame, image=self.img_next, fg=fog, bg=bag, highlightthickness=0, bd=0,
                              command=self.tela_login)
        self.btn_url.pack(ipady=10, ipadx=10, pady=5)
        self.btn_url.bind('<Enter>', configcolor)
        self.btn_url.bind('<Leave>', configbagcolor)

        self.lb_obs = Label(self.frame, text=self.obs, font=('Roboto', 11), fg=fog, bg=bag)
        self.lb_obs.pack(side='bottom', ipady=2)

        def configbagcolor(event):
            self.btn_back.config(bg=bag)
            self.app.update()
            return event

        def configcolor(event):
            self.btn_back.config(bg='#202122')
            self.app.update()
            return event

        self.btn_back = Button(self.app, image=self.img_back, bg=bag, highlightthickness=0, bd=0,
                               command=voltar_tela_init)
        self.btn_back.pack(side='left', padx=3, pady=3, ipadx=2, ipady=2)
        self.btn_back.bind('<Enter>', configcolor)
        self.btn_back.bind('<Leave>', configbagcolor)

    def tela_login(self, bag=back_gr, fog=fore_gr):
        def voltar_tela_url():
            self.frame.destroy()
            self.btn_back.destroy()
            self.app.update()
            self.tela_url()

        def add_list_names():
            if self.cb_names.get() in self.list_names_nr:
                mb.showwarning(message=f'"{self.cb_names.get()}" ja foi adicionado a lista!')
                self.cb_names.set('')
            elif self.cb_names.get() == '':
                mb.showwarning(message='Preencha o campo antes de adicionar!')
            elif '"' in self.cb_names.get() or "'" in self.cb_names.get(
            ) or r"!@#$%¨&*()_+{}[]/?|\?" in self.cb_names.get():
                mb.showwarning(message='Não aceitamos caracteres especiais!!!')
            else:
                self.list_names_nr.append(self.cb_names.get())
                self.cb_names.config(values=self.list_names_nr)
                self.cb_names.set('')

            return self.app.update()

        def remove_list_names():
            if self.cb_names.get() in self.list_names_nr:
                self.list_names_nr.remove(self.cb_names.get())
                self.cb_names.config(values=self.list_names_nr)
                if len(self.list_names_nr) >= 1:
                    self.cb_names.set(self.list_names_nr[len(self.list_names_nr) - 1])
                else:
                    self.cb_names.set('')
                self.app.update()
            elif self.cb_names.get() == '':
                mb.showwarning(message='Selecione algum nome para retirar!')
            else:
                mb.showwarning(message=f'"{self.cb_names.get()}" não está na lista!')
                if len(self.list_names_nr) >= 1:
                    self.cb_names.set(self.list_names_nr[-1])
                else:
                    self.cb_names.set('')

            return self.app.update()

        def key_press_cb(event):
            if event.keysym == 'Return':
                add_list_names()
            elif event.keysym == 'Escape':
                remove_list_names()
            else:
                pass

        self.url = str(self.ent_url.get())

        if "https://www.facebook.com/" in self.url and self.url[-7:] == 'friends':
            self.frame.destroy()
            self.btn_back.config(command=voltar_tela_url)
            self.app.update()

            self.frame = Frame(self.app, bg=bag)
            self.frame.pack(expand=True, fill=BOTH)

            self.lb_list_names = Label(self.frame, text='''Digite corretamente o nome das pessoas que deseja manter.
Respeitando letras MAIÚSCULAS, minúsculas e espaços.''', bg=bag, fg=fog, font=('Roboto', 14))
            self.lb_list_names.pack(padx=5, pady=5, ipady=10, ipadx=5)

            self.cb_names = Combobox(self.frame, font=('Inherit', 13), background=fog, foreground=bag,
                                     values=self.list_names_nr)
            self.cb_names.pack(ipadx=100, ipady=3, pady=3, padx=3)
            self.cb_names.bind('<Key>', key_press_cb)

            def configbagcolor(event):
                self.btn_add_l_n.config(bg=bag)
                self.app.update()
                return event

            def configcolor(event):
                self.btn_add_l_n.config(bg='#202122')
                self.app.update()
                return event

            self.btn_add_l_n = Button(self.frame, image=self.img_add, command=add_list_names, bg=bag, bd=0,
                                      highlightthickness=0)
            self.btn_add_l_n.pack(padx=5, pady=5)
            self.btn_add_l_n.bind('<Enter>', configcolor)
            self.btn_add_l_n.bind('<Leave>', configbagcolor)

            def configbagcolor(event):
                self.btn_remove_l_n.config(bg=bag)
                self.app.update()
                return event

            def configcolor(event):
                self.btn_remove_l_n.config(bg='#202122')
                self.app.update()
                return event

            self.btn_remove_l_n = Button(self.frame, image=self.img_remove, command=remove_list_names, bg=bag, bd=0,
                                         highlightthickness=0)
            self.btn_remove_l_n.pack(padx=5, pady=5)
            self.btn_remove_l_n.bind('<Enter>', configcolor)
            self.btn_remove_l_n.bind('<Leave>', configbagcolor)

            def configbagcolor(event):
                self.btn_next.config(bg=bag)
                self.app.update()
                return event

            def configcolor(event):
                self.btn_next.config(bg='#202122')
                self.app.update()
                return event

            self.btn_next = Button(self.frame, image=self.img_next, command=self.tela_run, bg=bag, highlightthickness=0,
                                   bd=0)
            self.btn_next.pack(ipady=10, ipadx=10, pady=50, padx=5, side='right')
            self.btn_next.bind('<Enter>', configcolor)
            self.btn_next.bind('<Leave>', configbagcolor)

        else:
            mb.showwarning(message='Digite um endereço válido!!!')
            self.app.update()

    def tela_run(self, bag=back_gr, fog=fore_gr):
        res = mb.askquestion(message='Deseja iniciar o procedimento?')
        if res == 'yes':
            self.frame.destroy()
            self.btn_back.destroy()
            self.app.update()

            self.lb_run = Label(self.app, text='Iniciando Procedimento...', bg=bag, fg=fog, font=('Arial', 18))
            self.lb_run.pack(ipadx=100, ipady=10, pady=5, padx=5)
            self.app.update()

            sl(1)
            try:
                run = Run()
                run.get_page(self.url)
                run.desamigar(self.list_names_nr)
            except Exception as e:
                print(Exception)
                self.lb_run.config(bg='#D00', text=f"""Algo deu errado!!! 
                {e}""")
        else:
            return

# Principal
Interface()
