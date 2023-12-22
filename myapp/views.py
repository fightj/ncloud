# myapp/views.py
from django.shortcuts import render
from math import gcd

from myapp.forms import GCDLCMForm


def gcd_lcm(request):
    if request.method == 'POST':
        form = GCDLCMForm(request.POST)
        if form.is_valid():
            A = form.cleaned_data['A']
            B = form.cleaned_data['B']

            # 최대공약수(GCD) 계산
            gcd_result = gcd(A, B)

            # 최소공배수(LCM) 계산
            lcm_result = A * B // gcd_result

            return render(request, 'gcd_lcm.html', {'form': form, 'gcd_result': gcd_result, 'lcm_result': lcm_result})
    else:
        form = GCDLCMForm()

    return render(request, 'gcd_lcm.html', {'form': form})
