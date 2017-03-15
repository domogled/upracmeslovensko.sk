# Tuto su zdrojove súbory pre web upracmeslovensko.sk

Stránky su založené na projekte bratrského webu uklidmecesko.cz

# pre dobrovoľníkov

Hľadáme dobrovolníkov na:

- preklad textov z češtiny do slovenčiny
- tvorbu vlastného obsahu a funkcionality stránok


# pre prekladateľov

Je treba preložiť texty:
- z webu [uklidmecesko.cz](http://www.uklidmecesko.cz) - všetko čo je použitelne aj na slovensku, najme FAQ, navody ako organizovať atd.
- niektore dalšie texty (najme tie čo su v zdrojákoch a na webe ich priamo nevidno) su v adresári *src/texty na preklad*
- v adresári *src/obrazky na preklad* su texty v obrazkoch. |Bohužial v svg nie je text ako text, čiže s tím bude viac roboty - asi napisat vlastný text to je hned.

# pre vývojárov

## livereload
TODO: doplnit až bude index.html / index.php 

## vývojový server

Aký vývojárský server používaš je tebe. Tu je jedno z možných riešení, keď sa ti nepáčí, možeš pridať svoje. 

## pomocou python3 -m http.server

Ak máš na počítači Python, choď do adresára webu a spusť
```sh
cd src/html
python3 -m http.server
```

> No, lenže web používá PHP a takto spustený http server PHP nepodporuje. Abysme si rozumeli, nepoužívám PHP na backende, ale na vývoji. PHP je šablonovací jazyk, a to veľmi dobrý šablonovací jazyk. Len kvoli bezpečnosti a dogmatismu ohladne objektoveho programovanie z neho ľudia urobili niečo celkom ine.

No, su dve možnosti. V konzoli spúšťat príkaz:
```sh
php src/index.php > src/index.html
```
a pre opakované potreby si jeho spuštanie automatizovat.

Alebo si vyvojový web spustit pod webovým serverom s podporou PHP. Len pametaj, že **PHP súbory v adresári src nie su určené na spustanie na serveru !!!**.

## pre nginx


Toto je moje nastavenie nginx servera, ktoré si možeš upraviť. Dávám ho k dispozícii, skor pre inšpiráciu.

V priečniku server nájdeš konfiguráciu pre nastavenie webového servera. 

> Pozor, toto riešenie funguje len na Linuxe, na inom systéme som nezkúšal. Ak chceš, pridaj svoje riešenie na inom operačnom systéme, ale postavené na iných webových serveroch a jazykoch, nech sa páčí.

Inštalačný skript vyžaduje python 3.6 alebo vyšší. Ak nemate a nechcete mať nainštalovaný Python, nevadi, server nastavíte aj bez neho. Já Python ľúbim, takže všetko čo sa dá robím v nem. Okrem webového backendu, paradoxne. :-)

Najprv tedy pre tých, ktorý majú na svojom počítači Python. Skript spustíme veľmi jednoducho:

```sh
./server/install_nginx_server.py
```

> Pozor, pre konfiguraciu je použite PHP ako šablonovací jazyk, lebo PHP je v skutočnosti šablonovací jazyk s celkom univerzálným použitím. Len ľudia z neho urobili niečo celkom iné. Treba mať nainštalované PHP tak, aby sa dalo spúšťat z konsole.

Ak nemáš Python, namiesto inštalačného skriptu možeš spustit postupne tieto príkazy:

```sh
cd server/nginx
php ./hosts.php > ./hosts
meld ./hosts /etc/hosts
php ./nginx_site_php > /etc/nginx/sites-available/upracmeslovensko
ln -s /etc/nginx/sites-available/upracmeslovensko /etc/nginx/sites-enabled/upracmeslovensko
service nginx restart
```

Postup sa može na vašom počítači mierne lišit. Zrejme bude treba spúšťat niektoré z týchto príkazov s oprávnením roota.

V príklade je použitý program *meld* na porovnanie a ručne spájanie rozných verzii súborov. Ak nemáte nainštalovaný *meld*, použite iný program, alebo do súboru `/etc/hosts` pridajte ručne to, čo vrátí skript `php ./hosts.php`. Automatizovať porovnavanie obsahu súboru `/etc/hosts` sa mi nechcelo, možno nekedy nabudúce.

>Viem, že existuje veľa iných riešení, založených na nodejs, alebo ja v Pythonu

