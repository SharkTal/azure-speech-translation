Prerequisites
An Azure subscription. You can create one for free.
Create a Speech resource in the Azure portal.
Get the Speech resource key and region. After your Speech resource is deployed, select Go to resource to view and manage keys.

Set up the environment
Set environment variables
You need to authenticate your application to access Azure AI services. This article shows you how to use environment variables to store your credentials. You can then access the environment variables from your code to authenticate your application. For production, use a more secure way to store and access your credentials.

on macOS
Bash
Edit your .bash_profile file, and add the environment variables:

export SPEECH_KEY=your-key
export SPEECH_REGION=your-region

pip install azure-cognitiveservices-speech

python speech_translation.py
