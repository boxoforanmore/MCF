from __future__ import print_function
import pymongo

# Connect to the server
client = pymongo.MongoClient('localhost', 27017)


#### TO DO ####
# -- Make primary keys the tune_type_names
# -- Add rest of tune_types
# -- Add ABC notation of characteristic examples
# -- Rename char_ex to 'archetypes'
# -- Rename rhythmic_char to 'rhythmic_notes'
# --------> Fix spelling of rhythmic throughout




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

# Slow Air (trad)
tune_types[0]['metre'] = ('3/4', '4/4')
tune_types[0]['tempo'] = ("Slow", "Not discernable")
tune_types[0]['rythmic_char'] = ("use of rubato", "spacious", "song-like")
tune_types[0]['strong_beats'] = None
tune_types[0]['char_ex'] = None                 # The slow air provided should be added here


# Slow Air (Romantic)
tune_types[1]['metre'] = ('3/4', '4/4')
tune_types[1]['tempo'] = ("Slow", "Not discernable")
tune_types[1]['rythmic_char'] = ("heavy use of rubato", "spacious", "song-like")
tune_types[1]['strong_beats'] = None
tune_types[1]['char_ex'] = None                  # The romantic slow air provided should be added here


# Double Reel
tune_types[2]['metre'] = ('4/4')
tune_types[2]['tempo'] = ('a minim', '+-112 BPM')
tune_types[2]['rythmic_char'] = ('motoric quaver rhythm occasionally broken by crochets and longer values')
tune_types[2]['strong_beats'] = ('1', '3')
tune_types[2]['char_ex'] = None                  # The double reel provided should be added here


# Single Reel
tune_types[3]['metre'] = ('2/2')
tune_types[3]['tempo'] = ('Minim', '+-122 BPM')
tune_types[3]['rythmic_char'] = ('motoric quaver rhythm occasionally broken by crochets and longer values', 'strong feeling of two pulses per bar')
tune_types[3]['strong_beats'] = ('1', '2')
tune_types[3]['char_ex'] = None                  # The single reel provided should be added here


# Slow Reel
tune_types[4]['metre'] = ('2/2')
tune_types[4]['tempo'] = ('minim', '+-70 BPM')
tune_types[4]['rythmic_char'] = ('motoric quaver rhythm occasionally broken by crochets and longer values', 'very mildly swung'))
tune_types[4]['strong_beats'] = ("1'", "2'")     # The single quote here is meant to represent a more minor emphasis on the beat
tune_types[4]['char_ex'] = None                  # The slow reel provided should be added here


# Dancer's Hornpipe
tune_types[5]['metre'] = ('4/4')
tune_types[5]['tempo'] = ('crotchet', '+-113 BPM'))
tune_types[5]['rythmic_char'] = ('motoric rhythm punctuated by two or three accented beats usually on the same pitch and typically at the end of eight-bar phrases', \
                               'can contain anything from a mild to substantial use of triplets', 'accentuation of beats one, two, and three at the end of a tune part')
tune_types[5]['strong_beats'] = ('1', '3')
tune_types[5]['char_ex'] = None                  # The dancer's h-pipe provided should be added here


# Instrumentalist's Hornpipe
tune_types[6]['metre'] = ('4/4')
tune_types[6]['tempo'] = ('crotchet', '+-150 BPM')
tune_types[6]['rythmic_char'] = ('motoric rhythm punctuated by two or three accented beats usually on the same pitch and typically at the end of eight-bar phrases', \
                               'can contain anything from a mild to substantial use of triplets', 'accentuation of beats one, two, and three at the end of a tune part')
tune_types[6]['strong_beats'] = ('1', '3')
tune_types[6]['char_ex'] = None                  # The intsrumentalist's h-pipe provided should be added here


