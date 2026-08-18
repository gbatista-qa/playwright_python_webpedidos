class SelecionarProdutosAtacado:
    def __init__(self, page):
        self.page = page

    def pesquisa_produtos_atacado(self, linha_produto=""):
        self.page.get_by_role("textbox", name="Pesquise o produto por código").click()
        self.page.wait_for_timeout(3000)  # Espera 3 segundos
        self.page.get_by_role("textbox", name="Pesquise o produto por código").fill(linha_produto)
        self.page.wait_for_timeout(3000)  # Espera 3 segundos
        produto = self.page.locator(f"#form_{linha_produto}")
        produto.wait_for(state="visible")
        produto.click()

    def selecionar_lentes_atacado(self, dioptria, quantidade):
        escolha = self.page.locator(f"#CSTVII{dioptria}")
        escolha.click()
        quantos = self.page.locator(f"#CSTVII{dioptria}")
        quantos.fill(str(quantidade))

    def add_carrinho(self):
        self.page.locator("div").filter(has_text=".fil0AddCarrinho {fill:var(--").click(force=True)
        self.page.locator("a.BtnAdicionarCarrinho").first.click(force=True)
        self.page.get_by_role("link", description="Adicionar ao Carrinho", exact=True).click(force=True)
        botao = self.page.get_by_role("button", name="Finalizar Pedido").first
        botao.wait_for(state="visible")
        botao.click()
        self.page.get_by_role("textbox", name="Solicitante*").click()
        self.page.get_by_role("textbox", name="Solicitante*").fill("testeplaywright")
        self.page.get_by_text("ENVIAR PEDIDO").click()
        self.page.get_by_role("button", name="FECHAMENTO").click()
        self.page.get_by_role("link", name="Fechar", exact=True).click()


