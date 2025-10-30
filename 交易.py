from datetime import datetime
from transaction import Transaction
class InputHandler:
    @staticmethod
    def get_float_input(prompt):
        """获取浮点数输入"""
        while True:
            try:
                value=float(input(prompt))
                return value
            except ValueError:
                print("请输入有效数字")
    @staticmethod
    def get_date_input(prompt):
        """获取日期输入"""
        while True:
            date_str=input(f"{prompt}(格式：xxxx.yy.zz，回车使用今天日期):").strip()
            if not date_str:
                return datetime.now()
            try:
                return datetime.now()
            except ValueError:
                print("日期格式错误，请用xxxx.yy.zz的格式")
