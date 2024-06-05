# Visual Cryptography for Color Images

## Wprowadzenie
Kryptografia wizualna jest  obszarem kryptografii, który koncentruje się na kodowaniu i dekodowaniu informacji wizualnej. W przeciwieństwie do tradycyjnych metod kryptografii, które opierają się na przekształceniach matematycznych, kryptografia wizualna wykorzystuje obrazy, aby ukryć i przekazać tajne informacje. Technika ta pozwala na podzielenie obrazu na kilka warstw (tzw. udziałów), które indywidualnie nie ujawniają żadnych informacji, ale po ich odpowiednim połączeniu odtwarzają oryginalny obraz.
Jednym z najprostszych przykładów kryptografii wizualnej jest schemat 2-out-of-2. Oryginalny obraz jest podzielony na dwa udziały. Oba udziały wyglądają jak losowe szumy, ale nałożone na siebie tworzą czytelny obraz. Dzięki temu, nawet jeśli jeden udział zostanie przechwycony, bez drugiego nie można odtworzyć oryginalnej informacji.

## Opis Projektu

Wykorzystana przez nas metoda kryptografii wizualnej polega na podziale obrazka na dwa, częściowo losowe, nieczytelne obrazy, które po odpowiednim nałożeniu na siebie, odtwarzają oryginalny obraz. Ta technika, zwykle stosowana do obrazów binarnych (czerń i biel), została tutaj rozszerzona na kolorowe zdjęcia, zwiększając tym samym pulę obrazów możliwych do zakodowania. Nasz projekt wykorzystuje paletę kolorów RGB oraz schemat kryptograficzny (2, 2), który wymaga obu części do odszyfrowania obrazu.

### Wykorzystana metoda 
Wykorzystana przez nas metoda bazuje na tej opisanej w

> Color Visual Cryptography with Completely Randomly Coded Colors, Arkadiusz Orłowski & Leszek J. Chmielewski[**<sup>[1]</sup>**](#source1)


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
  <img src="./input/ImageToBeCoded.png" alt="Plik wejściowy" width="650">
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

## Podział pracy
- Sebastian Matejak:
  - Pierwsza metoda oparta na szyfrowaniu przy użyciu logicznego AND i deszyfrowaniu przy uzyciu OR. (folder obsolete).
  - Research.
  - Odtworzenie metody dla szyfrowania obrazów binarnych będącem punktem startowym.
- Adam Ropelewski:
  - Interfejs graficzny użytkownika
  - Nie wykorzystana metoda z użyciem HSV zamiast RGB.
  - Krok nr. 6 poprawiający kolory obrazka. Przywraca on orginalną rozdzielczość.
  - Refaktoryzacja kodu main.py na potrzeby GUI.
  - Instrukcja obsługi. Plik readme.
- Dawid Maliszewski:
  - Ostatecznie użyty algorytm wykorzysujący XOR do szyfrowania oraz AND do deszyfracji.
  - Przystosowanie GUI do systemów Macintosh.
  - Krok nr. 2 - Dithering obrazka do przestrzenin 10 kolorów.
  - Krok nr. 3 - zapisanie każdego z 10 kolorów za pomocą 9 pikseli składających się z RGB.
## Bibliografia
1. <a name="source1">[Orłowski, A., Chmielewski, L.J. (2019). Color Visual Cryptography with Completely Randomly Coded Colors. In: Vento, M., Percannella, G. (eds) Computer Analysis of Images and Patterns. CAIP 2019. Lecture Notes in Computer Science(), vol 11678. Springer, Cham.](https://doi.org/10.1007/978-3-030-29888-3_48)</a>
