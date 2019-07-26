from sweetest.autotest import AutoTest
from sweetest.lib.mail import Pop3

# 执行自动化测试
AutoTest.plan()
# result = AutoTest.get_result()

# 如果是集成到 CI/CD，可以给出退出码
#sys.exit(sweet.code)