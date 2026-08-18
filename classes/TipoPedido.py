class TipoPedido:
    def __init__(self, page):
        self.page = page

    def selecionar_tipo(self, tipo_pedido=""):
        try:
            self.page.locator("div").filter(has_text=tipo_pedido).nth(4).click()

            print(f"Tipo do pedido '{tipo_pedido}' selecionado com sucesso")

        except TimeoutError:
            print(f"Não foi possível selecionar o tipo do pedido '{tipo_pedido}'")
