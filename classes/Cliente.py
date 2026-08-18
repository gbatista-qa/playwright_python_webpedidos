class Cliente:

    def __init__(self, page, id_cliente):
        self.page = page
        self.id_cliente = id_cliente

    def acesso_cliente(self):
        self.page.get_by_role("textbox", name="Busque por Código do Cliente").click()
        self.page.get_by_role("textbox", name="Busque por Código do Cliente").fill(str(self.id_cliente))
        self.page.locator("a").filter(has_text=".str1 {stroke:#FEFEFE;stroke-").click()
        self.page.locator("#ui-id-6").click()
        self.page.wait_for_timeout(3000)
        self.page.locator("#pesquisaSimples").nth(1).click()

