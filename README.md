# Video-a-texto
Necesitarás instalar las siguientes bibliotecas si aún no lo has hecho:

Copy code
pip install SpeechRecognition
pip install PyAudio
pip install noisereduce
pip install librosa

Este código incluye una función adicional llamada reduce_noise, que utiliza la biblioteca noisereduce para reducir el ruido de fondo del archivo de audio. Después de descargar el audio del video, el código reduce el ruido y luego transcribe el audio a texto utilizando la función transcribe_audio_to_text. Ten en cuenta que la reducción de ruido puede no ser perfecta y puede afectar la calidad del audio. Puedes ajustar los parámetros de la función nr.reduce_noise para obtener mejores resultados según tus necesidades.
