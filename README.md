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
31512/31512 [==============================] - 5s 150us/step - loss: 1.3173

--- DIVERSITY: 0.2 ---

Camastonan
Balnaban
Gargandush
Carslide
Cashteridden
Ballenbridge
Camasdale
Craiggown
Colintran
Dalbree
Ballochae Bride
Kirkton of Maltown
Carse
Camastownan
Craigbank
Kilmalloch
Ballendrean
Craignogr
Camasaig
Ardersie
Ardnamore
Ballenbree
Kilmalarr
Dunban
Stevie
Stracheray
Craigweld
Cardersie
Ballen
Kilmaladock
Strachenbridge
Ballendren
Branaig
Craiggonn
Braeheaden
Craigholl
Ardnans
Kings
Craig of Muthren
Kirkton of Callingall
Craig of Munton
Carnaga
Minnichtown
Bracaridden
Carnal
Braeheadenarry
Bondyle
Colindernoch
Cambusk
Gortondee
Kilmalare
Camase
Mill of Charlet
Sandallan
Carsleichae
Carsessdan
Dalbrenger
Ardness
Carstavallich
Bondalloch
Dalbrain
Craingston
Ardnagort
Strano
Dunish
Braeheadell
Ballinan
Ardraig
Dunbarit
Ballamavun
Dalnagland
Clachan of Glenaseigh
Dunbarn
Clachan of Glenaseig
Ballend
Balnacrbrits
Dalmerite
Torrig
Craston
Ballinsburgh
Barnanan
Carnon
Tarber
Ballanton
Carston
Craigwood Bridge
Dalmall
Cothanan
Gardon
Carnacs
Kildranneth
Ardwood
Dalbride
Cloversde
Bridge of Destown
Moulth
Golansour
Achnabridge
Mill of Chirnacrous
Craigead
--- DISCARDED: 33 real names ( 16.25615763546798 % ); 70 duplicates ( 34.48275862068966 % )

--- DIVERSITY: 0.5 ---

Achmadden
Blachnacrich
Barran
Tilly of Loch
Milton of Gouthorn
Invererridge
Ardnaston
Invere
Pitter Wellacel
Dundean
Capber
Dalbree
Bogton
Caddingnann
Inverindran
Gortinghan
Glenerge
Stebbegg
Brachavouse
Collich
Saltobridger
Ballen
Whitestanish
Cothown
Collie
Camastonan
Bailestone
Gattllston
Rutoan
Newbath
Bellybridge
Moulton
Mortton
Colliessae
Gordenbogse
SteleybridgeDal Trriscuir
Forrig
West Ena
Dalbrain
Bradie
Inveraclaig
Carstast
Chapees
Cadal
Sorts
Kilmighaig
Kinnethmore
Dunaighay
Kilmoran
Carnalish
Halns
dal
Achindalline
Caple Camlunach
Ardingsidg
Skallas
Redhh Rahale
Carletown of Elvar
Carston
Tigh Taringerton
Invererran
Inveread
Camastownan
Edin sten
Glanghall
Crastlether
Balmearn
Galnaga
mair
Dallavenreich
Kirkton of Campsie
Clachary
Halnton
Saint Burn
Port Newwome
Calloch
Farnand
Gargiggon
New Abegfarry
Kirkton of Maig
Kilchetstown
Salinar
Gargick
Kinch
Stelerride
MossCumming
Gattleton
Garvoch
Ardnand
Newh Pilside
Easter Monn
Craig of Munton
Gargutown
Baleacalloch
Baltrawins
Colintray
Laggume
Lochie
Largus Bay
Barnshie
--- DISCARDED: 11 real names ( 9.734513274336283 % ); 2 duplicates ( 1.7699115044247788 % )

--- DIVERSITY: 1.0 ---

Nether Glencaute
Strachtynan
oheill
Shawhceigang
Ashie
Muchnan
mairn
Pollach
Craignood
Tordan
Carmore
Condan
Meinstow
Airdridge
Forringie
Dunbel
Craigallick
Penmar
Glenbead
Welloce
Greenochie
Lochwinnet
Camastownan
Pruskhinne
Inverishait
Saint Daug
Knockester Bain
Kirkton of Montonbrait
Fanhouse
Arnarown
Rhyrick
Wellocf
Gloibur
Bregsick
Tohshel
Obtondick
Fordal
Achnoon
Dunaighay
lash
Libeeton
Carban
Carnston
Dalsety Bair
Birn
Maverich
Brouse
Palco
Dunnoss
Lower dobhyle
Kilmelloch
Hodrburn
Michemston
Craig ayva
Dallus
Garmore
Achneenbie
nisaig
Edra
Gaasdanass
Melloch
Hilessie
Mouldridge
Marrtfoot
Kirkfood
ay
Daugs
Carglack
Kirkton own
Rossick
Burrar
Craich
Rhybernock
Risesdal
Stron
Vullabridge
Invere
Inverisha
Cranferkortie
Hyndocs
Skalloch
Caddings
Granggend
Cloverfieldie
Bridge of Muge
Durna
Monton Spint
Steber
Inveredranne
Sanyill
Braeton Buster
Achinalach
Campsdort
Bowlingend
West
Camcaff
Galleston
Contonwoot
Auchnandhill
Mot Bridge
--- DISCARDED: 5 real names ( 4.761904761904762 % ); 0 duplicates ( 0.0 % )

--- DIVERSITY: 1.2 ---

Portrie
ullage
Culron Esmpack
Kebiss
Dalsetcrymy
Gatabeoch
Tillyfey
Cash
Blackfoon
mair
Netherisden
Eliordal
Dunie
Airdastle
Steat of bork
Fer Inverey
Darlebridge
Hothill
Rate Echill
Creebs
Cardindaln
korra
Culole
Grygary
Amnacred Buguhalroch
Kilmalganabride
Comaster
Kingsbosn
Crasklabla
Clach Uiss
Dulemore
Dalborton
Pound
Cstaminh
Carse
fienarurhay
Slasnaig
Hillth
ulpock
Kirnaston
Skavie
Fairh
gindaig
minda
Lochmannan
Kilmulock
Kibbown
Pitboshock
Stoplebridge
Falestonn
Loga
ykerwood
Kishuelall
Poundome
Summerslan
Kligatthearn
Scyteran Fourd
Wilsooty
Aalbanle
Ash
Stom
Pattemswar
Raul
Aartholl
Liklorry
Boshnmillie
Rothie
Adpin
Sunaie
North ris
Achridenny
Nedblet
Athton
Inverindal Ma
While
Middone Rean
Luntearlos
Grunfoush
 Termore
Bodraig
Westqurgape
Strupae
Masdtoad Fraick
Dungcarny
Bogherarroth
Portmrgan
Braca
Gotonan
Stoney
Glorghaven
eas Gaynyburn
Kirkboon
Sandulds
Wpland
Tyniline
Dunis airt
Duanairsie
Barnansca
Scaltlorven
Storehaven
--- DISCARDED: 6 real names ( 5.660377358490567 % ); 0 duplicates ( 0.0 % )
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
