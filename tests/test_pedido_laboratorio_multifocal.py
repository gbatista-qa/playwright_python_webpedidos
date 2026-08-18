from pytest_playwright.pytest_playwright import page
from classes.Login import Login
from classes.AcessoSite import AcessoSite
from classes.Cliente import Cliente
from classes.ReceitaLaboratorio import ReceitaLaboratorio
from classes.TipoPedido import TipoPedido

def test_pedido_laboratorio_multifocal(page):
    login = Login(page)
    tipo_pedido = TipoPedido(page)
    acesso_site = AcessoSite(page)

    acesso_site.acesso_site() #Acesso ao site

    login.logar_usuario() #Digitar o usuario, senha e dar OK

    cliente = Cliente(page, 7) #Declarando o cliente

    cliente.acesso_cliente() #Acesso ao cliente

    tipo_pedido.selecionar_tipo(page,"Laboratório").click() #Tipo de pedido "Laboratorio"

    receita = ReceitaLaboratorio(page, "Teste Gustavo", "Teste113312121") #Informar solicitante e Ordem de Compra
    receita.digitar_pedido()
    page.pause()