# Barndance
tune_types[7]['metre'] = ('4/4')
tune_types[7]['tempo'] = ('minim', '+-80 BPM')
tune_types[7]['rythmic_char'] = ('motoric rhythm making use of the three accents on beats one, two, and three of the bar, typically occurrring at the ends of phrases', \
                               'tends to use three-accent motif or variant thereofat the end of some phrases', 'stringly marked rhythm with an emphatic ending to each section')
tune_types[7]['strong_beats'] = ('1', '3')
tune_types[7]['char_ex'] = None                  # The barndance provided should be added here


# Strathspey
tune_types[8]['metre'] = ('4/4')
tune_types[8]['tempo'] = ('minim', '+-95 BPM')
tune_types[8]['rythmic_char'] = ('a highly swung motoric quaver rhythm feauring the Scotch Snap and its inverse', 'Scotch Snap', \
                               'it also features a considerable use of triplet rhythms, usually towards the end of a phrase')
tune_types[8]['strong_beats'] = ('1', '3')
tune_types[8]['char_ex'] = None                  # The strathspey provided should be added here


# Highland
tune_types[9]['metre'] = ('4/4')
tune_types[9]['tempo'] = ('minim', '+-90 BPM')
tune_types[9]['rythmic_char'] = ('gently swung motoric rhythm punctuated by the presence of crotchets', 'occationally features runs of triplets')
tune_types[9]['strong_beats'] = ('1', '3')
tune_types[9]['char_ex'] = None                  # The highland provided should be added here


# 2/4 March
tune_types[10]['metre'] = ('2/4')
tune_types[10]['tempo'] = ('crotchet', '+-117 BPM')
tune_types[10]['rythmic_char'] = ('predominantly quaver rhythm broken by dotted quaver to semiquaver duplets')
tune_types[10]['strong_beats'] = ('1', '2')
tune_types[10]['char_ex'] = None                  # The 2/4 march provided should be added here


# 4/4 March
tune_types[11]['metre'] = ('4/4')
tune_types[11]['tempo'] = ('crotchet', '+-75 BPM')
tune_types[11]['rythmic_char'] = ('predominantly crotchet rhythm broken by quaver runs', 'strong accented feel')
tune_types[11]['strong_beats'] = ('1', '3')
tune_types[11]['char_ex'] = None                  # The 4/4 march provided should be added here


# 6/8 March
tune_types[12]['metre'] = ('6/8')
tune_types[12]['tempo'] = ('dotted crotchet', '+-85 BPM')
tune_types[12]['rythmic_char'] = ('predominantly motoric quaver rhythm broken by both longer and shorter rhythmic values', 'strong accented feel')
tune_types[12]['strong_beats'] = ('1', '4')
tune_types[12]['char_ex'] = None                  # The 6/8 march provided should be added here


# 3/4 March
tune_types[13]['metre'] = ('3/4')
tune_types[13]['tempo'] = ('crotchet', '+-113 BPM')
tune_types[13]['rythmic_char'] = ('a motoric quaver rhythm broken by longer rhythmic values', 'strong accented feel')
tune_types[13]['strong_beats'] = ('1')
tune_types[13]['char_ex'] = None                  # The 3/4 march provided should be added here


# Narrative Air
tune_types[14]['metre'] = ('3/4')
tune_types[14]['tempo'] = ('Slow (yet animated)', 'Not discernable')
tune_types[14]['rythmic_char'] = ('begins with an anacrusis of three quavers', \
                                  'follows a quaver rhythm that is broken at the second bear of the bar by a longer rhythmic value, usually a crotchet or a dotted crotchet', \
                                  'heavy rubato is utilised')
tune_types[14]['strong_beats'] = None
tune_types[14]['char_ex'] = None                  # The narrative air provided should be added here


# 4/4 Set Dance
tune_types[15]['metre'] = ('4/4')
tune_types[15]['tempo'] = ('minim', '+-52 BPM')
tune_types[15]['rythmic_char'] = ('motoric quaver rhythm occasionally broken b longer and shorter rhythmic values', \
                                  'the B-part tends to be longer, usually twelve bars in length, than the typically eight-bar A-part', \
                                  'usually arranged by a dancing master for some set choreography')
