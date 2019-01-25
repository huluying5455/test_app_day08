
class Test_Abc:
    def setup(self):
        print("----> setup")

    def teardown(self):
        print("---> teardown")

    def test_abc_01(self):
        print("--->test_abc_01")
        assert True

    def test_abc_02(self):
        print("--->test_abc_02")
        assert True