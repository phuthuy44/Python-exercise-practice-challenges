class Song :
     def __init__(self, title, artist,album, track_number):
          self.title = title
          self.artist = artist
          self.album = album
          self.track_number = track_number

          artist.add_songs(self)
class Album :
     def __init__(self,title,artist,year):
          self.title = title
          self.artist = artist
          self.year = year
          self.tracks = []
          artist.add_album(self)
     def add_tracks(self,title,artist = None):
          """
          The function takes in a title and an artist, and if the artist is not specified, it defaults to
          the artist of the album
          
          :param title: The title of the song
          :param artist: The artist of the album
          """
          if artist is None:
               artist = self.artist
          track_number = len(self.tracks)
          song = Song(title,artist,self,track_number)
          # Adding the song to the list of tracks.
          self.tracks.append(song)

class Artist:
     def __init__(self,name):
          self.name = name
          self.album = []
          self.songs =[]
     def add_album(self,album):
          self.album.append(album)
     def add_songs(self,songs):
          self.songs.append(songs)
class Playlist:
     def __init__(self,name):
          self.name = name
          # Creating an empty list.
          self.songs = []
     def add_song(self,song):
          self.songs.append(song)

band = Artist("Bob's Awesome Band")
album = Album("Bob's First Single", band,2013)
album.add_tracks("A Ballad about Cheese")
album.add_tracks("A Ballad about Cheese( dance a remix)")

playlist = Playlist("My favorite songs")
# Adding the songs from the album to the playlist.
for song in album.tracks:
     playlist.add_song(song)

