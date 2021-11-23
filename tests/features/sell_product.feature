Feature: Venda de um produto

    Scenario: É realizado a venda de um produto com sucesso
        Given Um estoque de 2 bananas
        When Cliente solicita 1 bananas
        Then Estoque de bananas deve conter 1 bananas

    Scenario: Não há estoque suficiente de bananas
        Given Um estoque de 1 bananas
        When Cliente solicita 2 bananas
        Then Gerar erro avisando a indisponibilidade de estoque

    Scenario: Produto não pertence ao catálogo
        Given Estoque não possui o produto celulares
        When Cliente solicita 1 celulares
        Then Gerar erro avisando a inexistência do produto no catálogo
