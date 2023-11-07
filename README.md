# Grouping-Sounds: Data and Code Accompanying the Study "Grouping Sounds into Evolving Units for the Purpose of Historical Language Comparison"

Original study:

> List, Johann-Mattis; Hill, Nathan W.; Blum, Frederic; Juárez, Cristian (under review): Grouping Sounds into Evolving Units for the Purpose of Historical Language Comparison. Submitted to Open Research Europe.

## Installation

You will need `pyedictor` and `lingpy` as outlined in `requirements.txt`. Install all dependencies with `pip` as follows:

```
pip install -r requirements.txt
```

## Running the Code

To download the database and automatically create the profile, run:

```
python make-profile.py
```

To test the profile, run:

```
python grouping.py
```

The profile itself can be found in file `karen-profile.tsv`.

## Check Examples in EDICTOR

The file `examples.tsv` can be readily loaded into the [EDICTOR](https://digling.org/edictor) and from there, you can access the new formats that we introduced for grouped sounds.
