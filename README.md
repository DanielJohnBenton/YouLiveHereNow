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
63790/63790 [==============================] - 9s 147us/step - loss: 1.6808

--- DIVERSITY: 0.2 ---

DISCARDED: Walton
DISCARDED: Broadwood
DISCARDED: Carrington
DISCARDED: Woodton
DISCARDED: Bradley
DISCARDED: Charleston
DISCARDED: Stowey
DISCARDED: Christon
DISCARDED: Bradley
DISCARDED: Holme
DISCARDED: Bradley
DISCARDED: Bradley
DISCARDED: Stretton
DISCARDED: Stretton
DISCARDED: Chaldon
DISCARDED: Winton
DISCARDED: Broadwell
DISCARDED: Stretton
DISCARDED: Llangan
DISCARDED: Llangan
DISCARDED: Brackley
DISCARDED: Carrington
DISCARDED: Kirkton
DISCARDED: Broughton
DISCARDED: Chesterton
DISCARDED: Charleston
Branton
Brennie
Chalmer
Brookmall
West Bridge
Bridgerton
Stoney
Cranton
West Warth
Crosel
Chalkston
Little Ard
Brookston
Barragh
Chillerton
Little Branton
Bridgenden
Cross Bridge
Crossfield
Brookmille
Colden
Stoney
Crade
Cheston
Stoney
Cold Clift
West Warth
Bellston
Stoney Street
Cross Warton
Stonington
Bratherton
Stoney
Stoke Bridge
West Warton
Croseldon
Brooks Wood
Stoneston
Chilley
Coldaress
Brookston
Connand
Stoke Barne
Market Botterton
West Bridge
West Barton
Llangananan
Carnard
Stoney
Stoney
Branton
Charle Carnton
Brookmall
Chalmer Cross
Cornard
West Barden
Crossfield
Brooks
Crossforth
Brookston
Brooks Marston
Brooks Hill
Cornan
West Bramle
Brennie
Brooks Hill
West Harrishall
Cross Corner
Stoney Hill
Stonesham
Cornard
Branton
Stoney
Stoney
Stoke St Mary
Cranton
Stretten
Branton
Brenington
Stoney Mont
West Harster
Stoney
Cranton
West Carnage
West Barton
Charle
Carnall
West Harrishall
Stoney
Stoney
Brooks Corne
Cross Helle
Cranton
Challey
Llangol
Cheston
Stoney Marsh
Bramleston
Brooks Colmington
West Barden

--- DIVERSITY: 0.5 ---

DISCARDED: West Burton
DISCARDED: Harley
DISCARDED: Blackley
DISCARDED: Bradley
DISCARDED: Rock
DISCARDED: Stanford
DISCARDED: Holme
DISCARDED: Burley
DISCARDED: Harley
DISCARDED: Carrington
DISCARDED: Stainton
DISCARDED: Garton
DISCARDED: Bradley
DISCARDED: Stretton
DISCARDED: Stretton
DISCARDED: Harrington
DISCARDED: Burton
DISCARDED: Woodton
DISCARDED: Woodford
Stoke Marster
Carlington
Stont Marston
Mellonston
Brockfield
Little Lower Poet Hille
Branton
Fornham
Bretford
Monkstee
West Breston
Accote
Widills
Harlecragh
Penry
Bell
Carlington
Clarsend
Crossaburn
Croske
Shirdon
Stonarersh
Meaton
Coleston
Bridge of Rodnall
Little Leathwalt
Aberthagan
Thorperen
Stoney Baston
Holwinge
Cheston
Brackington
Blainston
West Ulwick
Stonnards
Great Cawill
Llangbedrry
Markick
Chader Hatheror
Pelston
Cornage
West Clisfield
Little Stonnath
Finder
Foreston
Brockerton
Shepport
Chilley
Llanolenfint
Lapham
Cordington
Brooks House
Lough Head
Martlesingham
Charlley
Charle
Hansley
New Gate
Long Willie
Stanling
Starhampton
Stoney
Porth Bredging
Derph
Perron
West Marst
Cradham
West Bardington
Coningxcote
Monnhys
Waterbourne
East Bally
Closston
Blainton
Brooks Bradley
Ablesham
Laddington
Great Bent
Aber-
Blynby
West Corne
Aberdrerna
Croslaham
Willow
Crayton
Woodforth
Stretten
Warwell
Carnand
Mounterton
Canton
Brooks
Little Handow
Great Cholle
West Hathery
New Halling
South Talliston
Charlesham
Colden
Wallerton

