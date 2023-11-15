from django.db import models
from django.utils.html import mark_safe
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField


STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered")
)


STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published")
)


RATING = (
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★")
)



#create a folder to store the user images
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Cathegory(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="Cat", alphabet = "abcdefgh12345678")
    title = models.CharField(max_length=100, default="food")
    image = models.ImageField(upload_to="cathegory", default="cathegory.jpg")
    
    class Meta:
        verbose_name_plural = "Cathegories"
        
    def cat_image(self):
        return mark_safe('<img src"%s" width="50px" height="50px" / >' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class Tags(models.Model):
    pass

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet = "abcdefgh12345678")
    
    title = models.CharField(max_length=100, default="ABCD")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    description = models.TextField(null=True, blank=True, default="This is the best vendor")
    
    address = models.CharField(max_length=100, default="123 Main Street.")
    contact = models.CharField(max_length=100, default="+237 987654321")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentication_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
        
    class Meta:
        verbose_name_plural = "Vendors"
        
    def vendor_image(self):
        return mark_safe('<img src"%s" width="50px" height="50px" / >' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="pdt", alphabet = "abcdefgh12345678")
    
    cathegory = models.ForeignKey(Cathegory, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
     
    title = models.CharField(max_length=100, default="fresh product")
    image = models.ImageField(upload_to="user_directory_path", default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is the description")

    price = models.DecimalField(max_digits=999999999999999, decimal_places=2, default="199")
    old_price = models.DecimalField(max_digits=999999999999999, decimal_places=2, default="299")
    
    specifications = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    
    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet = "1234567890")
    
    date = models.DateField(auto_now_add=True)
    update = models.DateField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Products"
        
    def product_image(self):
        return mark_safe('<img src"%s" width="50px" height="50px" / >' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Images"
   
   
   
###############################  Cart, Order, OrderItems #############################
###############################  Cart, Order, OrderItems #############################
###############################  Cart, Order, OrderItems #############################
  
   
   
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999999, decimal_places=2, default="199")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True) 
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="process")

    class Meta:
        verbose_name_plural = "Cart Orders"
        
        
class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999999999999999, decimal_places=2, default="199")
    total = models.DecimalField(max_digits=999999999999999, decimal_places=2, default="199")

    class Meta:
        verbose_name_plural = "Cart Order Items"
        
    def order_img(self):
        return mark_safe('<img src"/media/%s" width="50px" height="50px" / >' % (self.image))
    
    
    
###############################  Product Review, Wishlists, Address #############################
###############################  Product Review, Wishlists, Address #############################
###############################  Product Review, Wishlists, Address #############################

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date =  models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Reviews"
            
    def __str__(self):
        return f"{self.user} on {self.product}"
    
    def get_rating(self):
        return self.rating
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date =  models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Wishlist"
            
    def __str__(self):
        return f"{self.user} on {self.product}"


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Addresses"
    