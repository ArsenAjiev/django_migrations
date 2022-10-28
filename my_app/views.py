from django.shortcuts import render


from django.utils.crypto import get_random_string

print(get_random_string(32))