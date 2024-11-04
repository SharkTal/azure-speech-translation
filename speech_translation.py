import os
import time
import azure.cognitiveservices.speech as speechsdk


def recognize_from_long_audio_file():
    try:
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_translation_config = speechsdk.translation.SpeechTranslationConfig(
            subscription=os.environ.get("SPEECH_KEY"),
            region=os.environ.get("SPEECH_REGION"),
        )
        speech_translation_config.speech_recognition_language = "zh-CN"  # zh-Hans doesn't work, be careful with the usage of language codes

        to_language = "en" #en-US doesn't work, only en works
        speech_translation_config.add_target_language(to_language)

        audio_config = speechsdk.audio.AudioConfig(
            filename="/Users/tal/Desktop/Speech_Translation_Azure_AI/test_audio.wav" #choose the audio file and path you want to translate
            # only wav format is tested, other formats may not work
        )
        translation_recognizer = speechsdk.translation.TranslationRecognizer(
            translation_config=speech_translation_config, audio_config=audio_config
        )

        translations = []

        def recognized_callback(evt):
            if evt.result.reason == speechsdk.ResultReason.TranslatedSpeech:
                print("Recognized: {}".format(evt.result.text))
                print(
                    "Translated into '{}': {}".format(
                        to_language, evt.result.translations[to_language]
                    )
                )
                translations.append(evt.result.translations[to_language])
            elif evt.result.reason == speechsdk.ResultReason.NoMatch:
                print(
                    "No speech could be recognized: {}".format(
                        evt.result.no_match_details
                    )
                )
            elif evt.result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = evt.result.cancellation_details
                print(
                    "Speech Recognition canceled: {}".format(
                        cancellation_details.reason
                    )
                )
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print(
                        "Error details: {}".format(cancellation_details.error_details)
                    )
                    print("Did you set the speech resource key and region values?")

        done = False

        def stop_cb(evt):
            """callback that signals to stop continuous recognition upon receiving an event `evt`"""
            print("CLOSING on {}".format(evt))
            nonlocal done
            done = True

        # Connect callbacks to the events fired by the translation recognizer
        translation_recognizer.recognized.connect(recognized_callback)
        translation_recognizer.session_stopped.connect(stop_cb)
        translation_recognizer.canceled.connect(stop_cb)

        try:
            # Start continuous recognition
            translation_recognizer.start_continuous_recognition()

            while not done:
                time.sleep(0.5)

        finally:
            # Ensure recognition stops properly
            translation_recognizer.stop_continuous_recognition()

        # Save translations to a file
        output_file = "/Users/tal/Desktop/Speech_Translation_Azure_AI/test_audio.wav" #change this to the desired output file name and path
        with open(output_file, "w", encoding="utf-8") as f:
            for translation in translations:
                f.write(translation + "\n")

        print(f"Translations saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


recognize_from_long_audio_file()