--- DIVERSITY: 1.0 ---

DISCARDED: Melbourne
DISCARDED: Worton
DISCARDED: Duddington
DISCARDED: Burgh
DISCARDED: Muston
DISCARDED: Wetton
DISCARDED: Littleborough
DISCARDED: Newton
DISCARDED: Swindon
DISCARDED: Kenwick
DISCARDED: Harrington
DISCARDED: Whitfield
DISCARDED: Benton
DISCARDED: Warley
DISCARDED: Cayton
DISCARDED: Denham
DISCARDED: Wetton
Llanlagh
Edick
Hernure
Hookstow
North Saret
Marford
Madsingtanfee
Great bleygunda
Beckingdon Clwyn
Eardsker
Penmley
Stordmore
Chilop Hill
Hawlinds Common
Sraundidwast
Stelberlas
Moor
Mustel-on-fyig
vinx Brooks
Harleton xworth
Monkin
Riseste Mock
NewSapow
Beynaby
Cimputon undgerest
Beath
Newonspell
Fristhe Catin
isherpe
Landunds
Saint Manan
Lokeley
Elinsington
forle
West Llankish
Cairrinnan
Biaghen
Dristelloe
Linabelgh
ghocir
Rourk
Marsteddin
Llanalwall
Bermonf
Shindingbede
Wivethead
Martlee
Grilterner
Gampen Cross
Portby
Nainton
Alnington
Littlel
Hippenbirk
Stockby
Crace
Aibberton
Heakeness
Houstoe
Earide
Enby
Portchise
Lyndie
Tkeheety
Woodworthn
Aursham
Haufton
Llandesidbenton
Pretyveley
Miltreety
Great Wooduld
Mhunnybeg
Saint Warth Magbstley
Tolmurs Wood in the Magna
Toddlegalton
Ponton
Budmannard
Michelynana Bad
Springton
Lower Coulton
Heodcott
Wiseaton
Shelalls
Bardartail
Rower
Edsall
Beedstod
Gridcrows
Pelbersdinhamphorthn
Brett
Great Degby
Ikellaws
St Kefield
Ellockdenham
Crane
Raddrafnnes
Hommshall
Cockles
Saint Burton
Malberlis

--- DIVERSITY: 1.2 ---

DISCARDED: Upton
DISCARDED: Petton
DISCARDED: Deal
DISCARDED: Swine
Opderley
Steveninghills
East Wattes
Weoburash
Bedline
Milsey
Tusham on swne
Newtatton Sbe
Pont iucheicu
Dolwedas
Portony
Pston Chollawour
Oldgedre
Ty Rowers
Whihill Cegrbado
Wintingvehpalls undingle
Langnafold
Sterlasht
Applihay
Copthtrwich
Scomphoe
Staelaketon
Llangebeden
Streston
Welmirkmorth
Lisesiansty
uxverine
Huntoor
Kirkcodilloch
Rosel Norths
Walternardaloch
Bnynloa
Rhydowke
Cwmnare
Swinland
Assyn
Eagaborghdside
Ponmnifield
Porllas
Bladwest
Want Sconast
Hillney
Somledgington
Newbourrerton
Wiokcombe
Whisatry
Port
Rhydargh
Mutlele
Blydowin
Fary
Llandaeknwy
holdsley
Llanderfangen
ghyru
Grittoffford
Faakfort
Westwer
Totfield
ilcly-fis
Llugpon
Ashawor Kick
Lidmue
Hanthyvono
Sedatnews
Croys
ble
isshaken
Ruy Cross
Pont Street
ileton Green
Pauntfmelmint
Ellinch
Chenckmayn
Llana
Chileassdon
Twyt Ovunly
Blaf
Greeton
nogwood
Pisby
onh
Chespenwy Nwe
Isleton
Spitfield
Macwingpone
Drymast
Coltyke
Wintan
St wad
o
Rydetunt Cross
Stunhampton
Lower Eaton
Midtlebigh
Rawtrnoke
Woldhopeluugswell
Ridfield
Cronguaau
Haswleldon
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

## Acknowledgements

The code is based very closely on [this Keras example](https://github.com/fchollet/keras/blob/fd3ac2a93ea2584d0679e27a10ebeff0508d7a37/examples/lstm_text_generation.py).

Thanks to [GeoNames](http://www.geonames.org/) for the place names.
