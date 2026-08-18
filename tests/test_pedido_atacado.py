from pytest_playwright.pytest_playwright import page
from classes.Login import Login
from classes.Cliente import Cliente
from classes.TipoPedido import TipoPedido
from classes.AcessoSite import AcessoSite
from classes.SelecionaProdutosAtacados import SelecionarProdutosAtacado
from classes.EscolhaEmpresa import EscolhaEmpresa

def test_pedido_atacado(page):
    login = Login(page)
    acesso_site = AcessoSite(page)
    cliente = Cliente(page, "7")  # Declarando o cliente
    escolha_empresa = EscolhaEmpresa(page, "1")
    tipo_pedido = TipoPedido(page)
    selecionar = SelecionarProdutosAtacado(page)

    acesso_site.acesso_site() #Acesso ao site

    login.logar_usuario() #Realizar o login

    cliente.acesso_cliente()
    escolha_empresa.escolha_Empresa()

    tipo_pedido.selecionar_tipo("Atacado") # Tipo de pedido "Atacado"
    selecionar.pesquisa_produtos_atacado(linha_produto="1436") #Digita a linha do produto na barra de pesquisa

        # Informa as lentes e suas quantidade
    selecionar.selecionar_lentes_atacado("3100D", "2")
    selecionar.selecionar_lentes_atacado("3100E", "3")
    selecionar.selecionar_lentes_atacado("2100E", "10")

    selecionar.add_carrinho() #Adiciona produtos ao carrinho e finaliza o pedido

    page.pause()


