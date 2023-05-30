from django.shortcuts import render

# Create your views here.
import math
import numpy as np
from scipy.stats import norm


def call_TwoStep_Binomial(request):
    r = float(request.GET['rate'])
    su = float(request.GET['increment'])
    sd = float(request.GET['decrement'])
    s0 = float(request.GET['InitialStockPrice'])
    k0 = float(request.GET['StrikePrice'])
    t0 = float(request.GET['Maturity'])
    e = 2.718281828459045
    tu = t0 / 2
    p = (pow(e, r * tu) - sd) / (su - sd)
    c0 = (max(s0 * pow(su, 2) - k0, 0) * pow(p, 2) + max(s0 * pow(sd, 2) - k0, 0) * pow(1 - p, 2) + 2 * max(
        s0 * su * sd - k0, 0) * p * (1 - p)) * pow(e, -r * t0)
    return render(request, 'output.html', {'result': c0})


def call_nStep_binomial(request):
    n = int(request.GET['steps'])
    r = float(request.GET['rate'])
    su = float(request.GET['increment'])
    sd = float(request.GET['decrement'])
    s0 = float(request.GET['InitialStockPrice'])
    k0 = float(request.GET['StrikePrice'])
    t0 = float(request.GET['Maturity'])
    e = 2.718281828459045
    tu = t0 / n
    p = (pow(e, r * tu) - sd) / (su - sd)
    c0 = float(0)
    for j in range(0, n + 1):
        a = math.factorial(n)
        b = math.factorial(n - j) * math.factorial(j)
        c = a / b
        c0 = c0 + c * pow(p, j) * pow(1 - p, n - j) * max(s0 * pow(su, j) * pow(spyd, n - j) - k0, 0)

    c0 = c0 * pow(e, -r * t0)

    return render(request, 'output.html', {'result': c0})


def call_Black_Scholes(request):
    sigma = float(request.GET['volatility'])
    r = float(request.GET['rate'])
    s0 = float(request.GET['InitialStockPrice'])
    k0 = float(request.GET['StrikePrice'])
    t0 = float(request.GET['Maturity'])

    t0 = t0 / 365

    d1 = (np.log(s0 / k0) + (r + sigma ** 2 / 2) * t0) / (sigma * np.sqrt(t0))
    d2 = d1 - sigma * np.sqrt(t0)

    price = s0 * norm.cdf(d1, 0, 1) - k0 * np.exp(-r * t0) * norm.cdf(d2, 0, 1)

    return render(request, 'output.html', {'result': price})
