
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('PZCXW0hrOngpygiym70VOqpR4Y3qkzmDklqwG0O-4CoT')
tts = TextToSpeechV1(
    authenticator=authenticator
)


tts.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/431825e3-9c9d-44d9-abc3-ac5eb3088c86')


with open('./recording.mp3', 'wb') as audio_file:
     res = tts.synthesize('hello thanks for helping', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content)  

print("completed!")
