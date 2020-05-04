class Restaurant():
    """创建一个餐馆类"""
    def __init__ (self,restaurant_name,cuisine_type):
        """初始华属性"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("这是一个很好的餐馆名：  "+self.restaurant_name.title())
    def open_restaurant(self):
        print(self.restaurant_name+self.cuisine_type.title()+"  欢迎您的光临!")

restaurant=Restaurant("南城县聚财酒店","正在营业")
restaurant.describe_restaurant()
restaurant.open_restaurant()








