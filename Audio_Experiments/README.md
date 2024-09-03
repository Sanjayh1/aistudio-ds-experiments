![alt](../../images/NLP.png)
# 02. Experiments with Audio

Experiments involving the training and inference of deep learning models with audio-related tasks, such as voice-to-text and text-to-voice conversion. Recommended for showcasing features related to GPU, Monitor Table, NEMO (Nvidia's Experiment Management System), and Nvidia technology. TOffers models for inference via Hugging Face.

---
#### [Audio Translation Sample](Audio%20Translate%20Sample)
In this experiment, we are going to analyze a pipeline consisting of four models from Nemo, provided by NVIDIA. This pipeline performs audio translation, where it first converts audio to text. Subsequently, the text is translated, resulting in the generation of audio in the new language.

| Needed Resources for training     |              |
|--------------|--------------        |
| Recommended workspaces         | NEMO image|
| GPU enabled          | Yes           |
| Minimum GPU memory   | 4GB    |

| Integrations     |
|--------------|
| Published Services        
---

---
#### [Audio Transcription](Audio%20Transcription)
In this pipeline, we utilize a pre-trained small Whisper model to transcribe audio extracted from a YouTube video. This model specializes in accurately converting low-quality audio to text.

| Needed Resources for infering     |              |
|--------------|--------------        |
| Recommended workspaces         | Data Science image|
| GPU enabled          | No           |
| Minimum GPU memory   | 0GB    |

| Integrations     |
|--------------|
|        
---

---
#### [Text To Speech](Text%20to%20speech)
In this pipeline, we utilize the gTTS (Google Text-to-Speech) library to convert text into speech. The provided model, with the specified language (in this case, English), generates audio output corresponding to the input text. Additionally, users have the flexibility to change both the language and the text that will be converted into audio according to their preferences.

| Needed Resources for infering     |              |
|--------------|--------------        |
| Recommended workspaces         | Data Science image|
| GPU enabled          | No           |
| Minimum GPU memory   | 0GB    |

| Integrations     |
|--------------|
|        
---