from enum import Enum
from typing import Union


class LanguageType(Enum):
    """
    语言类型枚举类

    """

    JAVA = (1, "Java", "java")
    C_PLUS = (2, "C++", "cpp")

    @classmethod
    def get_type_by_specified_value(cls, index: int, value: Union[str, int]):
        """
        通过指定某个位置的值来获取对应的枚举类型

        :param index:
        :param value:
        :return:
        """
        for member in cls:
            if member.value[index] == value:
                return member
        return None


class CustomEnum(Enum):
    @classmethod
    def get_type_by_specified_value(cls, index: int, value: object):
        """
        通过指定某个位置的值来获取对应的枚举类型

        :param index:
        :param value:
        :return:
        """
        for member in cls:
            if member.value[index] == value:
                return member
        return None


class MyEnum(CustomEnum):

    ONE = (1, "1")
    TWO = (2, "2")
    THREE = (3, "3")


if __name__ == "__main__":
    assert LanguageType.C_PLUS == LanguageType.get_type_by_specified_value(1, "C++")
    assert MyEnum.TWO == MyEnum.get_type_by_specified_value(1, "2")
