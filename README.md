# Подгрузка либ:
1. pip3 install google-cloud-speech
2. pip install pyaudio
3. pip install SpeechRecognition
# Работа
Сейчас слушает речь с микрофона, речь должна быть до 10 сек, если речь идет > 10, то все что было 0-10 затирается и слушает снова начиная с 11 сек  
Распознанный текст в переменной `text` (сделать как будет удобно)  
