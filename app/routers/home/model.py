from pydantic import BaseModel
from typing import Dict,List


class ProductReview(BaseModel):
    product_rating : str
    product_review : str
    user_upload_image :Dict

class ProductBrand(BaseModel):
    product_name :str
    product_price :str
    product_image_url :Dict
    product_details :str
    seller :str
    product_review :List[ProductReview]

class ProductCategory(BaseModel):
    product_brand_name :str
    brand_products :List[ProductBrand]

class Product(BaseModel):
    product_category :str
    brands :List[ProductCategory]

class productList(BaseModel):
    __root__ :List[Product]


def product_entitiy(item):
    item['_id'] = str(item['_id'])
    return item


def product_list_entitiy(entity) ->List:
    return[product_entitiy(item) for item in entity]