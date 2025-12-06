import random
from django.http import HttpResponse

generated_qr_urls = []

def generateQRCode(request):
    base_url = "https://127.0.0.1:8000/QRCode/qr_token/"
    
    # Generate a random number between 0 and 9999 (for example)
    random_number = random.randint(0, 9999999999999999999)

    # Combine into full URL
    url = base_url + str(random_number)

    # Add to list
    generated_qr_urls.append(url)

    return HttpResponse(f"QR URL added: {url} (Total now: {len(generated_qr_urls)})")




def  read_QRCode_url(request, url_token_numbers):
    full_url = f"https://127.0.0.1:8000/QRCode/qr_token/{url_token_numbers}"

    respone = ""
    if generated_qr_urls:
        for i in generated_qr_urls:
            if full_url == i : 
                respone = "access granter, valid QR CODE URL"
            else: 
                respone = "access denied, QR CODE URL donsn't exist"

    return HttpResponse(respone)


