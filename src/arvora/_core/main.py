#! /usr/bin/env python
# -*- coding: UTF8 -*-
""" Ponto de entrada do módulo Arvora.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Classes neste módulo:
    - :py:class:`SimplePage` A page used as a base for the others.
    - :py:class:`LandingPage` Entry point for the platform.
    - :py:class:`LoginPage` User Registration page.
    - :py:class:`Arvora` Main class with the main functionality.
    - :py:func:`main` Called entry page to start the application.

Changelog
---------
.. versionadded::    24.03
   |br| first version of main (05)

|   **Open Source Notification:** This file is part of open source program **Arvora**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

"""
MENU_OPTIONS = tuple(zip("PROJETO CONHECIMENTO PESQUISA INTERAÇÃO LOGIN USER".split(),
                     "bars-progress book book-medical hands-asl-interpreting right-to-bracket user".split()))


class SimplePage:
    PAGES = dict()

    def __init__(self, brython, menu=MENU_OPTIONS, hero="none_hero"):
        _menu = [{"title": items, "icon": icons} for items, icons in menu]
        self.brython = brython
        self.hero_class = hero
        self.items = []
        self.page = self.hero(self.navigator(_menu))
        [item.bind("click", self.link) for item in self.items]

    def link(self, ev=None):
        ev.preventDefault()
        page = ev.target.id.strip("-")
        self.PAGES[page].show()

    def show(self):
        self.brython.document["pydiv"].html = ""
        _ = self.brython.document["pydiv"] <= self.page
        self.brython.document["_USER_-"].html = Arvora.ARVORA.current_user

    def build_body(self):
        return ()

    def hero(self, navigator):
        h = self.brython.html
        cnt = h.DIV(self.build_body(), Class="container has-text-centered pb-6 mgb-large")
        hby = h.DIV(cnt, Class="hero-body is-justify-content-center is-align-items-center")
        hea = h.DIV(navigator, Class="hero-head")
        sec = h.SECTION((hea, hby), Class=f"hero {self.hero_class} is-fullheight")
        return sec

    def navigator(self, menu):
        h = self.brython.html

        def do_item(title=None, icon=None):
            spn = h.SPAN(
                h.I(Class=f"fa fa-lg fa-{icon}", Id=f"-_{title}_-")+h.SPAN(title, Id=f"_{title}_-"),
                Class="icon-text", style="color: #333;", Id=f"-_{title}_--")
            return h.A(spn, Id=f"_{title}_", Class="navbar-item", href="./#")
        aim = h.IMG(src="/src/arvora/_media/arvora_ico.png", alt="Arvora", height="28", Id="_MAIN_-")
        arv = h.A(aim, Id="_MAIN_", Class="navbar-item", href="./")
        nbr = h.DIV(arv, Class="navbar-brand", Id="-_MAIN_-")
        self.items = [do_item(**item) for item in menu]
        end = h.DIV(self.items[-1], Class="navbar-end")
        self.items = items = [nbr]+self.items[:-1]+[end]
        nav = h.NAV(items, Class="navbar")
        fna = h.DIV(h.DIV(nav, Class="container"), Class="first_nav")
        return fna


class LandingPage(SimplePage):
    def __init__(self, brython, menu=MENU_OPTIONS):
        super().__init__(brython, menu, hero="main_hero")

    def build_body(self):
        h = self.brython.html
        tt1 = h.P("A R V O R A", Class="title main-text has-text-weight-bold")
        tt2 = h.P("Brain Computational School", Class="title is-1 main-text")
        return h.DIV((tt1, tt2))


