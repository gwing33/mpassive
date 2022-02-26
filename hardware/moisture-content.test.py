from util import resistanceToPercentage, formatToPercentage


def runTestSuite(tests):
    passed = []
    failed = []
    for test in tests:
        if test[1] == test[2]:
            passed.append(test)
        else:
            failed.append(test)
    
    passedCount = len(passed)
    failedCount = len(failed)
    summary = """Test Results:
    {0} Passed 
    {1} Failed""".format(passedCount, failedCount)
    print(summary)

    if (failedCount > 0):
        print('\nFailed Tests:')

    for failure in failed:
        print('    "' + failure[0] + '" failed to match ', failure[1], ' with ', failure[2])
        
runTestSuite([
    ['Min Value', formatToPercentage(resistanceToPercentage(22400000001)), '<7%'],
    ['Max Value', formatToPercentage(resistanceToPercentage(460000)), '>25%'],
    ['One million', formatToPercentage(resistanceToPercentage(1000000)), '22.68%'],
])