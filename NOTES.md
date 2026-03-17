# Exercício Bookstore

## Sobre o Projeto

Este arquivo documenta o exercício acadêmico de desenvolvimento de uma API REST para gerenciamento de uma livraria (bookstore), implementada com Django e Django REST Framework.

---

## 🛠 Tecnologias e Ferramentas Utilizadas

- **Python** - Linguagem de programação principal
- **Django** - Framework web
- **Django REST Framework** - Framework para criação de APIs REST
- **Poetry** - Gerenciamento de dependências e ambiente virtual
- **Pytest + Pytest-Django** - Framework para testes automatizados
- **SQLite** - Banco de dados para desenvolvimento
- **Factory Boy** - Geração de dados para testes

---

##  Escopo do Projeto

### Apps Principais

####  Order (Pedidos)
- **Models**: Modelo de pedidos com relacionamentos
- **Serializers**: Serialização de dados de pedidos
- **ViewSets**: Endpoints para CRUD de pedidos
- **Tests**: Testes automatizados de models, serializers e viewsets

####  Product (Produtos)
- **Models**: 
  - `Product` - Modelo de produtos
  - `Category` - Modelo de categorias
- **Serializers**: Serialização de produtos e categorias
- **ViewSets**: Endpoints para CRUD de produtos e categorias
- **Tests**: Testes automatizados de models, serializers e viewsets

---

##  Funcionalidades Implementadas

### Relacionamentos entre Entidades
- **OneToMany**: Usuário → Pedidos
- **ManyToMany**: 
  - Pedidos ↔ Produtos
  - Produtos ↔ Categorias

### Serialização de Dados
- Serialização para APIs REST
- Serialização aninhada (nested serialization)
- Campos de leitura e escrita separados
- Validação de dados de entrada

### Testes Automatizados
- ✅ Testes de models
- ✅ Testes de serializers
- ✅ Testes de viewsets (GET, POST)
- ✅ Testes de autenticação (Token)
- ✅ Uso de factories para geração de dados

### Regras de Negócio
- Integridade referencial entre entidades
- Validações de campos obrigatórios
- Autenticação via Token para endpoints protegidos

---

##  Estrutura de Testes
```
bookstore/
├── order/
│   └── tests/
│       ├── test_serializers/
│       │   └── test_order_serializer.py
│       └── test_viewsets/
│           └── test_order_viewset.py
└── product/
    └── tests/
        ├── test_serializers/
        │   ├── test_category_serializer.py
        │   └── test_product_serializer.py
        └── test_viewsets/
            ├── test_category_viewset.py
            └── test_product_viewset.py
```

---

##  Status do Projeto

- [x] Models implementados
- [x] Serializers implementados
- [x] ViewSets implementados
- [x] Testes automatizados funcionando
- [x] Autenticação via Token
- [x] Relacionamentos configurados
- [x] Validações implementadas

---

##  Como Executar os Testes
```bash
# Executar todos os testes
poetry run python manage.py test

# Executar testes de um app específico
poetry run python manage.py test product
poetry run python manage.py test order

# Executar com verbosidade
poetry run python manage.py test --verbosity=2
```

---

##  Aprendizados

- Configuração de projeto Django com estrutura modular
- Implementação de testes automatizados com Django TestCase
- Uso de factories para geração de dados de teste
- Relacionamentos complexos em Django ORM
- Serialização aninhada no Django REST Framework
- Autenticação e permissões em APIs REST
- Debugging e correção de erros em testes

---

**Nota**: Este é um exercício acadêmico desenvolvido para fins educacionais.