class LoginPage(SimplePage):
    def __init__(self, brython, menu=MENU_OPTIONS):
        super().__init__(brython, menu, hero="main_hero")
        self.form = self.login = self.passd = None

    def click(self, ev=None):
        _ = self
        ev.preventDefault()
        form = ev.target
        # USER_OPTIONS = form.elements["username"].value
        Arvora.ARVORA.user(form.elements["username"].value)
        SimplePage.PAGES["_MAIN_"].show()

        # self.brython.alert(form.elements["username"].value, form.elements["password"])
        # print(self.login.value, self.passd.type)

    def build_body(self):
        h = self.brython.html
        btn = h.BUTTON("Login", Class="button is-primary is-fullwidth", type="submit")
        self.passd = h.INPUT(Id="password", Class="input is-primary", type="password", placeholder="Password")
        psw = h.DIV(h.LABEL("Password", For="Name")+self.passd, Class="field")
        self.login = h.INPUT(Id="username", Class="input is-primary", type="text", placeholder="Email address")
        eid = h.DIV(h.LABEL("Email", For="email")+self.login, Class="field")
        form = h.FORM((eid, psw, btn), Class="column is-4 box")
        form.bind("submit", self.click)

        cls = h.DIV(form, Class="columns is-flex is-flex-direction-column")
        return cls

class InteractionPage(SimplePage):
    #Adicionando o init
    def __init__(self, brython, menu=MENU_OPTIONS):
        super().__init__(brython, menu, hero="main_hero")
        self.form = self.text = None

    def click(self, ev=None):
        _ = self
        ev.preventDefault()
        form = ev.target
        # USER_OPTIONS = form.elements["username"].value
        Arvora.ARVORA.user(form.elements["username"].value)
        SimplePage.PAGES["_MAIN_"].show()

        # self.brython.alert(form.elements["username"].value, form.elements["password"])
        # print(self.login.value, self.passd.type)

    #construindo a página em si
    def build_body(self):
        h = self.brython.html

        #um botão para enviar o formulário
        btn = h.BUTTON("Enviar", Class="button has-background-grey-light is-4 block is-fullwidth", type="submit")

        #O campo onde as pessoas pode escrever o texto delas, esse monte de tag é o bulma. Ela tem os placeholders e o rows que é a quantidade padrão de linhas
        self.text = h.TEXTAREA(Id="text", Class="textarea is-light has-fixed-size block mb-4 mt-0 has-background-grey has-text-success-light is-medium", rows='17', type="text", placeholder="Comece a escrever aqui!")

        #Aqui eu criei uma div para armazenar todos os componentes da página
        div = h.DIV()
            
        #tit == titulo. Esse é o título da página
        tit = h.H1("Escreva seu artigo", Class='title is-2 block hero p-2 has-text-white')

        #aut == autor. Aqui que a pessoa pode botar o nome dela ((só uma ideia inicial))
        aut = h.INPUT(placeholder='Autor', Id='input', Class='input is-light has-fixed-size block has-background-grey has-text-success-light is-medium')

        #Aqui eu to adicionando tudo dentro da div, na ordem que eu quero que eles aparecam
        div <= tit
        div <= aut
        div <= self.text

        #aqui eu encapsulei a div com tudo e o botão em um formulário
        form = h.FORM((div, btn), Class="column")
        form.bind("submit", self.click)

        #inte == interactions. aqui eu adicionei tudo isso em outra div
        inte = h.DIV(form, Class="columns is-flex")
        #Aqui eu to retornando a div com todos os elementos
        return inte

class Arvora:
    ARVORA = None

    def __init__(self, br):
        self.users = dict(ADMIN="admin", USER="user")
        self.brython = br
        self.current_user = None
        Arvora.ARVORA = self

    def user(self, current_user):
        self.current_user = current_user

    def start(self):
        br = self.brython
        SimplePage.PAGES = {f"_{page}_": SimplePage(br) for page, _ in MENU_OPTIONS}
        SimplePage.PAGES["_MAIN_"] = LandingPage(br)
        SimplePage.PAGES["_LOGIN_"] = LoginPage(br)
        SimplePage.PAGES['_INTERAÇÃO_'] = InteractionPage(br)
        _main = LandingPage(br)
        _main.show()
        return _main


def main(br):
    return Arvora(br).start()
