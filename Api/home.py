import requests, app, logging


class HomeApi:
    """首页API接口方法"""

    def __init__(self):
        # 轮播图
        self.banner_url = app.base_url + "/banner/{}"
        self.theme_url = app.base_url + "/theme"
        self.recent_product_url = app.base_url + "/product/recent"

    def banner_api(self, num=1):
        """
        请求轮播图
        :param num: 轮播图页面数
        :return: 响应对象
        """
        logging.info("首页-轮播图")
        return requests.get(self.banner_url.format(num))

    def theme_api(self, ids="1,2,3"):
        """
        请求专题栏
        :param ids: 专题栏数据
        :return:
        """
        logging.info("首页-专题栏")
        data = {"ids": ids}
        return requests.get(self.theme_url, params=data)

    def recent_product_api(self):
        """请求最近商品"""
        logging.info("首页-最近商品")
        return requests.get(self.recent_product_url)
