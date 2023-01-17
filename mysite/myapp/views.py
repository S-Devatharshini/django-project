from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from django.core.paginator import Paginator
from django.views.generic import DetailView

#Notes:
#It is responsible for view of the app
#We write all our views here

#The index function accepts a request and provide the response.
#once we define the function add a url pattern to the urls.py file.

def index(request):
    return HttpResponse("Hello world")

#Function based view for products

def products(request):
    page_obj = products = Product.objects.all()
    product_name=request.GET.get('product_name')
    if product_name!='' and product_name is not None:
        page_obj=products.filter(name__icontains=product_name)
    
    paginator=Paginator(page_obj,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'page_obj':page_obj
    }
    return render(request,'myapp/index.html',context)

#class based view for above products view using Listview
#from django.views.generic import ListView
#and in urls.py add path('products/',views.ProductListView.as_view(),name="products"),
#modify {% for x in products %}

'''class ProductListView(ListView):
    model=Product
    template_name='myapp/index.html'
    context_object_name='products'
    paginate_by= 3
'''

#Function based view for products

def product_details(request,id):
    productone=Product.objects.get(id=id)
    contextone={
        'product':productone
    }
    return render(request,'myapp/detail.html',contextone)

#class based view for above product_detail view using Detailview
#from django.views.generic import ListView
#and in urls.py add path('products/',views.DetailListView.as_view(),name="products_details"),

'''class ProductDetailView(DetailView):
    model=Product
    template_name='myapp/detail.html'
    context_object_name='product'
'''


#Function based view for products
@login_required
def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        image=request.FILES.get('upload')
        seller_name=request.user
        product=Product(name=name,price=price,description=description,image=image,seller_name=seller_name)
        product.save()
    return render(request,'myapp/addproduct.html')

#from django.views.generic.edit  import CreateView
#class based view for above add_product view using Createview
#and in urls.py path('products/add/',views.ProductCreateView.as_view(),name="add_product"),
#create a product_form.html(model_form.html) file and render the form 

'''class ProductCreateView(CreateView):
    model=Product
    fields= ['name','price','decsription','image','seller_name']
    product_form.html
'''

@login_required
def update_product(request,id):
    product=Product.objects.get(id=id)
    if request.method=='POST':
        product.name=request.POST.get('name')
        product.price=request.POST.get('price')
        product.description=request.POST.get('description')
        product.image=request.FILES['upload']
        product.save()
        return redirect('/myapp/products')
    contextupdate= {
        'product':product,
    }
    return render(request,'myapp/updateproduct.html',contextupdate)

#from django.views.generic.edit  import UpdateView
#class based view for above update_product view using Updateview
#and in urls.py path('products/update/<int:pk>',views.ProductUpdateView.as_view(),name="add_product"),
#create a product_update_form.html(model_update_form.html) file and render the form 
'''class ProductCreateView(CreateView):
    model=Product
    fields= ['name','price','decsription','image','seller_name']
    template_name_suffix='_update_form'
'''

@login_required
def delete_product(request,id):
    product=Product.objects.get(id=id)
    context={
        'product':product
    }
    if request.method=='POST':
        product.delete()
        return redirect('/myapp/products')
    return render(request,'myapp/deleteproduct.html',context)

#from django.views.generic.edit  import DeleteView
#from django.urls import reverse_lazy
#class based view for above delete_product view using Deleteviewview
#and in urls.py path('products/update/<int:pk>',views.ProductDeleteView.as_view(),name="delete_product"),
#create a product_confirm_delete.html file and render the form 
'''class ProductCreateView(CreateView):
    model=Product
    success_url=reverse_lazy('myapp:products')
'''

@login_required   
def my_listings(request):
    products=Product.objects.filter(seller_name=request.user)
    context={
        'products':products
    }
    return render(request,'myapp/mylistings.html',context)