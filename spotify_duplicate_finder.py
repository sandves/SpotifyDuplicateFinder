#! /usr/bin/env python

from urllib.request import urlopen
from collections import Counter
from enum import Enum
import urllib
import json
import sys
import codecs


class Match(Enum):
    URL = 1
    title = 2


class SpotifyDuplicateFinder(object):

    @staticmethod
    def progress(count, total, suffix=''):
        """
        This function displays a progress bar on the console.
        :param count: The number of elements that has been processed.
        :param total: Total number of elements.
        :param suffix: The text to be shown to the right of the progress bar.
        :return: None
        """
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
        sys.stdout.flush()

    @staticmethod
    def fetch(url):
        """
        Reads data from the provided url and loads it into a JSON-object.
        :param url: The address to where the data is located.
        :return: A JSON-object containing the data.
        """
        json_data = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(json_data))
        json_data.close()
        return data

    @staticmethod
    def http_to_uri(track_list):
        """
        Convert a list of Spotify HTTP addresses to a list of Spotify URIs.
        :param track_list: The list of Spotify HTTP links to be converted.
        :return: List of Spotify URIs.
        """
        uri = []
        for track in track_list:
            id = track.split("track/")
            if len(id) > 1:
                uri.append("spotify:track:" + id[1])
        return uri

    @staticmethod
    def get_title(url):
        """
        Reads the HTTP address to the song and extracts the title from the
        response.
        :param url: The HTTP address that points to the song.
        :return: The title of the song.
        """
        f = urlopen(url).read().decode("utf-8")
        s = f.find('<title>')
        e = f.find('</title>')
        # To extract the title wee need to skip the 7 first and the 11 last
        # characters. The 7 first is to remove the "<title>" tag, and the 11
        # last is to remove the " on Spotify" suffix.
        return f[s:e][7:-11]

    @staticmethod
    def get_description(url):
        """
        Builds a description (artists and track name) based on data retrieved
        from the Metadata API.
        :param url: HTTP address to the track.
        :return: A string with the following format;
        "artist1, artist2 - track name".
        """
        id = url.split("track/")
        if len(id) > 1:
            lookup_uri = ("http://ws.spotify.com/lookup" +
                          "/1/.json?uri=spotify:track:" + id[1])
        track = SpotifyDuplicateFinder.fetch(lookup_uri)["track"]
        artists = track["artists"]
        a = ""

        # If there are multiple artists, make a comma separated string with all
        # the artists.
        if len(artists) > 1:
            for idx, artist in enumerate(artists):
                if idx != len(artists)-1:
                    a += artists[idx]["name"] + ", "
                else:
                    a += artists[idx]["name"]
        # If not, use the one and only artists in the list.
        else:
            a = artists[0]["name"]
        return a + " - " + track["name"]

    @staticmethod
    def find_duplicates(file=open('tracks.txt', 'r'), list=None,
                        match_on=Match.URL):
        """
            Make a list from a file of space separated Spotify links.

            By matching on URL, the function will find all duplicates with the
            same unique ID. By matching on title, the function will find all
            duplicates with the same name (which may be incorrect due to the
            fact that many songs may have the same name without being the same
            song). The title matching function is also a lot slower due to all
            the HTTP requests.

            You will be presented with a progress bar on the console to keep
            track of the matching process.
            :rtype : List, int.
            :param file: The file to read the URLs from.
            :param list: The playlist can also be provided as a Python list.
            This will override the file parameter if set.
            :return: A set of duplicates and the number of distinct songs
            """
        a = []
        if match_on == Match.URL:
            if list is None:
                songs = [word for line in file for word in line.split()]
            else:
                songs = list.split()
            for idx, song in enumerate(songs):
                a.append(song)
                SpotifyDuplicateFinder.progress(idx, len(a), song)
        elif match_on == Match.title:
            if list is None:
                http_tracks = [word for line in file for word in line.split()]
            else:
                http_tracks = list.split()
            uris = SpotifyDuplicateFinder.http_to_uri(http_tracks)
            for idx, uri in enumerate(uris):
                lookup_uri = "http://ws.spotify.com/lookup/1/.json?uri=" + uri
                name = SpotifyDuplicateFinder. \
                    fetch(lookup_uri)["track"]["name"]
                a.append(name)
                SpotifyDuplicateFinder.progress(idx, len(uris), name)
        return Counter(a) - Counter(set(a)), len(Counter(set(a)))