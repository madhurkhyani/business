from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect,get_object_or_404
from django.views import View
from .forms import Cash_in_form, Cash_out_form, Sales_form  # Import your forms
from .models import Cash_in,Cash_out,Sales
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.apps import apps
from client.models import ClientData

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
            "info": info,
            "clients": ClientData.objects.all()
        })
    
    def post(self, request, feature):
        # Using the feature parameter instead of slug
        info = temp.get(feature)

        if not info:  # Handle case where feature is not found
            return HttpResponse("Page not found", status=404)

        form_class = info["forms"]
        form = form_class(request.POST)  # Instantiate the form with POST data

        if form.is_valid():  # Validate the form data
            # Save the Cash_in object
            cash_in = form.save()

            # Update the ledger in the ClientData model
            if feature!="sales_page":
                try:
                    client = cash_in.client
                    if hasattr(client, 'ledger'):
                        if client.ledger is None:
                            client.ledger = 0  # Initialize if null
                        print(f"Client Ledger Before Update: {client.ledger}")
                        print(f"Cash In Amount: {cash_in.amount}")
                        if feature=="cash_in_page":
                            client.ledger += cash_in.amount
                        else:
                            client.ledger -= cash_in.amount
                        client.save()
                        print(f"Client Ledger After Update: {client.ledger}")
                    else:
                        return HttpResponse("Ledger attribute not found in ClientData model", status=500)
                except ClientData.DoesNotExist:
                    return HttpResponse("Client not found", status=404)
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