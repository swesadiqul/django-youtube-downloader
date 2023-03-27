from turtle import title
from django.shortcuts import render
from pytube import YouTube
import os

# create a view
def index(request):
	return render(request, 'index.html')

def download(request):
	global url
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
	# video = yt.streams.filter(progressive=True)
	source = yt.streams.filter(adaptive=True)
	mime = []
	for x in source:
    		print(x)
    		# for y in x:
    		# 		mime.append(y.mime_type)
	print(mime)
    		
	em_link = url.replace("watch?v=", "embed/")
	Title = yt.title

	context = {
		'source': source,
		'embed': em_link,
		'title': Title,
	}

	return render(request, 'download.html', context)

def yt_download_done(request, resolution):
	global url
	homedir = os.path.expanduser("~")
	dirs = homedir + "/Downloads"

	if request.method == "POST":
		YouTube(url).streams.get_by_resolution(resolution).download(dirs)
		return render(request, 'done.html')
	else:
		return render(request, 'error.html')