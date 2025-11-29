import pytest
from products.models import Product

def test_product(db,product_factoray):
    product=product_factoray.build()
    print(product.description)
    assert True

@pytest.mark.parametrize(
    "name,categoray,description,slug,price,stock,validity",
    [
        ('it ends with us',1,'novel by collen hover','it end with us',0.00,0.00,True)
    ]
)

def test_product_instanc(
    db, product_factoray,name,categoray,description,slug,price,stock,validity
):
    test=product_factoray(
        name=name,
        categoray_id=categoray,
        description=description,
        slug=slug,
        price=price,
        stock=stock,
    )
    item=Product.objects.all().count()
    print(test)
    assert item==validity

