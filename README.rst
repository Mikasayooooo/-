setup.py 在安装python的相关模块和库时，我们一般使用pip install 模块名或者python setup.py install，前者是在线安装，会安装该包的相关依赖包；
后者是下载源码包然后在本地安装，不会安装该包的相关依赖包

README.rst README 文档，告诉用户如何使用你的插件，具体能实现什么功能

pytest_change_report.py 也就是之前conftest.py里面写的hook函数实现的功能

tests 用于测试本插件的相关功能，属于自测的内容

tests/conftest.py 开启需要的插件pytester

tests/test_change_report.py 测试插件的代码





==============
pytest-change-report: pytest plugin
==============


**This pytest plugin turn . into √，turn F into x**


Usage
=====

从github源码安装

   pip install git+https://github.com/yoyoketang/pytest-change-report.git

命令行运行示例

   pytest --change on


demo
====

先写pytest用例test_demo.py

    def test_01():
        a = "hello"
        b = "hello"
        assert a == b


    def test_02(login):
        a = "hello"
        b = "hello world"
        assert a == b

命令行执行pytest, 默认不会改变之前的报告内容

    >pytest test_demo.py
    ============================= test session starts =============================
    collected 2 items

    test_demo.py .F                                                          [100%]

    ================================== FAILURES ===================================
    ___________________________________ test_02 ___________________________________

        def test_02():
            a = "hello"
            b = "hello world"
    >       assert a == b
    E       AssertionError: assert 'hello' == 'hello world'
    E         - hello
    E         + hello world

    test_demo.py:10: AssertionError
    ===================== 1 failed, 1 passed in 0.11 seconds ======================

加上 --change on 参数后运行

    >pytest test_demo.py --change on
    ============================= test session starts =============================
    collected 2 items

    test_demo.py √x                                                          [100%]

    ================================== FAILURES ===================================
    ___________________________________ test_02 ___________________________________

        def test_02():
            a = "hello"
            b = "hello world"
    >       assert a == b
    E       AssertionError: assert 'hello' == 'hello world'
    E         - hello
    E         + hello world

    test_demo.py:10: AssertionError
    ===================== 1 failed, 1 passed in 0.08 seconds ======================



pytest.ini
==========

可以添加到pytest.ini配置文件，这样默认就会带上--change参数

      [pytest]
      --change = on

