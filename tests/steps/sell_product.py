import behave as bdd

import pseudodb as pdb


@bdd.fixture
def setup_db(context):

    db = pdb.PseudoDatabase()
    context.db = db
    context.exception = None

    return context


@bdd.given('Um estoque de {quantity:d} {product:w}')
def _(context, quantity, product):

    context.db.add_product(pdb.Product(product, quantity))


@bdd.when('Cliente solicita {quantity:d} {product:w}')
def _(context, quantity, product):

    try:
        context.db.sell_product(product)
    except Exception as e:
        context.exception = e


@bdd.then('Estoque de bananas deve conter {quantity:d} {product:w}')
def _(context, quantity, product):

    assert context.db.stock_size(product) == 1


@bdd.then('Gerar erro avisando a indisponibilidade de estoque')
def _(context):

    assert isinstance(context.exception, pdb.NoStockAvailableException)


@bdd.given('Estoque não possui o produto {product:w}')
def _(context, product):

    assert product not in context.db.list_products()


@bdd.then('Gerar erro avisando a inexistência do produto no catálogo')
def _(context):

    assert isinstance(context.exception, pdb.ItemNotFoundException)
