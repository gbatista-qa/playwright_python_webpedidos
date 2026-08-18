from playwright.sync_api import TimeoutError
class AcessoSite:
    def __init__(self, page):
        self.page = page



    def acesso_site(self):
        try:
            self.page.goto("https://webpedidos.grupoacert.com.br/auth/login?acesso=qa-cloud&sistema=acert")
            self.page.get_by_role("textbox", name="Informe seu login").wait_for(timeout=5000)
            print("Acesso ao site realizado com sucesso.")
        except TimeoutError:
            print("Não foi possível acessar o site.")
