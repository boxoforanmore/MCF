from __future__ import print_function
import pymongo

# Connect to the server
client = pymongo.MongoClient('localhost', 27017)


#### TO DO ####
# -- Make primary keys a combination of time signature and one-bar rhythm
# -- Add ABC notation of characteristic examples (also add sound files and MXML?)
# -- Rename char_ex to 'archetypes'
# -- Rename rhythmic_char to 'rhythmic_notes'
# --------> Fix spelling of rhythmic throughout



swings = ['almost straight', 'traditional swing', 'near dotted']
one_bar_rhythms = [] # All of these need to be added
time_sigs = []
char_version = [] # Of one bar rhythm, with intervals


# List of tune types to help allow more dynamicism
tune_type_names = ['Slow Air (trad)', 'Slow Air (Romantic)', '(Double) Reel', \
              'Single Reel', 'Slow Reel', "Dancer's Hornpipe", \
              "Instrumentalist's Hornpipe", 'Barndance', 'Strathspey', \
              'Highland', '2/4 March', '4/4 March', '6/8 March', \
              '3/4 March', 'Narrative Air', '4/4 Set Dance', \
              '6/8 Set Dance', 'Single Polka', 'Double Polka', \
              'Early Jig', 'Early Slip Jig', 'Single Jig', \
              'Double Jig', 'Heavy Double Jig', 'Heavy Single Jig', \
              'Slide', 'Slip Jig', 'Hop Jig', 'Waltz', 'Mazurka', \
              '7/8 tunes']

tune_types = list()

for tune_type in tune_type_names:
    tune_types.append(dict(name=tune_type, metre=None, tempo=None, \
                           rythmic_char=None, \
                           strong_beats=None, char_ex=None))


# Create/select mcf dataase
tunedb = client.mcf

# Drop collection
print('Dropping collection rhythms')
tunedb.rhythms.drop()

# Add a tune-type
print('Adding rhythms')
for tune_type in tune_types:
    mcf.tune_types.insert(tune_type)


# Fetch list of all databases (mcf should be present)
print("DB's present on the system:")
for db in client.list_databases():
    print('    %s' % db)

# Close connection
print('Closing client connection')
client.close()
