from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autenticar al usuario automáticamente después del registro
            return redirect('home')  # Redirigir a la página principal después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Diccionario que mapea categorías con sus respectivas imágenes en AWS S3
categories_images = {
    'Personal': [
        'https://mariaemegeweb.s3.amazonaws.com/photos/carlos.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/India.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/ginger.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/Manitas.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/samarillo.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/sazul.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/sboom.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/safari.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/scuervos.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/sburbuja.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/sflamenco.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/sllanto.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/sojeras.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/spelos.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/srojo.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/ssirena.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/strenza.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/City.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/svampiro.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/Niña_tropical.jpg'
    ],
    'Sports': [
        'https://mariaemegeweb.s3.amazonaws.com/photos/Lebron.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/Jordan.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/jordanblue.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/Kobe.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/Kyrie.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/lebrontunes.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/lebronyjordan.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/magic.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/mcgregor.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/nbaplayers.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/pau.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/kobe2.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/jokic.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/iverson.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/kingjames.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/dreamteam.jpg'
    ],
    'Anime & Videogames': [
        'https://mariaemegeweb.s3.amazonaws.com/photos/babyyoda.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/ff.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/skull.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/sith.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/silver.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/pentiment.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/kratos.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/jinx.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/lou.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/ciri.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/conan.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/farwest.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/fallout.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/manofmedan.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/ellie.jpg'
    ],
    'Custom Shoes & More': [
        'https://mariaemegeweb.s3.amazonaws.com/photos/prince.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/akira.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/checo.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/madmax.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/balon.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/astarion.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/diablo.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/goku.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/zapaswomans.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/xbox.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/pselden.jpg',
        'https://mariaemegeweb.s3.amazonaws.com/photos/faker.jpg'
    ]
}

def category_view(request, category_name):
    images = categories_images.get(category_name, [])
    return render(request, 'category.html', {'images': images, 'category_name': category_name})

# Vista para mostrar la imagen individual en detalle
def image_detail(request, image_name):
    # Buscar la imagen en el diccionario
    image_url = None
    for category, images in categories_images.items():
        if any(image_name in url for url in images):
            image_url = f'https://mariaemegeweb.s3.amazonaws.com/photos/{image_name}'
            break
    
    return render(request, 'image_detail.html', {'image_url': image_url})

# Añadir al carrito
@login_required
def add_to_cart(request, image_name):
    cart = request.session.get('cart', [])
    image_url = f'https://mariaemegeweb.s3.amazonaws.com/photos/{image_name}'
    
    if image_url not in cart:
        cart.append(image_url)
        request.session['cart'] = cart
        messages.success(request, "Imagen añadida al carrito.")
    else:
        messages.info(request, "Esta imagen ya está en tu carrito.")
    
    return redirect('image_detail', image_name=image_name)