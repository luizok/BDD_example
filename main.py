import pseudodb as pdb


def main() -> None:

    db = pdb.PseudoDatabase()
    prod_1 = pdb.Product('Banana', 1)
    prod_2 = pdb.Product('Gummy', 2)

    db.add_product(prod_1)
    db.add_product(prod_2)

    db.sell_product('Banana')
    db.sell_product('Gummy')
    db.sell_product('Gummy')
    db.sell_product('Banana')


if __name__ == '__main__':

    main()
