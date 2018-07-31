import unittest


def test():
    "test load and run"
    tests = unittest.TestLoader().discover('.', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 1
    else:
        raise ValueError('test failed')


if __name__ == '__main__':
    test()
