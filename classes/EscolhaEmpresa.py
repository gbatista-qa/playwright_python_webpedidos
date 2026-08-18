class EscolhaEmpresa:
    def __init__(self, page, empresa):
        self.page = page
        self.empresa = empresa

    def escolha_Empresa(self):
        self.page.locator(f"#empCodigo_{self.empresa}").click()# Acesso ao cliente