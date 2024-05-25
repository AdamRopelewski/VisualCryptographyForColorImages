# Visual Cryptography for Color Images

## Wprowadzenie



## Opis Projektu

Wykorzystana przez nas metoda kryptografii wizualnej polega na podziale obrazka na dwa częściowo losowe, nieczytelne obrazy, które po nałożeniu odpowiednim na siebie, odsłaniają oryginalny obraz. Ta technika, zwykle stosowana do obrazów binarnych (czerń i biel), została tutaj rozszerzona na kolorowe zdjęcia, zwiększając tym samym pulę zdjęć możliwych do zakodowania. Nasz projekt wykorzystuje model kolorów RGB oraz schemat kryptograficzny (2, 2), który wymaga obu części do odszyfrowania obrazu.


## Instalacja


```sh
git clone https://github.com/AdamRopelewski/VisualCryptographyForColorImages.git
cd VisualCryptographyForColorImages
pip install -r requirements.txt
```

## Użycie
Po zainstalowaniu wymaganych modułów uruchom program gui.py przy użyciu pythona.
```python gui.py```


### Szyfrowanie Obrazu

* Zaznacz opcje "Encode" naciśnij przycisk "Start". 
* Następnie wskarz plik wejściowy i zatwierdź. 
* Po zakończeniu wyświeli się komunikat o czasie trwania. 
* Użyj przycisku "Open output folder", aby dostać się do plików wynikowych.


### Deszyfrowanie Obrazu

* Zaznacz opcje "Decode" naciśnij przycisk "Start". 
* Następnie wskarz dwa pliki wejściowowe (te ozyskane w kroku Encode) i zatwierdź. 
* Po zakończeniu wyświeli się komunikat o czasie trwania. 
* Użyj przycisku "Open output folder", aby dostać się do plików wynikowych.




## Przykładowe zdjęcie w kolejnych krokach.

### 1. Plik Wejściowy
<p align="center">
  <img src="./input/ImageToBeCoded0.png" alt="Plik wejściowu" width="650">
</p>

### 2. Plik ze zmniejszoną przestrzenią kolorów (dithering)
<p align="center">
  <img src="./output/1_dithered_image.png" alt="Zaszyfrowany plik cz. 1" width="650">
</p>

### 3. Plik pierwotne piksele otworzone z płytek RGB. Rozdzielczość 9 razy większa
<p align="center">
  <img src="./output/2_x9_res_dithered_made_of_tiles_image.png" alt="Zaszyfrowany plik cz. 1" width="650">
</p>

### 4. Zakodowany plik nr. 1
<p align="center">
  <img src="./output/3_encoded_image_1.png" alt="Zaszyfrowany plik cz. 1" width="650">
</p>

### 5. Zakodowany plik nr. 2
<p align="center">
  <img src="./output/4_encoded_image_2.png" alt="Zaszyfrowany plik cz. 2" width="650">
</p>

### 6. Zdekodowany plik - Błedne kolory
<p align="center">
  <img src="./output/5_decoded_image_xor_and.png" alt="Odszyfrowany przykład z przywróconymi kolorami" width="650">
</p>

### 7. Zdekodowany plik - Poprawione kolory
<p align="center">
  <img src="./output/6_decoded_image_restored_colors.png" alt="Odszyfrowany przykład z przywróconymi kolorami" width="650">
</p>

## Twórcy
* **Adam Ropelewski** 
* **Dawid Maliszewski** 
* **Sebastian Matejak**


