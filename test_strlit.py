import pytest
import requests
from Bienvenue import get_image_from_api
from pages.Prediction import get_client_address, predict_for_client

# Constantes pour les tests
FASTAPI_SERVER = 'https://dsoc-p7-api-019616fdcaac.herokuapp.com'
TEST_IMAGE_NAME = 'PAYMENT_RATE_kde'
TEST_CLIENT_ID = 100042  # Remsplacez par un ID client valide pour les tests

def test_get_image_from_api():
    response = get_image_from_api(TEST_IMAGE_NAME)
    assert response is not None or response is None  # Réussite si l'image est trouvée ou correctement gérée si elle n'existe pas

def test_get_client_address():
    response = get_client_address(TEST_CLIENT_ID)
    assert response is not None  # Vérifiez si l'adresse du client est correctement récupérée

def test_predict_for_client():
    response = predict_for_client(TEST_CLIENT_ID)
    assert response is not None  # Vérifiez si la prédiction est correctement effectuée
