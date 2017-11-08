import sys
import random
import numpy
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
from keras.optimizers import RMSprop

# =====
# SETTINGS
INPUT_PATH = "data/placenames_uk.txt";

PRESERVE_CASE = True
SHUFFLE_INPUT = True
PIECE_LEN = 10
STEP = 3

LSTM_N = 50
LEARN_RATE = 0.01
LOSS_FUNCTION = "categorical_crossentropy"
TRAIN_ITERATIONS = 200

TEST_DIVERSITIES = [0.2, 0.5, 1.0, 1.2]
NAMES_PER_DIVERSITY = 100
KEEP_ALREADY_EXISTING_NAMES = False
DISPLAY_DISCARDED = True
BAD_OUTPUT_LIMIT = 300
# =====

text = open(INPUT_PATH, encoding="utf-8").read()
if not PRESERVE_CASE:
	text = text.lower()
	print("Will not preserve case.")

if SHUFFLE_INPUT:
	items = text.splitlines()
	random.shuffle(items)
	text = "\n".join(items)
	print("Input lines have been shuffled")

existingPlacesLookup = {}
if not KEEP_ALREADY_EXISTING_NAMES:
	existingNames = dict((name, i) for i, name in enumerate(text.lower().splitlines()))
	print("Pre-existing items will not count during generation.")

characters = sorted(list(set(text)))

lText = len(text)
lCharacters = len(characters)

charIndices = dict((c, i) for i, c in enumerate(characters))
indicesChar = dict((i, c) for i, c in enumerate(characters))

pieces = []
nextChars = []
for i in range(0, lText - PIECE_LEN, STEP):
	pieces.append(text[i:i + PIECE_LEN])
	nextChars.append(text[i + PIECE_LEN])

x = numpy.zeros((len(pieces), PIECE_LEN, lCharacters), dtype=numpy.bool)
y = numpy.zeros((len(pieces), lCharacters), dtype=numpy.bool)

for i, piece in enumerate(pieces):
	for t, character in enumerate(piece):
		x[i, t, charIndices[character]] = 1
	y[i, charIndices[nextChars[i]]] = 1

model = Sequential()
model.add(LSTM(LSTM_N, input_shape=(PIECE_LEN, lCharacters)))
model.add(Dense(lCharacters))
model.add(Activation("softmax"))

optimiser = RMSprop(lr=LEARN_RATE)

model.compile(loss=LOSS_FUNCTION, optimizer=optimiser)

def sample(preds, temperature=1.0):
	# helper function to sample an index from a probability array
	preds = numpy.asarray(preds).astype("float64")
	preds = numpy.log(preds) / temperature
	expPreds = numpy.exp(preds)
	preds = expPreds / numpy.sum(expPreds)
	probas = numpy.random.multinomial(1, preds, 1)
	return numpy.argmax(probas)

for iteration in range(1, TRAIN_ITERATIONS + 1):
	print()
	print("=" * 30)
	print("Iteration:", iteration)
	
	model.fit(x, y, batch_size=LSTM_N, epochs=1)
	
	xStart = random.randint(0, lText - PIECE_LEN - 1)
	
	for diversity in TEST_DIVERSITIES:
		print()
		print("--- DIVERSITY:", diversity, "---")
		print()
		
		seed = text[xStart:xStart + PIECE_LEN]
		currentCharacter = ""
		
		length = 0
		
		while currentCharacter != "\n" and length < BAD_OUTPUT_LIMIT:
			x_pred = numpy.zeros((1, PIECE_LEN, lCharacters))
			for t, character in enumerate(seed):
				x_pred[0, t, charIndices[character]] = 1.
			
			preds = model.predict(x_pred, verbose=0)[0]
			nextIndex = sample(preds, diversity)
			currentCharacter = indicesChar[nextIndex]
			seed = seed[1:] + currentCharacter
			length += 1
		
		generatedNames = []
		generatedNamesLookup = {}
		nGenerated = 0
		
		realNamesDiscarded = 0
		duplicatesDiscarded = 0
		
		while nGenerated < NAMES_PER_DIVERSITY:
			name = ""
			currentCharacter = ""
			
			length = 0
			
			while currentCharacter != "\n" and length < BAD_OUTPUT_LIMIT:
				x_pred = numpy.zeros((1, PIECE_LEN, lCharacters))
				for t, character in enumerate(seed):
					x_pred[0, t, charIndices[character]] = 1.
				
				preds = model.predict(x_pred, verbose=0)[0]
				nextIndex = sample(preds, diversity)
				currentCharacter = indicesChar[nextIndex]
				seed = seed[1:] + currentCharacter
				
				if currentCharacter != "\n":
					name += currentCharacter
					length += 1
			
			if not KEEP_ALREADY_EXISTING_NAMES and name.lower() in existingNames:
				realNamesDiscarded += 1
			elif name in generatedNamesLookup:
				duplicatesDiscarded += 1
			else:
				generatedNames.append(name)
				generatedNamesLookup[name] = True
				nGenerated += 1
		
		totalGenerated = nGenerated + realNamesDiscarded + duplicatesDiscarded
		
		print("\n".join(generatedNames))
		print("--- DISCARDED:", realNamesDiscarded, "real names (", (realNamesDiscarded / totalGenerated * 100), "% );", duplicatesDiscarded, "duplicates (", (duplicatesDiscarded / totalGenerated * 100), "% )")
