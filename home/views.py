from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect,get_object_or_404
from django.views import View
from .forms import Cash_in_form, Cash_out_form, Sales_form  # Import your forms
from .models import Cash_in,Cash_out,Sales
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.apps import apps

# Dictionary mapping slugs to information and form classes
temp = {
    "cash_in_page": {
        "title": "CASH IN",
        "name": "Transactions",
        "forms": Cash_in_form,
        "slug": "cash_in_page",
        "model": Cash_in,
        "dataTitle": "Transactions"
    },
    "cash_out_page": {
        "title": "CASH OUT",
        "name": "Transactions",
        "forms": Cash_out_form,
        "slug": "cash_out_page",
        "model": Cash_out,
        "dataTitle": "Transactions"
    },
    "sales_page": {
        "title": "ADD SALES",
        "name": "Sales",
        "forms": Sales_form,
        "slug": "sales_page",
        "model": Sales,
        "dataTitle": "Sales"
    }
}

def home_page(request):
    return render(request, "home/home.html")

class Features(View):

    def get(self, request, feature):
        # Using the feature parameter instead of slug
        info = temp.get(feature)

        if not info:  # Handle case where feature is not found
            return HttpResponse("Page not found", status=404)

        form_class = info["forms"]
        form = form_class()  # Instantiate the form

        return render(request, "home/feature123.html", {
            "form": form,
            "info": info
        })
    
    def post(self, request, feature):
        info = temp.get(feature)

        if not info:  # Handle case where feature is not found
            return HttpResponse("Page not found", status=404)

        form_class = info["forms"]
        form = form_class(request.POST)  # Instantiate the form with POST data

        if form.is_valid():  # Validate the form data
            # Here you would typically save the data or process it as needed
            # For example, if using a ModelForm, you might call form.save()
            # For simple forms, you might just process the cleaned data
            # Example: print(form.cleaned_data)
         form.save()
         return redirect('feature123_page', feature=feature)
            # Redirect to a success page (you could change this to any URL)
          # Change to your success URL

        # If the form is not valid, re-render the form with error messages
        return render(request, "home/feature123.html", {
            "form": form,  # Pass the form with errors back to the template
            "info": info
        })


def previous_transaction(request,feature):
     info = temp.get(feature)
     title=info["dataTitle"]
     model=info["model"]
     slug=info["slug"]
     data=model.objects.all().order_by('-id')
     return render(request, "home/previous.html",{"data": data, "title":title ,"slug" : slug})

def soon(request):
    return render(request,"home/soon.html")

@csrf_exempt
def delete_object(request, slug, object_id):
    """
    Delete an object based on the page slug and model_id.
    """
    if request.method == 'DELETE':
        # Look up the page data by slug in the temp dictionary
        page_data =temp[slug]        
        if not page_data:
            return JsonResponse({"error": "Invalid page slug"}, status=400)

        model = page_data["model"]  # Get the model from the temp dictionary

        # Try to get the object and delete it
        obj = get_object_or_404(model, id=object_id)
        obj.delete()

        return JsonResponse({"message": "Transaction deleted successfully"}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=400)
