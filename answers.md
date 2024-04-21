# Detector de spam

## 1. ¿Cuáles son las 10 palabras más encontradas en correos con SPAM y en correos No SPAM? ¿Hay palabras en común? ¿Algunas llaman la atención?

### SPAM

Las 10 palabras más encontradas en correos con SPAM son:

| Orden | Palabra  | Frecuencia |
| ----- | -------- | ---------- |
| 1     | you      | 4105599    |
| 2     | your     | 2502597    |
| 3     | will     | 997100     |
| 4     | free     | 939790     |
| 5     | our      | 931799     |
| 6     | all      | 732080     |
| 7     | mail     | 635470     |
| 8     | email    | 578759     |
| 9     | business | 521250     |
| 10    | remove   | 499309     |

### No SPAM

Las 10 palabras más encontradas en correos No SPAM son:

| Orden | Palabra | Frecuencia |
| ----- | ------- | ---------- |
| 1     | you     | 3541702    |
| 2     | george  | 3527559    |
| 3     | hp      | 2496576    |
| 4     | will    | 1495268    |
| 5     | your    | 1223098    |
| 6     | hpl     | 1204398    |
| 7     | re      | 1159138    |
| 8     | edu     | 800669     |
| 9     | address | 681569     |
| 10    | meeting | 604460     |

### Palabras en común y llamativas
Las palabras comunes entre los correos con SPAM y los correos No SPAM son: `you`, 'your', 'will', nótese que estas palabras que podrían ser comunes en cualquier tipo de texto, dado que son pronombres y verbos comunes en inglés. 

En cuanto a palabras llamativas, destacan palabras como 'free', 'business' y 'remove' en los correos con SPAM, dado que son palabras que podrían asociarse a ofertas, publicidad, estafas, etc. También resulta interesante ver un nombre propio como 'george' en los correos No SPAM, lo cual podría deberse a que es un nombre común en la base de datos de correos No SPAM, por otro lado, 'edu', 'address', 'meeting' podrían ser palabras comunes en correos institucionales o de trabajo.

## 2. Separe el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba (70% y 30% respectivamente).
El desarrollo de esta pregunta se encuentra en el notebook [spam_detector_notebook.ipynb](spam_detector_notebook.ipynb). Realizando la separación de los datos en un conjunto de entrenamiento y un conjunto de prueba, se obtuvo que el conjunto de entrenamiento tiene 3220 muestras y el conjunto de prueba tiene 1381 muestras.