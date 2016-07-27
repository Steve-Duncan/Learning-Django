from django.shortcuts import render, redirect
from .models import Product

#########################################################################
#index page
def index(request):
	#get all products from database
	products=Product.objects.all()
	#build return context
	context={
		'products' : products
	}
	#render the index page, passing the context
	return render(request, 'product_mgmt/index.html', context)

#########################################################################
#show products
def show(request, id):
	#get product from database matching id passed into function
	product=Product.objects.get(id=id)
	#build return context
	context={
		'id' : id,
		'name' : product.name,
		'description' : product.description,
		'price' : product.price
	}
	#render the show product page, passing the context
	return render(request, 'product_mgmt/show.html', context)
#########################################################################
#show create product page
def new(request):
	#show the create page
	return render(request, 'product_mgmt/create.html')
#########################################################################
#edit a product
def edit(request, id):
	#get product from database matching id passed into function
	product=Product.objects.get(id=id)
	#build return context
	context={
		'id' : id,
		'name' : product.name,
		'description' : product.description,
		'price' : product.price
	}
	#render the edit product page, passing the context
	return render(request, 'product_mgmt/edit.html', context)
#########################################################################
#create a new product record
def create(request):
	if request.method == 'POST':
		#get info from form
		name=request.POST.get('name')
		description=request.POST.get('description')
		price=request.POST.get('price')

		#send to model to add to database
		Product.objects.create(name=name,description=description,price=price)

	#return to products page
	return redirect('/products')
#########################################################################
#update a product record
def update(request, id):
	
	#get product from database matching id passed into function
	product=Product.objects.get(id=id)

	#get info from form
	product.name=request.POST.get('name')
	product.description=request.POST.get('description')
	product.price=request.POST.get('price')
	#save changes to database
	product.save()
	#return to products page
	return redirect('/products')
#########################################################################
#remove product record
def destroy(request, id):
	#get product from database matching id passed into function
	product=Product.objects.get(id=id)
	product.delete()
	#return to products page
	return redirect('/products')

#########################################################################