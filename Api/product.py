import requests

import app, logging


class ProductApi:
    def __init__(self):
        # 商品分类
        self.product_classify_url = app.base_url + "/category/all"
        # 分类下商品
        self.classify_product_url = app.base_url + "/product/by_category?id=2"
        # 商品信息
        self.product_detail_url = app.base_url + "/product/2"

    def product_calssify_api(self):
        """商品分类"""
        logging.info("商品-商品分类")
        return requests.get(self.product_classify_url)

    def classify_product_api(self, classify_id=2):
        """
        分类下商品
        :param class_id:分类id
        :return:
        """
        logging.info("商品-分类下商品")
        # 请求数据
        data = {"id": classify_id}
        return requests.get(self.classify_product_url, params=data)

    def product_detail_api(self, product_id=2):
        """
        商品信息
        :param product_id: 商品id
        :return:
        """
        logging.info("商品-商品信息")
        return requests.get(self.product_detail_url.format(product_id))
