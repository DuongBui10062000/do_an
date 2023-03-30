from urllib.parse import urljoin
from django.shortcuts import render, redirect
from websitecontent.models import Blogs
import requests
import bs4
import json
import codecs #mở ghi file nên dùng vì hạn chế lỗi
import os
import glob
from django.http import HttpResponse
from requests.exceptions import ConnectionError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import AddBlogsForm

SOURCE_URL = 'https://suckhoedoisong.vn/y-te/blog-thay-thuoc.htm'
BASE_URL = 'https://suckhoedoisong.vn/y-te/blog-thay-thuoc.htm'

# Create your views here.
def blogPage(request):
	object_list = Blogs.objects.all()
	return render(request, 'websitecontent/blogspage.html', { 'object_list' : object_list, 'nav' : 'blogs' })


def aboutPage(request):
	return render(request, 'websitecontent/aboutpage.html', { 'nav' : 'about' })


def homePage(request):
	return render(request, 'websitecontent/homepage.html', { 'nav' : 'home'})


def detailBlogPage(request, id):
	blog_id = Blogs.objects.get(id=id)
	return render(request, 'websitecontent/detailblog.html', { 'blog_id' : blog_id })


def get_article_url(url, image_url):
	data = {}
	r = requests.get(url)
	if r.ok:
		s = bs4.BeautifulSoup(r.content, 'lxml')

		title = s.select_one('h1.detail-title')
		data['title'] = title.text.strip() if title else ''

		sub_title = s.select_one('h2.detail-sapo')
		data['sub_title'] = sub_title.text.strip() if sub_title else ''

		# content = s.find("div", {'class':'detail-content afcbc-body'})
		# p = content.find_all('p')
		# data['content'] = ''.join(item.prettify() for item in p)
		content = s.select_one('.container .detail__contenent-main')
		data['content'] = content.prettify() if content else ''
		if data['content'] == '':
			return False

		pub_date = s.select_one('span.publish-date')
		data['pub_date'] = pub_date.text.strip() if pub_date else ''

		author = s.select_one('.detail-author')
		data['author'] = author.text.strip() if author else ''

		data['image_url'] = image_url

	return data


def crawl(request):
	try:
		r = requests.get(SOURCE_URL)
	except ConnectionError as e:
		print(e)
		return render(request, 'websitecontent/connectionfailed.html')

	dir_name = 'save_json'
	if r.ok:
		s = bs4.BeautifulSoup(r.content, 'lxml')
		links = s.select('.box-category-middle > .box-category-item')
		for a in links:
			id_ = a.attrs['data-id']
			link = a.select_one('.box-category-item a')
			image = a.select_one('a.box-category-link-with-avatar img')
			image_url = image.attrs['src']

			article = get_article_url(urljoin(BASE_URL, link.attrs['href']), image_url)
			if article == False:
				continue

			# tao thư mục
			if not os.path.isdir(dir_name):
				os.mkdir(dir_name)

			#tạo tên tệp
			file_name = id_ + '.json'
			file_name = os.path.join(dir_name, file_name)

			f = codecs.open(file_name, encoding='utf-8', mode='w')
			json.dump(article, f, ensure_ascii=False, indent=2)
	else:
		return HttpResponse('Lỗi')

	if not os.path.isdir(dir_name):
		return HttpResponse('Không tồn tại thư mục chứa dữ liệu')
	
	data = []
	for fn in glob.glob(f'{dir_name}/*.json'):
		f = codecs.open(fn, mode='r', encoding='utf-8')
		d = json.load(f)
		d['post_name'] = fn.split('\\')[-1].replace('.json', '')
		data.append(d)
		print(fn)

	context = {'data': data,
			   'nav' : 'article'}
	return render(request, 'websitecontent/testing_crawl.html', context)


def article_detail(request, post_name):
	dir_name = 'save_json'
	fn = f'{dir_name}/{post_name}.json'
	if not os.path.isfile(fn):
		return HttpResponse(f'Không tồn tại file {post_name}')

	f = codecs.open(fn, mode='r', encoding='utf-8')
	d = json.load(f)

	context = {'d': d}
	return render(request, 'websitecontent/article.html', context)


class AddBlogs(LoginRequiredMixin, View):
	def get(self, request):
		initial_data = {
			'author': request.user
		}
		f = AddBlogsForm(initial=initial_data)
		context = { 'fm': f }
		return render(request, 'websitecontent/add_blog.html', context)

	def post(self, request):
		f = AddBlogsForm(request.POST, request.FILES)
		if f.is_valid():
			f.save()
			return redirect('nameInforProfile')
		return HttpResponse('Upload Lỗi')


