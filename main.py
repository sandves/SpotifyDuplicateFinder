import codecs

from spotify_duplicate_finder import SpotifyDuplicateFinder
from spotify_duplicate_finder import Match


def main():
    match_on = input("Type 1 to match on URL and 2 to match on title: ")

    if match_on == '1':
        duplicates, number_of_distinct_tracks = SpotifyDuplicateFinder. \
            find_duplicates(match_on=Match.URL)
        tracks = [SpotifyDuplicateFinder.get_description(track)
                  for track in duplicates]
    elif match_on == '2':
        duplicates, number_of_distinct_tracks = SpotifyDuplicateFinder. \
            find_duplicates(match_on=Match.title)
        tracks = [track for track in duplicates]

    if len(tracks) == 0:
        print('The playlist contains ' + str(number_of_distinct_tracks) +
              ' tracks and no duplicates.')
    else:
        with codecs.open("duplicates.txt", "w", "utf-8") as dup:
            dup.write(
                'Your playlist contains ' + str(number_of_distinct_tracks) +
                ' distinct tracks.\nFound '
                + str(len(tracks)) + ' duplicates: \n\n')
            [dup.write(tracks[i] + '\n') for i in range(0, len(tracks))]
        print('Found ' + str(number_of_distinct_tracks) +
              ' distinct tracks and ' + str(len(tracks)) +
              ' duplicates. Check duplicates.txt '
              'for a list of the duplicates.')

if __name__ == '__main__':
    main()