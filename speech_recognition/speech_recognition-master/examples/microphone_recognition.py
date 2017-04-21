#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""
{
  "type": "service_account",
  "project_id": "share-time-149716",
  "private_key_id": "92da03126c4d94cd78fd5a141104c5758d0f559f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDIQnGsgcvDQPy7\nd1iXQgbH2rAgPXhaEMguASRa0lSebZtaklScGKGDzcmaqMBx8uiNBOHStmEON/fb\n+Io7M8DSAdTCsu514oPE+x17WPCjbNtNPSHk5g5brvRpYM8kHt+R++YVDc5j7yQ+\nfcUzP7j7z473vb2iweIufWmjDU2IPZx9DB39XcGfc7mYgQlnGwfbhXTVHTXeOMPE\nOQMG76OFIPOopgoBgMMpejP4oBeWVpX/kna+oFk9oID8FGqu4iwJFlsrhGyko09R\nIZ0avp63WDIOs7BDP+VDJ97V6boKaNCvhh4HZVSuVFHMjMjioSVdMu9t8FLGsJRu\nqjxq/FMfAgMBAAECggEAHBvvdsZVQpfpoaqz3a9f4keY9z2JmiLG5mY0oybox8Ac\n0U6+35Y5fZWyGapcMOJmr/yicgA1iVhjyxWM2Zh/FTs6kQWqoRNlaY3R6pFmXZoX\nAjV1f3qnQ0lAd1YmXSyUNxqDhisE8FQN41OmDXaBUZ8lszKH3sOWKu5hmIhyfI/h\nk0/uC40BjCfyzNC/Nzrrick5xjlomSh6PfUBSZp5Fr8mkjkwr+WLd9MRuMA4+YKr\nwdXPkpmg1rbbQJktvoGJwbaP7Fv0SNdDRnMmh/BwULNZrmQSFul1AV19bO/i/UyX\nMlxAS0f8OZbV2luiak/C8f2h1YMR0PRlz2LpFR/ASQKBgQD1xkoCeBbPiRJwHhGb\nPG0DWXxsUvQmJaVRdOGmOytmA32XyMY+P8Borp+vVvCQivPMAYSHi/FIqHPdyaLh\n3JarcS58KdiTosDySA25D28NsHOqLpwRDs6xsnEmteutEcE0odSPrkkC4mzrUZZg\nPYg8Oey+mq946C18si90QJtTDQKBgQDQl2F5kdOee/hme5bAg4GqGW6mSXen3/O5\nX5YqfehJmx93xtWrKqICcjYsB1jR1CesLF/EuCWMhie2cS+nRnk+/kCZttea3uNH\nTxV6Q2MmsCF+ZJDVBt7n9WK8nxRJxdKXfapboO4GjvTbd/GEZFyjvScxp/QzVs+2\nesFJrmej2wKBgFO0JKCSpbIozM7Cbtyfx8DMSUPbPKuBRrxnQjKLFEy6A5weFOY+\ncBk238unoGaZ7E4edjRzxMkqFcwDUCX8KpRZB6vh1JDzbSMWxxWv2/Kdlcbv+NcW\nY+7BByhX7NwUn+h89Re6E8OXueCq+LvuOOfKEocXx4s2B8fgJ6lAF6ZBAoGBAL8V\n/qjEy20DOnJ/w4GGt1EhTTkuUlxKj9aA12sDvrk3TyOF1hWgz5uYD0JUVKycQt+6\nIt1uqI9MErNSiwodSFNJzdpDIs5wYxrfOtivRPSbI4PLEtbkHW23YQVUYdyXSa2X\n5GleSs9dRLiM74aN/kPNs0sNBmvFmjEb0VfzWmRDAoGAGYivgOmOLZ1fwYOhGRJ5\nfaH5MYfdWPK2Cq5CAKbCVTJOIPGoiI8YfHGbp1QAZImS5Qhxyfm5QBeTy8rvx5yV\n5DneLApcijiswziKTsrlp/LGgi0AyYq6qmzYmM4u4+bFI/HjaoVpPnNaZ/Z++wsf\nRN/dlISHbC26uoeEVbHqxPU=\n-----END PRIVATE KEY-----\n",
  "client_email": "google-speech@share-time-149716.iam.gserviceaccount.com",
  "client_id": "104590038847296109518",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/google-speech%40share-time-149716.iam.gserviceaccount.com"
}
"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE" # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE" # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))
