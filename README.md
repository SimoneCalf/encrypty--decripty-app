# Inleiding
Met behulp van deze applicatie kan tekst versleuteld en ontsleuteld worden.
Dit gebeurt door middel van symetrische encryptie.

# Gebruik
Typ in de terminal `python main.py`.
Voer een woord in om te versleutelen.
Voer het verleutelde woord in.

# Werking

## key
Hiervoor is een key nodig.
De variabel `key` bestaat uit een lijst met door elkaar gehusselde:
- spaties, 
- leestkens (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
- getallen (0 tot en met 9) en 
- letters (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
Iedere keer als de applicatie opnieuw wordt opgestart, wordt de lijst die is opgeslagen in de variabel `key` opnieuw gegenereerd. 

## Encryptyproces (versleutelen)
1. De lijst met karakters die versleuteld kunnen worden is opgeslagen in de variabele characters. Deze lijst bevat dezelfde karakters als de key, maar dan in een vaste volgorde.
2. Voor elke letter in het te versleutelen bericht wordt de index van die letter in characters opgezocht.
3. Vervolgens wordt het karakter dat op diezelfde index in de key staat, toegevoegd aan het versleutelde bericht (encrypted_message).
4. Dit proces wordt herhaald voor alle karakters van het bericht totdat het hele bericht is versleuteld.


## Decryptieproces (ontsleutelen)
1. Het versleutelde bericht is opgeslagen in de variabele encrypted_message.
2. Voor elk karakter in het versleutelde bericht wordt de index van dat karakter in de key opgezocht.
3. Vervolgens wordt het karakter op diezelfde index in de lijst characters opgezocht, en dat wordt toegevoegd aan het ontsleutelde bericht (decrypted_message).
4. Dit proces wordt herhaald voor alle karakters totdat het originele bericht is hersteld.


## versimpeld voorbeeld
In dit voorbeeld worden de letters van het woord "hond" versleuteld naar "cfbi" met behulp van de key:
- karakters: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
- key      : ['g', 't', 'u', 'i', 'r', 'm', 'v', 'c', 'y', 'j', 'x', 'o', 'p', 'b', 'f', 'l', 'a', 'h', 'q', 'z', 'n', 'k', 's', 'd', 'e', 'w']


### versleutelen
- De index van "h" in characters is 7.
- Op index 7 in de key staat "c", dus "h" wordt versleuteld naar "c".
- Dit proces wordt herhaald voor de andere letters in het bericht, wat leidt tot het versleutelde bericht "cfbi".

### ontsleutelen
- De index van "c" in de key is 7.
- Op index 7 in de characters staat "h", dus "c" wordt ontsleuteld naar "h".
- Dit proces wordt herhaald om het originele bericht "hond" te herstellen.



