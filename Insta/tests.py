from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile,Image,Comment
import datetime as dt
# Create your tests here.
class ImageTestCLass(TestCase):
    '''
    setup self instance of image
    '''
    def setUp(self):
        self.post = Image(Image_name='Music',Image_caption='music is a southing sound that moves souls')
    
    ''' 
    test instance of image
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))


    '''
    test save image
    '''

    def test_save_image(self):
        self.post.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

class profileTestCLass(TestCase):
    '''
    setup self instance of image
    '''
    def setUp(self):
        self.prof = Profile(Bio='Live the moment')
    
    ''' 
    test instance of image
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_profile(self):
        self.prof.save_profile()
        bio = Profile.objects.all()
        self.assertTrue(len(bio)>0)

class CommentTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.comment = Comment(name='lovely')
    '''
    test instance of comment
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Commment))
        '''
        test for save instance of comment
        '''
    def test_save_comment(self):
        self.comment.save_comment()
        name= Comment.object.all()
        sel.assertTrue(len(name)>0)