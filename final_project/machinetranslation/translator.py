"""Module providing translation."""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """E to F"""
    french_text = language_translator.translate(english_text, model_id='en-fr')
    return french_text

def french_to_english(french_text):
    """F to E"""
    english_text = language_translator.translate(french_text, model_id='fr-en')
    return english_text
