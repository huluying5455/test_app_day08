import pytest

def test_a():
    print("====> test_a")
    assert 2>3

def test_b():
    print("===> test_b")
    assert True

if __name__ == '__main__':
    #  主函数运行方式 -不推荐使用，但适用于debug时使用
    pytest.main(["test_001.py"])