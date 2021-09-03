from core import WasRun


if __name__ == '__main__':
    test = WasRun('test_method')
    print(test.was_run)
    test.run()
    print(test.was_run)
