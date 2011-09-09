from settings import FLICKR_API_KEY, FLICKR_API_SECRET
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import flickrapi
from django.conf import settings

def require_flickr_auth(view):
	def protected_view(request, *args, **kwargs):
		if 'token' in request.session:
			token = request.session['token']			
		else:
			token = None			

		f = flickrapi.FlickrAPI(FLICKR_API_KEY,
			FLICKR_API_SECRET, token=token,
			store_token=False)

		if token:
			#check validity of the token
			try:
				f.auth_checkToken()
			except flickrapi.FlickrError:
				#set invalid token to None
				token = None
				del request.session['token']

		if not token:
			# Redirect to Flickr for authentication 
			# if no valid token
			url = f.web_login_url(perms='write')
			return redirect(url)

		return view(request, *args, **kwargs)

	return protected_view

def flickr_callback(request):
	f = flickrapi.FlickrAPI(FLICKR_API_KEY,
		   FLICKR_API_SECRET, store_token=False)

	frob = request.GET['frob']
	token = f.get_token(frob)
	request.session['token'] = token

	return redirect('index')

def flickr(request):
	token = request.session['token']			
	
	f = flickrapi.FlickrAPI(FLICKR_API_KEY,
		FLICKR_API_SECRET, token=token,
		store_token=False)

	return f
	
def getPhotosets(flickr):
	photoset_list = flickr.photosets_getList().find('photosets').findall('photoset')
	photoset_list_array = []
	for photoset in photoset_list:
		photoset_id = photoset.attrib['id']
		photoset_title = photoset.find('title').text
		photoset_list_array.append({
			'id':photoset_id,
			'name':photoset_title})
	return photoset_list_array

def getPhotos(flickr,id):
	photoset_photos = flickr.photosets_getPhotos(photoset_id=id).find('photoset').findall('photo')
	photoset_photos_list = []
	for photo in photoset_photos:
		photo_id = photo.attrib['id']
		secret = photo.attrib['secret']
		farm = photo.attrib['farm']
		server = photo.attrib['server']
		title = photo.attrib['title']
		photo_url = 'http://farm%s.static.flickr.com/%s/%s_%s.jpg' % (farm,server,photo_id,secret)
		photoset_photos_list.append(photo_url)
	return photoset_photos_list

@require_flickr_auth
def index(request):
	f = flickr(request)
	photosets = getPhotosets(f)
	output = []
	for photoset in photosets:
		photos = getPhotos(f,photoset['id'])
		output.append({
			'album_name':photoset['name'],
			'photo_list': photos})
		
	context = {'output':output}
	return render_to_response(
			'index.html',
			context,
			context_instance=RequestContext(request))