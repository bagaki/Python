import uuid
from django.db import models

# Create your models here.
class Users(models.Model):
	userAccount = models.CharField(max_length=20, unique=True)
	userPasswd = models.CharField(max_length=20)
	userName = models.CharField(max_length=20)
	userAddress = models.CharField(max_length=100)
	userImg = models.CharField(max_length=150)
	# token验证值，每次登录之后都会更新
	userToken = models.CharField(max_length=50)

	@classmethod
	def createuser(cls, account, passwd, name, address, img, token):
		u = cls(userAccount = account, userPasswd = passwd, 
			userName = name, userAddress = address, userImg = img, 
			userToken = token)
		return u


class Comics(models.Model):
	comicsNum = models.CharField(max_length=20, unique=True)
	comicsName = models.CharField(max_length=120)
	comicsAuthor = models.CharField(max_length=100)
	comicsImg = models.CharField(max_length=150)
	orderid = models.CharField(max_length=20, default='0')
	isDelete = models.BooleanField(default=False)

	@classmethod
	def createcomics(cls, comicsNum, comicsName, comicsAuthor, comicsImg,
		orderid, isDelete):
		c = cls(comicsNum=comicsNum, comicsName=comicsName, 
			comicsAuthor=comicsAuthor, comicsImg=comicsImg,
			orderid=orderid, isDelete=isDelete)
		return c


class MainPage(models.Model):
	ImgId = models.CharField(max_length=20, unique=True)
	ImgName = models.CharField(max_length=120)
	img = models.CharField(max_length=150)



class BookKeep(models.Model):
	book = models.ForeignKey(Comics)



class Search(models.Model):
	sid = models.CharField(max_length=20, unique=True)
	sname = models.CharField(max_length=100)
	sAuthor = models.CharField(max_length=100)
	sImg = models.ForeignKey(Comics)


class History(models.Model):
	hid = models.CharField(max_length=20, unique=True)
	hname = models.CharField(max_length=100)
	hImg = models.CharField(max_length=20)






# def make_secret_key():
# 	return uuid.uuid4().hex


# class UserProfile(models.Model):
# 	user = models.OneToOneField(Users, related_name='comics_profile')
# 	secret_key = models.CharField(max_length=32, blank=False, default=make_secret_key,
# 		help_text = 'Secret key for feed and API access')
# 	comics = models.ManyToManyField(Comics, through = 'Subscription')

# 	def generate_new_secret_key(self):
# 		self.secret_key = make_secret_key()


# class Comics(models.Model):
# 	name = models.CharField(max_length=100, help_text='Name of the comics')
# 	slug = models.SlugField(max_length=100, unique=True, 
# 		verbose_name='Short Name',
# 		help_text='For file paths and URLs')

# 	url = models.URLField(verbose_name='URL', blank=True,
# 		help_text='URL to the official website')
# 	active = models.BooleanField(
# 		default=True,
# 		help_text='Wheter the comic is still being crawled')