# You Live Here Now
## A place name generator

## Some favourites so far
- Sowton Porkham
- Diphead
- Ancestor
- Little Worth
- Long Mill on the Hill
- Shirtie Hacktown
- Bridge of Little Stratch Hill
- Old Belchown of Glemmuirthonton
- Little Lower Poet Hille
- Clatterbridge
- Arch on Samnickton of Tin Isle Beirton

Yes...
It actually came out with Sowton Porkham.

## Technologies used
- Architecture: [Long Short-Term Memory (LSTM)](https://en.wikipedia.org/wiki/Long_short-term_memory) neural network
- Language: Python
- 3rd-party libraries: [Keras](https://keras.io/), [Tensorflow](https://www.tensorflow.org/), [NumPy](http://www.numpy.org/)

## Results example
After each training run, the network generates 100 place names for each of several different "diversity" settings. This setting determines how "wacky" the place names can get based on the predicted probabilities from the network's output. The lower diversity settings give place names that look extremely realistic but are rather boring, whereas many of my favourites come from the more wacky settings, which come out with more creative stuff, but also generate nonsense that wouldn't pass as a place name.

While generating these responses, it discards names generated that already existed in the training set (i.e. the network has generated a place name that really exists).

After training 59 times, here are some example outputs at various diversity settings:

```
Iteration: 59
Epoch 1/1
63771/63771 [==============================] - 9s 147us/step - loss: 1.6989

--- DIVERSITY: 0.2 ---

Colston
Llangaddd
Carnington
Carton
Carle
Carleston
Charle
Harthorpe
Llangard
Saint Mary
Browen
Corrow
Carles
Chilley
Collisham
Ballyne
Martherby
Llangande
Sandbury
High Cherby
Llangandon
Briggton
Carran
Brower
Carrow
Carral
Compton Heath
West Charle
Lower Carrin
East Cross
West Howerton
Carlestone
Colling
West Penn
Charley
South Carrington
Sandborough
West Chambley
Corthorpe
West Wood
Cortherby
Little Wynton
Corrington
Carney
Wingley
Cainthorpe
South Carle
West Hinton
Hartherby
Little Carrington
West Hanton
West Halley
Aldside
Crosston
Llangathinges
West Harley
Corth Carrington
West Cross
Carley
Alley
Lower Carrendon
Sheaton
Long Bridge
West Langton
West Home
Whitenham
Barreston
Brockham
Compton Stoke
Burton Heat
West Charlton
Carrestone
Compton Saint Mary
Cold Hill
Harthorn
Browes
West Collen
Saint Marton
Correston
Stoke Hill
Witton Saint Mary
Hartham
West Wynton
Charrington
Statton
Compton of Stone Hill
Witton Hill
Scarestone
Stoke Cross
Little Cander
Stowen
Sand Cambley
Crossington
Chilly
Little Cross
West Howery
West Long
Sanderstone
Fowston
Compton Hill
--- DISCARDED: 202 real names ( 39.29961089494164 % ); 212 duplicates ( 41.245136186770424 % )

--- DIVERSITY: 0.5 ---

West Alderted
Lower West
Llangrift
Beddenhurst
Chilley Saint Mary
Worthbourne
East Chadley
Saint Mary
Holden
Pentriel
Walley
Denrington
Sheaton
Church Wood
Costham
Aldbridge
Chilley
Glasston
Clatham
Wingston
Chitton Willers
West Crook
Statton
Carlemort
Watersh
West Winchley
Bodich
Doyne
High Bishop
Llangathar
Carle
Stoke Church-M-theech
Charle
West Mone
Harthorn
Great Marlin
Harstead
Catterborough
Saint  bydulch
Fanfield
Colderley
Ardin
Kings Heaton
LlanstBriet
Carton
South Carle
Burney
Hompton
Colley
Saint Peter
East Chaddington
Cheir
South South
West Heyton
West Share
West Loog
Callgross
Cotton Green
Alberrogham
Holling
Thorn Downstone
South Shipston
Carley
Gardington
Charlestone
Great Bridge
West Cross
Colcester
Charleton
Cartebour
High Halsford
West Hantley
South Charrington
Chelling
East Weighton
Ballyny
Fowston
Hendington
Auchton
Tretton
Cromstead
Calgatton
Marington
Llanande
Criasterham
Port
Crove
Barrenton
Pennyd
Great Swinton
Compstone
Winching
West Wynton
Great Wisherse
Saint rMers
Carrowalton
Dunside
Carren
Hollow
Charleigh
--- DISCARDED: 34 real names ( 24.817518248175183 % ); 3 duplicates ( 2.18978102189781 % )

--- DIVERSITY: 1.0 ---

K drynt
Winnford
Clorrinakley
Plman
Doagh Saint whan
West Walkonnourt
Scatlant
mangisby
Calkirks
Mintochgin
Tsfreton of Sterrode
Derrington Woodring
Llandydd
Llandrivais
Wingbearce
Tardrom
Crosss
Ley House
Pittrowbrey
Whutterbohenpe
Birdford
Betcatff
Kirks Keans
Drettlewood
Carrenford
South Panwick
Saint ONToS Greeli
Halmston
Huston
Southreat
Lapon
Stalston
Sysridge Crorse
adudrodge
Stexlater
Flaurdence
Spicklebury
Bolventon
Hhingham
Curestone
Kirkohorh
Hobbey
HemooBaWerford
East Pamwell
Ocklands
Cornfield High
Bungay Wastreith
High Ceston
Cesterwmttone
Holdingborough
Winnforth
Woohtow Heath
Shillan
Cran
Eortham
Whead
Carrichau
West Hewkwortgste
Newthenton
iDoLfMelld
Alcham
Lowutusk
Freckns
Puddley
wMccur
Sispad
Barncabe
Halgatefor
New Chainsham
Hayt
ingtol
Reavensley
Atton
Anstreth
Pomsh
Llanganan
houst Wriston
Boint Keas
Garsalt
Rhockn
Appley
MarRidghton
Llanodxu
Buckborough
Madwood
Frebden
Chippleford
Asterwick
Dridegton
Cuestfield
Stockfield
Beun
Duntnir
licastor
Welta-figll
Haod
Nanbury
Tewtlebigiog
Newton Estate
Newton the Wildom
--- DISCARDED: 14 real names ( 12.280701754385964 % ); 0 duplicates ( 0.0 % )

--- DIVERSITY: 1.2 ---

North Bunces
Port Hyderton
Mosteat
North Boasal Will
bffa
Fowsbruceba
Breckfield
millawensey
Cleighily um Dsbrick
thuntref
Ambaar
Woodoch
Hourhillickm Marrisaru
Corcpwrol
Mhee
wWncum Champton waldele
Hayt Carmaretry
Barphillucum
Maockack
Carrtocum
Hardwood
Bompton Stoke
risgort
Nempston
Sighill
Dackepllan
Abercharniun Ferrckes che ey
ewitneyy
Bahulmheads
Praston
Weston Moor
avont
Meffry
Arock
New Wyford
aHyamnton
Bradwick
Sailt Rignage

Lowinols Prisgum
Fore
Puddy
Brefeland
Anshand
Saint Fethownney
Pet-Tmarasham
Wickolmore
thelmiston
Sutterbury
Padford
Crissde
Woylsalla
hestoun
Adrhinad
ls steet
Hithlmassey
Cratatter Bail
Penattnes
goLyhede
Norghtrind
Basbury
nNairogan
Sidestertown
Kirkichgiatt
Sypth
Farrton
Mil Haysry
Newtown Woodre
Tor Oxd
Almsden
Briustrioughtone
Cadgateslett
Modsford Basloftoning
Thorboel
SnaesMby
Ec
Stovhillen
Grauddleswny
Whalsich
Knwborug
Clam
Shw
Pombervile
Hampstown
Sherning
Wutterbell
Cedanvin
Podworth
sCark
Tasntherys
Crosstaf
Kisken
Hebishors
File
Hilley
Wathing
codacombes
Aemey Boykred
Worhaw
Nelkwick
--- DISCARDED: 4 real names ( 3.8461538461538463 % ); 0 duplicates ( 0.0 % )
```

## Example using only Scottish placenames

```
Iteration: 59
Epoch 1/1
10504/10504 [==============================] - 2s 149us/step - loss: 0.6920

--- DIVERSITY: 0.2 ---

DISCARDED: Castleton
DISCARDED: Blackford
Caldsty
Badilachu
Dullisston
Lonerd
Baldenstole
Middel
Dangry
Inchremston
Altlank
Wilt Gramn
Archol
Kircercorn
Polterre
Kilulaing
Kirkcoly
Barkloch
Baldern
Abery
Bridgear
Tallaness
Ayleberry
Saff Goovern
Stratheld
Brighou
Dunbriees
Saint Miwnarton
Kirkford
Inverkien
Duncraigh
Denbirt
Criegsheydls
Stothnass
Luchincroy
Blllochie
Midoll
Barblynd
Maintordhie
Midol
Dunbry
Inchragburn
Coalie
Saiev
Hownathridge
Lonbridge
Cournn
Corrandre
Shille
Coruld
Ferry
Bricksind etd
Badercote
Briecorn
Boullie
Kinkwncrud
Salenah
Polwlybenss
PolMtow Ger
Arnander
Ardderale
Carnich
Derry
Barglod
Dumers
Duneldert
Dannneed
Cardliston
AchlisareShee
Avingriee
Duchenaick
Ganart Saick
Dungried
Kingcalr
Logher Morn
Galesargie
Raigin
Bosle Blagk
AuchinPiet
Glenhrossain
Dalrendale
Ston
Morth Low
CrHfgam
Cassald
Spirt
Miltale
Bailos Flechie
Kirkton of Achle
Bellyskerry
Stenkort
Arnidale
Saitthin
Midolliig
Kinceraick
Salebern
Cowncretisk
Denblusie
CaHllafie
Ardhenal
Gorinevick
Stoney

--- DIVERSITY: 0.5 ---

DISCARDED: Barry
DISCARDED: Auch
Carglem
Chasty
BalloGron
Kilccofnick
Poltocl
Aidmole
Stienane
Cardold
Barnan
Cullogidgrowe
Kingehrithe
Invercilva
Tond Bay
lenston
Brilckien
Sauch nakrn
Scarry
Blaighord
DurcrSumach
Dorvinn
Logher of Gorey
Haldsain Meanton
Urdhie
Bald n ckw
Akfon
Ardford
MotfinbriNistop
Ale
Kington
Darchneen
Bruglowach
Lowanmole
Stolvuie
Midell
Charnow
Auden
Buhnniecharn
Cornychill
Lowerrie
Canslysken
Arnie
rige Comalie
Sallinathilcort
Mooser
Corrndon
Ardtluchan
Kinglochton
Gransten
Dallendert
Glencorry
Klenston
Kingwerthie
Ardsterton
Craggn
Mhockhinn
Morskart
Lochwood Forth otl
Pitleberds
Canton
Fean of Firtrie
Croie
Lower Ber
Farrisga

Carvangant
Mirchston
Fossington
Craigg
Ball
Arnbriggs
Canbrifies
Saint Miwnord
Drumank
utha
Kilmora
Hideldsher
Arddbullie
Cass
Drumsidgot

DonSknk
Stown
Ballyshy
len
Auctonbriagh
Coallie
Kirkckinna
Druminar
Crosbridge
Casslie
CanniComer
Clochneblan
Croseh Olde hendart
Granrouss Benchry
Forrossill
Keiltom
Eist die
oomale Saint Gailusse
Isl
Doukle

--- DIVERSITY: 1.0 ---

DISCARDED: Kilmore
Ballochaie
shed
CaCUtron
Nochwene
aighole
Bllachmick
Fairy
Carnan Mrick
Auclington
Kilcforthie
Loweshen
Ardforidge
Donala
Kenter Griege Ferins
Auchergerw
CrSaghores
Pollherin
duirletlon
Starr
hiterard Dee nas Glassken
Aldbreen
Rochaina
Clowfie
Isle Grean
Abriston
Molair
of Glas
Bamnochte
KirkluGle
Whill Ben Bandawlee
Ardloystoles
Ardea
AvullIumin
Ridckalbriagh
Caird Davin
Ballochry
Invenkte
Inchillick
Sanmwinn
Saunnahern
Borgholdchach
Craigt
Glencrgick
AuchinCrey
Sooth Mainceraheld
Balenburn
Royth
ooshie
Easter Bridge
Gearventons ofle
shig
Tihen
Dunlock
glacon Ales
Durkannich
Westens
fie
Kirckreeld
SInesstown
Golmachun Glany
cortysiee
Stoth
Losfurn
Fonmilleaco
Weathrood
CrHggs Knvenk
Thacklicr
Inverbrigg
Lowerishels
Strather
Proskigk
Cemmsside
towny Beldie
Kinckhoot
Lonlfererishe
trochar
Crossiisktorn
Carnsd la O
Ayle knisse
Eartossill
Kingtruse
Rogin
Ballickhinn
Strothhall
mirgston Fornes
Oldsig
Ridton All
Remick
Kilchoon
Forlinar
hiaddaig
Tibriston
Achtors
Um
Stolvuie
Arvalmichine
Portnemroe
khirroot
Morliem
GlacroGras

--- DIVERSITY: 1.2 ---

Lheytertherr
plintyness Banrossater
Leerilandald
Twentole
Klockfoon
Rorlitonn Sairl
PoretenCre
Cardshale
Legneffouchie
Kingter
Garvie
gorridcore
Westherr
Germacater
East Skuln Forvuich
kergisse
Strathill
Hairtmit
Howny
Ardslay
Erstan
Hamole
Mill
Clltoberr
Reygle
towner
Rog
Lorcharie
Finbidge
Derichne
Ard lem
KilkinBord
Gouliston
Durluch
gattin
Banrancore
Fonarin
Borchwick
Kirtonnochn
DunHupry
Rishton
Ardhocad
Rachachie
mirth Blagoo
Foverisk
Foxross Shield
Carona
Salentoce
GrenGremes
Lichon
Berilcsy
Invermoran of endia
Midoburghiig Cavill
Corrern
BirKell
A'hnaighort
Goucmin
Kington
Alllan
Culryilt
Lunghoodchie
Kirkfick
Bundall
Fennakill
Gouloras
Clanomriem
Goungigs
Casraichar
Drumall Emven
Porphinrtun
Kington
Forrosfid
conmelly
Hanten
Bully
Kirkword New
Ardfort
Eccorrosston
Brdochbrnd
Enpirt
wirkol
yre
Isle
Archremos
Corlin
Black
readie
Maxdll
Maitthiel
Lossay
Kirkton of Sletton
Craggiston
Grestancr
Gruignan
Kirkburn
Kilnaray
East Bacny
Auchssie
LeOnton
Timmon
```

## Original idea?
No. It's been done before.
- [AI is traned to generate incredibly British place names](http://www.telegraph.co.uk/technology/2017/07/20/ai-trained-generate-incredibly-british-place-names/) - Telegraph

The code is based very closely on [this Keras example](https://github.com/fchollet/keras/blob/fd3ac2a93ea2584d0679e27a10ebeff0508d7a37/examples/lstm_text_generation.py).

The main changes are to train from newline-separated lists to generate small pieces of text, and tweaking various parameters and behaviour to work better for generating place names instead of just general blobs of text.

It also works well for generating other similar lists, such as animal names.

## More fun/cool names - honourable mentions:
- Eddwaldbury
- Longltol Norton on The Mork
- Arfouclixhaven
- Curningwood Cryabyes
- Tunky Linke
- Scaldinghamme
- Fish Ash Holthorpe
- Bellybourne
- Ballybrook
- West Easton
- Hollie Heath
- Sherton on the Wallow
- Egling le Hacker
- Crosskingtoll

## Acknowledgements

The code is based very closely on [this Keras example](https://github.com/fchollet/keras/blob/fd3ac2a93ea2584d0679e27a10ebeff0508d7a37/examples/lstm_text_generation.py).

Thanks to [GeoNames](http://www.geonames.org/) for the place names.
