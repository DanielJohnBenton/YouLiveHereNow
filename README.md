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

## Original idea?
No. It's been done before.
- [AI is traned to generate incredibly British place names](http://www.telegraph.co.uk/technology/2017/07/20/ai-trained-generate-incredibly-british-place-names/) - Telegraph