# Automação de Testes E2E com Playwright e Python

Projeto de automação de testes end-to-end (E2E) desenvolvido com **Python, Playwright e Pytest**, com foco na validação automatizada de fluxos de um sistema web.

O projeto utiliza o padrão **Page Object Model (POM)** para organizar os elementos e comportamentos das páginas, facilitando a manutenção, reutilização e evolução dos testes.

## 🚀 Tecnologias utilizadas

* **Python**
* **Playwright**
* **Pytest**
* **pytest-playwright**
* **Git/GitHub**
* **HTML/CSS/JavaScript** — interação com aplicação web
* **API REST** — quando aplicável aos cenários de teste

## 📁 Estrutura do projeto

```text
playwright_python/
│
├── classes/
│   ├── Login.py
│   ├── Cliente.py
│   ├── TipoPedido.py
│   └── ...
│
├── tests/
│   ├── test_primeiro.py
│   ├── test_pedido_atacado.py
│   ├── test_pedido_laboratorio_multifocal.py
│   └── ...
│
├── .gitignore
├── requirements.txt
└── README.md
```

### `classes/`

Contém as classes responsáveis pela interação com as diferentes partes do sistema.

Exemplos:

* `Login.py` — realiza o processo de autenticação.
* `Cliente.py` — realiza a seleção/acesso ao cliente.
* `TipoPedido.py` — seleciona o tipo de pedido.
* Outras classes podem ser adicionadas conforme novos fluxos são automatizados.

### `tests/`

Contém os testes automatizados utilizando **Pytest**.

Os testes utilizam as classes do diretório `classes/` para executar os fluxos do sistema.

## 🧩 Page Object Model

O projeto utiliza o padrão **Page Object Model (POM)**.

A ideia é separar:

**Teste**

```python
login = Login(page)
login.acessar()

cliente = Cliente(page, id_cliente)
cliente.acesso_cliente()
```

da implementação dos elementos da página:

```python
class Login:

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("URL_DO_SISTEMA")
```

Isso evita que os testes fiquem diretamente dependentes dos detalhes dos elementos da interface.

### Benefícios

* Maior reutilização de código
* Melhor organização
* Manutenção mais simples
* Redução de duplicidade
* Maior legibilidade dos testes
* Facilidade para adicionar novos cenários

## ⚙️ Instalação

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entrar no diretório:

```bash
cd playwright_python
```

### 2. Criar ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Instalar os navegadores do Playwright

```bash
playwright install
```

## ▶️ Executando os testes

Para executar todos os testes:

```bash
pytest
```

Para executar um teste específico:

```bash
pytest tests/test_pedido_atacado.py
```

Para executar visualizando o navegador:

```bash
pytest --headed
```

Para executar utilizando um navegador específico:

```bash
pytest --headed --browser=chromium
```

Também é possível executar um teste específico:

```bash
pytest --headed --browser=chromium tests/test_pedido_atacado.py
```

## 🔎 Debug dos testes

O Playwright permite pausar a execução utilizando:

```python
page.pause()
```

Exemplo:

```python
def test_pedido(page):

    login = Login(page)
    login.acessar()

    page.pause()
```

Ao executar o teste em modo `headed`, o Playwright abrirá o Inspector, permitindo analisar os elementos da página e os locators utilizados.

## 🧪 Estratégia de automação

Os testes são estruturados buscando validar fluxos reais de utilização do sistema.

Entre os fluxos automatizados estão:

* Login
* Acesso ao cliente
* Seleção do tipo de pedido
* Seleção de produtos
* Seleção de lentes
* Preenchimento de quantidades
* Adição de produtos ao carrinho
* Criação de pedidos
* Fluxos específicos de pedidos atacado
* Fluxos de pedidos para laboratório

Novos cenários podem ser adicionados conforme a evolução do projeto.

## 🎯 Objetivos do projeto

O projeto tem como principais objetivos:

* Automatizar testes repetitivos;
* Reduzir o esforço de testes manuais;
* Aumentar a cobertura dos testes;
* Identificar regressões com maior rapidez;
* Validar fluxos críticos da aplicação;
* Facilitar a execução dos testes de regressão;
* Criar uma estrutura escalável de automação.

## 📌 Boas práticas utilizadas

### Locators

Priorizar locators estáveis e baseados na semântica da aplicação:

```python
page.get_by_role("button", name="Entrar")
```

ou:

```python
page.get_by_text("Atacado", exact=True)
```

Em situações específicas, utilizar:

```python
page.locator("#id_elemento")
```

### Reutilização

Funcionalidades utilizadas por vários testes devem ser encapsuladas em classes ou métodos reutilizáveis.

### Separação de responsabilidades

Os testes devem representar **o que está sendo validado**, enquanto as classes do Page Object devem concentrar **como interagir com a aplicação**.

## 📈 Próximos passos

Possíveis evoluções para o projeto:

* [ ] Implementar geração de relatórios HTML
* [ ] Adicionar evidências/screenshots em caso de falha
* [ ] Implementar execução em diferentes browsers
* [ ] Criar fixtures compartilhadas
* [ ] Melhorar gerenciamento de dados de teste
* [ ] Implementar testes de API
* [ ] Integrar com CI/CD
* [ ] Executar testes automaticamente através do GitHub Actions
* [ ] Adicionar testes paralelos
* [ ] Melhorar tratamento de logs
* [ ] Aumentar cobertura dos fluxos críticos

## 👨‍💻 Autor

**Gustavo Batista**

Projeto desenvolvido para prática e evolução em **Quality Assurance (QA), automação de testes e desenvolvimento de software**, utilizando Python, Playwright e Pytest.

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório.