tune_types[15]['strong_beats'] = ('1', '3', None)
tune_types[15]['char_ex'] = None                  # The 4/4 set dance provided should be added here


# 6/8 Set Dance
tune_types[16]['metre'] = ('6/8')
tune_types[16]['tempo'] = ('dotted crotchet', '+-95 BPM')
tune_types[16]['rythmic_char'] = ('a dotted quaver - semiquaver - quaver rhythm occasionally broken by longer and shorter rhythmic values', \
                                  'the B-part tends to be longer, usually twelve bars in length, than the typically eight-bar A-part', \
                                  'usually arranged by a dancing master for some set choreography')
tune_types[16]['strong_beats'] = ('1', '4', None)
tune_types[16]['char_ex'] = None                  # The 6/8 set dance provided should be added here


# Single Polka
tune_types[13]['metre'] = ('2/4')
tune_types[13]['tempo'] = ('crotchet', '+-160 BPM')
tune_types[13]['rythmic_char'] = ('motoric quaver rhythm with occational dotted quaver to semiquaver rhythms and use of crotchets at cadence points')
tune_types[13]['strong_beats'] = ('1', '2')
tune_types[13]['char_ex'] = None                  # The single polka provided should be added here


# Double Polka
tune_types[13]['metre'] = ('2/4')
tune_types[13]['tempo'] = ('crotchet', '+-114 BPM')
tune_types[13]['rythmic_char'] = ('rhythm based on semiquavers broken by quavers', 'occasionally featuring dotted quavers to semiquavers')
tune_types[13]['strong_beats'] = ('1', '2')
tune_types[13]['char_ex'] = None                  # The double polka  provided should be added here


# Early Jig
tune_types[13]['metre'] = ('6/4')
tune_types[13]['tempo'] = ('dotted minim', '+-60 BPM')
tune_types[13]['rythmic_char'] = ('it is based on a crotchet rhythm', 'phrases tend to open on a minim value', 'A-part usually shorter than the B-part')
tune_types[13]['strong_beats'] = ('1', '4')
tune_types[13]['char_ex'] = None                  # The early jig provided should be added here


# Early Slip Jig
tune_types[13]['metre'] = ('9/4')
tune_types[13]['tempo'] = ('dotted minim', '+-60 BPM')
tune_types[13]['rythmic_char'] = ('crotchet based rhythm', 'occasionally broken by minims', 'A-part usually 4-bars', 'B-part usually 6-bars')
tune_types[13]['strong_beats'] = (None)
tune_types[13]['char_ex'] = None                  # The early slip jig provided should be added here 


# Single Jig
tune_types[13]['metre'] = ('6/8')
tune_types[13]['tempo'] = ('dotted crotchet', '+-137 BPM')
tune_types[13]['rythmic_char'] = ('primarily but not exclusively features the crotchet - quaver rhythm', 'three quaver group followed by a crotchet or dotted crotchet')
tune_types[13]['strong_beats'] = ('1', '2')
tune_types[13]['char_ex'] = None                  # The early jig provided should be added here


# Double Jig
tune_types[13]['metre'] = ('6/8')
tune_types[13]['tempo'] = ('crotchet', '+-127 BPM')
tune_types[13]['rythmic_char'] = ('it is based on a crotchet rhythm', 'phrases tend to open on a minim value')
tune_types[13]['strong_beats'] = ('1', '4')
tune_types[13]['char_ex'] = None                  # The early jig provided should be added here





# Create/select mcf dataase
tunedb = client.mcf

# Drop collection
print('Dropping collection person')
tunedb.tune_types.drop()

# Add a tune-type
print('Adding tune-types')
employee = dict(name='', age=30)
for tune_type in tune_types:
    mcf.tune_types.insert(tune_type)


# Fetch list of all databases (mcf should be present)
print("DB's present on the system:")
for db in client.list_databases():
    print('    %s' % db)

# Close connection
print('Closing client connection')
client.close()
