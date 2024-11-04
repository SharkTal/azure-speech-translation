# This is a project based on Microsoft AI Service/Speech Service/Quickstart: Recognize and translate speech to text

## Prerequisites

An Azure subscription. 

You can create one for free.

Create a Speech resource in the Azure portal.

Get the Speech resource key and region. After your Speech resource is deployed, select Go to resource to view and manage keys.


## Set up the environment

### Set environment variables

You need to authenticate your application to access Azure AI services. This article shows you how to use environment variables to store your credentials. You can then access the environment variables from your code to authenticate your application. For production, use a more secure way to store and access your credentials.

### Clone the repo

```Bash
git clone https://github.com/SharkTal/azure-speech-translation.git
```

### on macOS

Edit your .bash_profile file, and add the environment variables:

```Bash

export SPEECH_KEY=your-key

export SPEECH_REGION=your-region

 ```

### Run this command to install the Speech SDK:

```Bash
pip install azure-cognitiveservices-speech
```

### Run your new console application to start speech translation

```Bash
python speech_translation.py
```

## Notes

### Audio format

So far only wav format is tested, other formates may not work

Run

```Bash
convert_mp3_to_wav.py
```

to convert

### Language codes with utf-8

For English, `en` works, `en-US` doesn't

For Chinese, `zh-CN` works, `zh-Hans` doesn't

### More details see: 

https://learn.microsoft.com/en-gb/azure/ai-services/speech-service/get-started-speech-translation?tabs=macos%2Cterminal&pivots=programming-language-python

