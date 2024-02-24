from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.


def Inputs(request):
  return  render(request, 'Inputs.html')

def Payroll(request):
  name = str(request.GET.get("Name"))
  rate = float(request.GET.get("Rate"))
  hours = int(request.GET.get("Hours"))

  if hours > 40:
    gross = (hours-40) * rate * 1.5 + 40 * rate
  else:
    gross = hours * rate

  deduction = gross * 0.14 # tax is 14%
  net = gross - deduction

  context = {
    "Name": name,
    "Rate": rate,
    "Hours": hours,
    "Gross": gross,
    "Tax": format(deduction, ".2f"),
    "Net": format(net, ".2f")
  }

  return  render(request,'payroll.html',context)

def Trial(request):
  return render(request, 'trialcheck.html')
