from data import Point, Rectangle, Duration, Song


# Write your functions for each part in the space below.

# Part 1

# Takes in two points and creates an object of class rectangle from such where they are
# two different corners

def create_rectangle(point1:Point, point2:Point) -> Rectangle:
    top_left = Point(min([point1.x, point2.x]), max([point1.y, point2.y]))
    bottom_right = Point(max([point1.x, point2.x]), min([point1.y, point2.y]))
    return Rectangle(top_left, bottom_right)

# Part 2

# Checks if one duration is shorter than another duration, returns if it is true
# or false

def shorter_duration_than(duration1:Duration, duration2:Duration) -> bool:
    return (duration1.minutes < duration2.minutes or (duration1.minutes ==
        duration2.minutes and duration1.seconds < duration2.seconds))

# Part 3

# Takes in a list of songs and a duration, spits out a list of songs from the input
# list that are shorter than the given duration

def song_shorter_than(songs:list[Song], duration_check:Duration) -> list[Song]:
    short_songs = []
    for song in songs:
        if shorter_duration_than(song.duration, duration_check):
            short_songs.append(song)
    return short_songs

# Part 4

# Takes in a list of songs and list of indexes for the list of songs, and adds together
# the songs at those index's duration

def running_time(songs:list[Song], song_ind:list[int]) -> Duration:
    total_duration = Duration(0, 0)
    for ind in song_ind:
        if ind >= 0 and (ind < len(songs)):
            total_duration.minutes = total_duration.minutes + songs[ind].duration.minutes
            total_duration.seconds = total_duration.seconds + songs[ind].duration.seconds
    while total_duration.seconds >= 60:
        total_duration.minutes = total_duration.minutes + 1
        total_duration.seconds = total_duration.seconds - 60
    return total_duration

# Part 5

# Takes in an input list of pairs/links of two different cities, and a different
# list of cities or a 'route' between cities, and checks if the given route
# is able to be traveled using pairs in the first input list. Returns if validity
# is true or false

def validate_route(city_links:list[list[str]], route:list[str]) -> bool:
    valid = False
    if len(route) == 0 or len(route) == 1:
        valid = True
    for link in city_links:
        for i in range(len(route)-1):
            segment = route[i:i+2]
            if (segment == link) or (segment.reverse() == link):
                valid = True
    return valid

# Part 6

# takes in an input list of numbers and returns the first index of the longest
# string of repetitions of the same number

def longest_repetition(rep_list:list[int]) -> int or None:
    longest_rep = 0
    largest = 0
    if rep_list == []:
        return None
    for i in range(len(rep_list)):
        streak = 0
        for j in range(i, len(rep_list)):
            if rep_list[i] == rep_list[j]:
                streak = streak + 1
            else:
                break
        if streak > largest:
            largest = streak
            longest_rep = i
    return longest_rep