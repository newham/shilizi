import os

from django.shortcuts import render


# Create your views here.
def bp_neural_network(request):
    img_dir = 'static/img/mnist/'
    context = {
        'img_dir': img_dir,
        'imgs': os.listdir(img_dir),
    }
    # print(context)
    return render(request, 'bp_neural_network.html', context)
