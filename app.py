
from flask import Flask, render_template
import requests

app = Flask(__name__)

# CoinGecko API (Anahtarsız/Ücretsiz)
# USD cinsinden piyasa verilerini çeken adres
API_URL = "https://api.coingecko.com/api/v3/coins/markets"

@app.route('/')
def home():
    try:
        # Hangi coinleri istiyoruz?
        parametreler = {
            'vs_currency': 'usd',
            'ids': 'bitcoin,ethereum,tether,dogecoin,ripple,solana', # İstediklerini ekle
            'order': 'market_cap_desc'
        }
        
        response = requests.get(API_URL, params=parametreler)
        
        if response.status_code == 200:
            veri_listesi = response.json()
            return render_template('index.html', coinler=veri_listesi)
        else:
            return "Borsa verilerine şu an ulaşılamıyor (API Yoğunluğu)."
            
    except Exception as e:
        return f"Hata: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
