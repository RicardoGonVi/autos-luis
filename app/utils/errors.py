from pandas.testing import assert_frame_equal


def assert_frame_not_equal(*args, **kwargs):
    try:
        assert_frame_equal(*args, **kwargs)
    except AssertionError:
        # Error when frames are not equal
        pass
    else:
        # Error when frames are equal
        raise AssertionError
