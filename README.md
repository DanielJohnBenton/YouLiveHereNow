# You Live Here Now
## A place name generator
Based pretty closely on [this Keras example](https://github.com/fchollet/keras/blob/fd3ac2a93ea2584d0679e27a10ebeff0508d7a37/examples/lstm_text_generation.py).

The main changes are to train from newline-separated lists to generate small pieces of text, and tweaking various parameters and behaviour to work better for generating place names instead of just general blobs of text.

It also works well for generating other similar lists, such as animal names.

## Some favourites so far
- Sowton Porkham
- Diphead
- Ancestor
- Little Worth
- Long Mill on the Hill
- Shirtie Hacktown
- Bridge of Little Stratch Hill

Yes...
It actually came out with Sowton Porkham.

## Technologies used
- Architecture: LSTM
- 3rd-party libraries: Keras, Tensorflow, NumPy

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

## Original idea?
No. It's been done before.
- [AI is traned to generate incredibly British place names](http://www.telegraph.co.uk/technology/2017/07/20/ai-trained-generate-incredibly-british-place-names/) - Telegraph

## More fun/cool names - honourable mentions:
- Eddwaldbury
- Longltol Norton on The Mork
- Little Lower Poet Hille