import discord
import youtube_dl as ytdl

#__all__ = ['a', 'v', 'b']

class MusicPlayer():

  def __init__(self, message, voiceChannel):

    self.queue = []
    self.queueContruct = {
      'textChannel': message.channel,
      'voiceChannel': voiceChannel,
      'connection': None,
      'songs': [],
      'volume': 5,
      'playing': True
    }

    #añadir cancion
    queueContruct.songs.push(song)

    self.queue.set(message.guild.id, queueContruct)

    try:
      connection = await voiceChannel.join()
      queueContruct.connection = connection
      play(message.guild, queueContruct.songs[0]);
    except Exception() as err:
      console.log(err);
      queue.delete(message.guild.id);
      return message.channel.send(err);
      

  async def execute(self, message, serverQueue):
    args = message.content.split(" ")

    voiceChannel = message.member.voice.channel
    if (voiceChannel is None):
      return message.channel.send(
        "You need to be in a voice channel to play music!"
      )

    permissions = voiceChannel.permissionsFor(message.client.user);

    if (not permissions.has("CONNECT") or not permissions.has("SPEAK")):
      return message.channel.send(
        "I need the permissions to join and speak in your voice channel!"
      )

    songInfo = await ytdl.getInfo(args[1])
    song = {
      'title': songInfo.videoDetails.title,
      'url': songInfo.videoDetails.video_url
    }

  def play(guild, song):
    serverQueue = queue.get(guild.id);
    if (not song):
      serverQueue.voiceChannel.leave()
      queue.delete(guild.id)
      return
    dispatcher = serverQueue.connection.play(ytdl(song.url))
    
    

    
