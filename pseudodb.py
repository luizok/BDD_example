import dataclasses as datacls


class ItemNotFoundException(Exception):
    pass


class NoStockAvailableException(Exception):
    pass


@datacls.dataclass
class Product:

    name: str
    quantity: int


@datacls.dataclass
class PseudoDatabase:

    dbname: str = 'Default Name'
    products: dict = datacls.field(default_factory=dict)

    def add_product(self, item: Product) -> None:

        self.products.update({item.name: item})

    def list_products(self) -> list:

        return self.products.keys()

    def is_product_available(self, product_name: str) -> bool:

        try:
            _ = self.products[product_name]
            return True
        except KeyError:
            return False

    def stock_size(self, product_name: str) -> bool:

        if not self.is_product_available(product_name):
            raise ItemNotFoundException(f'O item {product_name} não está disponível')

        if self.is_product_available(product_name):
            return self.products[product_name].quantity

        return False

    def sell_product(self, product_name: str, quantity: int = 1) -> None:

        if self.stock_size(product_name) >= quantity:
            self.products[product_name].quantity -= quantity

        raise NoStockAvailableException(f'Não há estoque disponível para {product_name}')
