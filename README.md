# Spongebob Case Converter

This is a very small Python script to convert any sentence to Mocking Spongebob mixed capitalization at the command line. It also provides its `to_spongecase` function for this to be done with any string in another program.

By default, `to_spongecase` returns a string with an approximate 50/50 distribution of uppercase and lowercase letters. It can alternatively be given a percentage &ndash; a `float` in the range [0.0, 1.0] &ndash; for a custom distribution. A particular string will always capitalize in the same pattern given a capitalization chance, e.g. "The freer the market, the freer the people." will always be converted to "tHe FrEer ThE markEt, tHe fReer the people." given a capitalization chance of 30%.

When running `spongebob_case.py` at the console, the text to be converted can be proceeded by the long-form option `--cap-chance=###%` or `--lower-chance=###%`, where `###` is a number from 0 to 100, optionally padded with arbitrarily many zeroes. This controls the capitalization distribution, and one is merely the inverse of the other. Note that if a typo is made in the option text, it will be considered part of the sentence and the default 50% distribution will be used.

See also: **[Know Your Meme: Mocking Spongebob](http://knowyourmeme.com/memes/mocking-spongebob)**

<img src="https://raw.githubusercontent.com/dhildebr/spongebob-case/master/memEs%20aRen't%20a%20SeRious%20SubjECt.jpg" />
