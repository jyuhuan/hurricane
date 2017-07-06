from tornado.testing import AsyncTestCase, gen_test
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.concurrent import Future

import hurricane.future_extensions


class TestRichFuture(AsyncTestCase):

    @gen.coroutine
    def sample_future_of_str(self):
        raise gen.Return('test')

    @gen_test
    def test_map(self):
        fut = self.sample_future_of_str()
        result = yield fut.map(lambda s: s.upper())
        self.assertEquals(result, 'TEST')
