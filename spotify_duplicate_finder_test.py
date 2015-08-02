import unittest
from spotify_duplicate_finder import SpotifyDuplicateFinder
from spotify_duplicate_finder import Match


class MyTestCase(unittest.TestCase):
    def test_find_duplicates_in_list_matching_on_url(self):
        test_data = ('http://open.spotify.com/track/0QctD66Yhe2D2yjVhxtTVx '
                     'http://open.spotify.com/track/0QctD66Yhe2D2yjVhxtTVx '
                     'http://open.spotify.com/track/7IOlbck6GABZ4LKKt33qgp '
                     'http://open.spotify.com/track/5uLSHSB8HGzVoMl0Q9YKcv '
                     'http://open.spotify.com/track/5fpj84RsT9cOTfWUCxBTXu '
                     'http://open.spotify.com/track/3fqwjXwUGN6vbzIwvyFMhx '
                     'http://open.spotify.com/track/62R1MRux3R0v2cngA2xdJn '
                     'http://open.spotify.com/track/2Y48Q7HryWdPJZypJotjlJ '
                     'http://open.spotify.com/track/2CzNAvr2nZKYxthPVMvdVe '
                     'http://open.spotify.com/track/2tariJ4d2UA9sy8SW9wc21 '
                     'http://open.spotify.com/track/4pj0iYI68FtGzKHJYRT84X '
                     'http://open.spotify.com/track/6Z9qTK7hFnHmITOFURnRix '
                     'http://open.spotify.com/track/79dgxSKYhjIU50XB2Tzyix '
                     'http://open.spotify.com/track/7eOlnxr0qiDugjddz945FC '
                     'http://open.spotify.com/track/48ZS7C9BIHmG5DHoN1XEz4 '
                     'http://open.spotify.com/track/6pIZ0u32c2Lku8PmCWtnMy '
                     'http://open.spotify.com/track/6pIZ0u32c2Lku8PmCWtnMy '
                     'http://open.spotify.com/track/6CKAuc7LAVa1oSKk2Px2b4 '
                     'http://open.spotify.com/track/6CKAuc7LAVa1oSKk2Px2b4')
        duplicates = SpotifyDuplicateFinder.find_duplicates(list=test_data,
                                                            match_on=Match.URL)
        self.assertEquals(3, len(duplicates[0]))

    def test_find_duplicates_in_list_matching_on_title(self):
        test_data = ('http://open.spotify.com/track/0QctD66Yhe2D2yjVhxtTVx '
                     'http://open.spotify.com/track/0QctD66Yhe2D2yjVhxtTVx '
                     'http://open.spotify.com/track/7IOlbck6GABZ4LKKt33qgp '
                     'http://open.spotify.com/track/5uLSHSB8HGzVoMl0Q9YKcv '
                     'http://open.spotify.com/track/5fpj84RsT9cOTfWUCxBTXu '
                     'http://open.spotify.com/track/3fqwjXwUGN6vbzIwvyFMhx '
                     'http://open.spotify.com/track/62R1MRux3R0v2cngA2xdJn '
                     'http://open.spotify.com/track/2Y48Q7HryWdPJZypJotjlJ '
                     'http://open.spotify.com/track/2CzNAvr2nZKYxthPVMvdVe '
                     'http://open.spotify.com/track/2tariJ4d2UA9sy8SW9wc21 '
                     'http://open.spotify.com/track/4pj0iYI68FtGzKHJYRT84X '
                     'http://open.spotify.com/track/6Z9qTK7hFnHmITOFURnRix '
                     'http://open.spotify.com/track/79dgxSKYhjIU50XB2Tzyix '
                     'http://open.spotify.com/track/7eOlnxr0qiDugjddz945FC '
                     'http://open.spotify.com/track/48ZS7C9BIHmG5DHoN1XEz4 '
                     'http://open.spotify.com/track/6pIZ0u32c2Lku8PmCWtnMy '
                     'http://open.spotify.com/track/6pIZ0u32c2Lku8PmCWtnMy '
                     'http://open.spotify.com/track/6CKAuc7LAVa1oSKk2Px2b4 '
                     'http://open.spotify.com/track/6CKAuc7LAVa1oSKk2Px2b4')
        duplicates = SpotifyDuplicateFinder. \
            find_duplicates(list=test_data, match_on=Match.title)
        self.assertEquals(3, len(duplicates[0]))

    def test_find_duplicates_in_file_matching_on_url(self):
        duplicates = SpotifyDuplicateFinder. \
            find_duplicates(file=open('tracks_test.txt', 'r'))
        self.assertEquals(3, len(duplicates[0]))

if __name__ == '__main__':
    unittest.main()
