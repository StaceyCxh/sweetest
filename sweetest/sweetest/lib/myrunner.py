import time
import warnings
from unittest import TextTestRunner, TextTestResult
from unittest.signals import registerResult
from sweetest.lib.log import logger
from sweetest.globals import g


class myTextTestResult(TextTestResult):

    def startTest(self, test):
        super(TextTestResult, self).startTest(test)
        if self.showAll:
            logger.info(self.getDescription(test) + "用例开始运行" + "... ")

    def addSuccess(self, test):
        super(TextTestResult, self).addSuccess(test)
        if self.showAll:
            logger.info("测试通过" + "\r\n")
        elif self.dots:
            logger.info('.')

    def addError(self, test, err):
        super(TextTestResult, self).addError(test, err)
        if self.showAll:
            logger.error("测试失败" + "\r\n")
        elif self.dots:
            logger.info('E')

    def addFailure(self, test, err):
        super(TextTestResult, self).addFailure(test, err)
        if self.showAll:
            logger.error("测试失败" + "\r\n")
        elif self.dots:
            logger.info('F')

    def addSkip(self, test, reason):
        super(TextTestResult, self).addSkip(test, reason)
        if self.showAll:
            logger.info("skipped {0!r}".format(reason))
        elif self.dots:
            logger.info("s")

    def addExpectedFailure(self, test, err):
        super(TextTestResult, self).addExpectedFailure(test, err)
        if self.showAll:
            logger.info("expected failure")
        elif self.dots:
            logger.info("x")

    def addUnexpectedSuccess(self, test):
        super(TextTestResult, self).addUnexpectedSuccess(test)
        if self.showAll:
            logger.info("unexpected success")
        elif self.dots:
            logger.info("u")

    def printErrors(self):
        if self.dots or self.showAll:
            pass
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            logger.error("\r\n%s: %s\r\n%s\r\n" % (
            flavour, self.getDescription(test), err))


class myTextTestRunner(TextTestRunner):

    def _makeResult(self):
        return myTextTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        result.tb_locals = self.tb_locals
        with warnings.catch_warnings():
            if self.warnings:
                # if self.warnings is set, use it to filter all the warnings
                warnings.simplefilter(self.warnings)
                # if the filter is 'default' or 'always', special-case the
                # warnings from the deprecated unittest methods to show them
                # no more than once per module, because they can be fairly
                # noisy.  The -Wd and -Wa flags can be used to bypass this
                # only when self.warnings is None.
                if self.warnings in ['default', 'always']:
                    warnings.filterwarnings('module',
                            category = DeprecationWarning,
                            message = r'Please use assert\w+ instead.')
            startTime = time.time()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()
            try:
                test(result)
            finally:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()
            stopTime = time.time()
        timeTaken = stopTime - startTime
        result.printErrors()
        if hasattr(result, 'separator2'):
            logger.info(result.separator2)
        run = result.testsRun
        logger.info("Ran %d test%s in %.3fs\r\n" %
                            (run, run != 1 and "s" or "", timeTaken))
        # 记录测试运行时间
        g.results['totalTime'] = str(round(timeTaken, 2))+'s'

        expectedFails = unexpectedSuccesses = skipped = 0
        try:
            results = map(len, (result.expectedFailures,
                                result.unexpectedSuccesses,
                                result.skipped))
        except AttributeError:
            pass
        else:
            expectedFails, unexpectedSuccesses, skipped = results

        infos = []
        if not result.wasSuccessful():
            logger.error("FAILED!" + "\r\n")
            failed, errored = len(result.failures), len(result.errors)
            if failed:
                infos.append("failures=%d" % failed)
            if errored:
                infos.append("errors=%d" % errored)
        else:
            logger.info("SUCCESS!" + "\r\n")
        if skipped:
            infos.append("skipped=%d" % skipped)
        if expectedFails:
            infos.append("expected failures=%d" % expectedFails)
        if unexpectedSuccesses:
            infos.append("unexpected successes=%d" % unexpectedSuccesses)
        if infos:
            logger.info(" (%s)" % (", ".join(infos),))
        else:
            logger.info("\n")
        return result
