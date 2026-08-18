from playwright.sync_api import TimeoutError
class Login:
    def __init__(self, page: object) -> None:
        self.page = page



    def logar_usuario(self):
        try:
            self.page.get_by_role("textbox", name="Informe seu login").fill("gustavo.batista")
            self.page.get_by_role("textbox", name="Informe seu login").press("Tab")
            self.page.get_by_role("textbox", name="Informe sua senha").fill("@cert2022G")
            self.page.get_by_role("button", name="Entrar").click()
            self.page.get_by_role("textbox", name="Busque por Código do Cliente").wait_for(timeout=5000)
            print("Login realizado com sucesso.")
        except TimeoutError:
            print("Falha ao realizar login.")