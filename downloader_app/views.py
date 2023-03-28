from turtle import title
from django.shortcuts import render
from pytube import YouTube
import os

# create a view
def index(request):
	return render(request, 'index.html')

def download(request):
	global url
	global yt
	url = request.POST.get('url')
	yt = YouTube(url)
	# print(yt)
	# print(yt.title)
	# print(yt.thumbnail_url)
	# print(yt.streams)
	# print(yt.streams.filter(progressive=True))
	# print(yt.streams.filter(adaptive=True))
	# print(yt.streams.filter(only_audio=True))
	# print(yt.streams.filter(only_video=True))
	# video = []
	webm_format = yt.streams.filter(progressive=False, mime_type='video/webm')
	source = yt.streams.filter(progressive=True, file_extension='mp4')
	audio_format = yt.streams.filter(only_audio=True)	
	em_link = url.replace("watch?v=", "embed/")
	title = yt.title

	context = {
		'source': source,
		'embed': em_link,
		'title': title,
		'webm_format' : webm_format,
		'audio_format': audio_format
	}

	return render(request, 'download.html', context)

def yt_download_done(request, itag):
	global url
	homedir = os.path.expanduser("~")
	dirs = homedir + "/Downloads"

	if request.method == "GET":
		# youtube = YouTube(url).streams.get_by_resolution(resolution)
		stream = YouTube(url).streams.get_by_itag(itag)
		stream.download(dirs)
		return render(request, 'done.html')
	else:
		return render(request, 'error.html')