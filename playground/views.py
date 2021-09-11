from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.db.models.aggregates import Max, Min, Avg, Sum
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from django.db import transaction, connection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Customer, Product, Order, OrderItem
from tags.models import TagItem


def say_hello(request):
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)

    # queryset_or = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    # queryset_f = Product.objects.filter(title = F('collection__title'))
    # queryset_sort = Product.objects.order_by('unit_price','-title').reverse() 
    # # product2 = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product3 = Product.objects.latest('unit_price')
    # queryset = Product.objects.all()[5:10]
    # queryset = Product.objects.values_list('id', 'title', 'unit_price', 'collection_id', 'collection__title')
    # queryset_odered = Product.objects.values_list('id', 'title','unit_price', 'orderitem__id').order_by('title')
    # queryset_order_item = OrderItem.objects.values_list('product_id', 'product__title').order_by('product__title')

    # queryset_pro_item = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # queryset_only = Product.objects.only('id', 'title', 'unit_price')
    # queryset_defer = Product.objects.defer('description')

    # queryset_order_item_all = OrderItem.objects.values('product__id', 'product__title').order_by('product__title').distinct()
    # queryset = Product.objects.prefetch_related(
    #     'promotions').select_related('collection').all()
    


    # queryset_order_item = OrderItem.objects.select_related('order', 'product')
    
    # queryset_orders = Order.objects.select_related('customer').prefetch_related(queryset_order_item).filter(id__in=
    #     queryset_order_item.values('order_id')
    #     )
   

    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product__collection').prefetch_related('orderitem_set__product__promotions').order_by('-placed_at')[:5]
  

    # result = Product.objects.filter(collection__id=6).aggregate(countq = Count('id'), min_price = Min('unit_price'), max_price = Max('unit_price'), average = Avg('unit_price'), sum = Sum('unit_price'))

    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name') , Value(' '), F('last_name'), function='CONCAT')
    #     ) 

    # queryset = Customer.objects.annotate(
    #     full_name2=Concat('first_name', Value(' '), 'last_name')
    #     ) 

    # discounted_price = ExpressionWrapper(
    #     F('unit_price') * 0.8, output_field = DecimalField())

    # queryset = Product.objects.annotate(
    #     discounted_price =discounted_price
    # )


    # queryset = TagItem.objects.get_tags_for(Product, 2)

    # queryset = Product.objects.all()
    # qs1 = queryset[0]
    # list(queryset)

    # collection = Collection(pk=11)
    # collection.delete()

    # Collection.objects.filter(id__gt=5).delete()

    # Collection.objects.filter(pk=11).update(featured_product=None)
    


    # # ...

    # with transaction.atomic():
            
    #     order = Order()
    #     # order.customer = Customer(pk=1)
    #     order.customer_id = 1 
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = -1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # queryset = Product.objects.raw('SELECT id, title FROM store_product')
    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * FROM store_product')
    #     cursor.callproc('get_customers', [1, 2, 'a'])

    return render(request, 'hello.html', {'name' : 'Ruwan Senavirathna' })

