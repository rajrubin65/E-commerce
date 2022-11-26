import json
from fastapi import APIRouter
from configurations.config import mongo_db
from bson import BSON
from bson import json_util
from app.routers.home.model import *

router = APIRouter()
db = mongo_db.local.products

@router.post('/add-product')
def add_product(product:Product):
    db.insert_one(product.dict())
    return product.dict()

@router.post('/add-all-products')
def add_product(all_product:productList):
    db.insert_many(all_product)
    return all_product.dict()   


@router.get('/get-categories')
def get_categories():
    data = list(db.find({},{'_id':0,'product_category':1}))
    data = json.dumps(data)
    return json.loads(data)

@router.get('/get-brands-by-category')
def get_brands(categorie):
    data = list(db.find({'product_category':categorie},{'_id':0,'brands.product_brand_name':1}))
    data = json.dumps(data)
    return json.loads(data)

@router.get('/get-products')
def get_brands(brand_name):
    data = list(db.find({'brands.product_brand_name':brand_name},{'_id':0, 'brands.brand_products':1}))
    data = json.dumps(data)
    return json.loads(data)
