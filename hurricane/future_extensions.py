from types import MethodType

from tornado.concurrent import Future
from tornado.ioloop import IOLoop


def future_map(self, f):
    """
    Applies a transformational function to this Future.

    :type self: Future
    :type f: (object) -> object
    :return: A new ``Future`` with the transformed value.
    :rtype: Future
    """
    mapped_fut = Future()
    self.add_done_callback(lambda fut: mapped_fut.set_result(f(fut.result())))
    return mapped_fut

Future.map = MethodType(future_map, None, Future)


def future_flat_map(self, f):
    """
    Flat map

    :type self: Future
    :type f: (object) -> Future
    :rtype: Future
    """
    raise NotImplementedError()
