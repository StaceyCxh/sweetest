from sweetest.globals import g
from sweetest.lib.log import logger


class Windows(object):
    def __init__(self):
        super(Windows, self).__init__()
        self.init()

    def init(self):
        # 当前页面名称
        self.current_page = ''
        # 当前frame名字
        self.frame = 0
        # 所有页面--窗口名柄映射表，如：{'门户首页': 'CDwindow-3a12c86f-1986-4c02-ba7b-5a0ed94c5963',...}
        self.pages = {}
        # 新开窗口标志
        self.new_window_flag = True
        # App context
        self.current_context = 'NATIVE_APP'

    def switch_window(self, page):
        '''
        切换标签页/窗口
        :param page: 目标页面
        :return:
        '''
        if self.new_window_flag:
            if page in list(self.pages):
                page = '通用'
                g.current_page = '通用'
            self.new_window_flag = False

        if page != '通用':
            if page not in list(self.pages):
                # 如果当前页未注册，则把当前窗口捆定到当前页面
                for k in list(self.pages):
                    if g.driver.current_window_handle == self.pages[k]:
                        self.pages.pop(k)
                self.pages[page] = g.driver.current_window_handle
                self.current_page = page
                logger.info('--- 注册标签页: %s' % repr(page))
                logger.info('Pages:')
                logger.info(self.pages)

            elif self.pages[page] != g.driver.current_window_handle:
                # 如果当前窗口为 HOME，则关闭之
                if self.current_page == 'HOME':
                    g.driver.close()
                    self.pages.pop('HOME')
                # 再切换到需要操作的窗口
                tw = self.pages[page]
                logger.info('--- 旧窗口: %s' % g.driver.current_window_handle)
                logger.info('--- 切换到窗口: %s' % repr(tw))
                g.driver.switch_to_window(tw)
                self.current_page = page
                logger.info('--- 当前标签页: %s' % repr(page))
                logger.info('Pages:')
                logger.info(self.pages)

    def switch_frame(self, frame):
        if frame.strip():
            frame = [x.strip() for x in frame.split('|')]
            if frame != self.frame:
                if self.frame != 0:
                    g.driver.switch_to.default_content()
                for f in frame:
                    logger.info('--- Frame值:  %s' % repr(f))
                    if f.startswith('#'):
                        f = int(f[1:])
                    elif '#' in f:
                        from sweetest.parse import elements_incase_format
                        from sweetest.locator import locating_element
                        element = elements_incase_format('通用',f)[2]
                        f = locating_element(element)
                    logger.info('--- 切换Frame: %s' % repr(f))
                    g.driver.switch_to.frame(f)
                self.frame = frame
        else:
            if self.frame != 0:
                g.driver.switch_to.default_content()
                self.frame = 0

    def open(self, step):
        # 查看当前窗口是否已经注册到 pages 映射表
        c = self.pages.get(self.current_page, '')
        # 如果已经存在，则需要清除和当前窗口绑定的页面
        if c:
            for k in list(self.pages):
                if self.current_page == self.pages[k]:
                    self.pages.pop(k)

        # 获取当前窗口handle
        handle = g.driver.current_window_handle
        # 注册窗口名称和handle
        self.register(step, handle)

    def register(self, step, handle):
        '''
        注册新标签页，打开链接或点击新开窗口时调用
        :param step: 测试步骤
        :param handle: 窗口句柄
        :return:
        '''
        # 如果有提供新窗口名字，则使用该名字，否则使用默认名字：HOME
        new_page = 'HOME'
        for k in ('新窗口', '标签页名', 'tabname'):
            if step['data'].get(k):
                new_page = step['data'].get(k)
        # 已存在同名的窗口，则
        if new_page in list(self.pages) and handle != self.pages[new_page]:

            # 1. 切换到同名旧页面去关闭它
            g.driver.switch_to_window(self.pages[new_page])
            g.driver.close()
            # 2. 清除旧页面
            self.pages.pop(new_page)

        # 然后切回当前窗口
        g.driver.switch_to_window(handle)
        # 再添加到窗口资源池 g.pages
        self.pages[new_page] = handle
        # 把当前窗口名字改为新窗口名称
        self.current_page = new_page
        logger.info('--- 注册新页面: %s' % repr(new_page))
        logger.info('Pages:')
        logger.info(self.pages)

        # 新窗口标志置为是
        self.new_window_flag = True

    def close(self):
        all_handles = g.driver.window_handles
        for handle in all_handles:
            # 切换到每一个窗口,并关闭它
            g.driver.switch_to_window(handle)
            g.driver.close()

    def switch_context(self, context):
        if context.strip() == '':
            context = 'NATIVE_APP'
        logger.info('--- ALL   Contexts:%s' % g.driver.contexts)
        logger.info('--- Input  Context:%s' % repr(context))
        if context != self.current_context:
            if context == '':
                context = None
            logger.info('--- Switch Context:%s' % repr(context))
            g.driver.switch_to.context(context)
            self.current_context = context


w = Windows()
