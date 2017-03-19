import random
import string

from django.shortcuts import render

def generate_key():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(4))

def gen(request):
    numb = generate_key()
    context = {

        'numb' : numb

          }
    return render(request, 'generator1/gen.html', context)
