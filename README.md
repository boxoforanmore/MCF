# Musical Catalyst Framework #

## About ##
The Musical Catalyst Framework comes from [Martin Tourish's PhD thesis](https://arrow.dit.ie/appadoc/46/).  In the thesis, Martin describes a system that can be used for individual or institutional educational purposes wherein a student can objectively have the stylistic elements of their playing graded and captured in some sense.  Additionally, the MCF (once filled with more examples) could be used by Master-level musicians to further develop their own style.  The first iteration of the MCF will likely rely on human input and assessment (via the instructor), with the process turning to only slightly supervised once some classfiers have been trained.

A further purpose for this project could be extrapolating an individual musician's style onto a new piece of music using a generative neural network.  For example, we could predict how Johnny Doherty might play a more recently composed tune that he would never have before seen.

While the MCF was originally intended for music and style in the contect of the world of Irish Traditional Music, other traditional musics could certainly be added to the framework if similar research was performed on in the respective musical pantheon.


## Current Progress ##
* MongoDB is being used for the inconsistency in some of the data
	* Launch MongoDB with `./run_me.sh`
* Filler scripts for the DB are in progress
	* Tune-types are done
	* Rhythms are in progress
	* Run the individual python scripts to fill the database


## What Needs to Be Done ##
* Finish the filler scripts
* Process audio into a simple ABC-notation format
	* Also create a more fluid and expansive ABC to MusicXML translator
* Add a front-end (using Flask or Django)
* Add AuthN and AuthZ
	* AuthZ should have admin, instructor, and student (possibly more)
* Train models to automatically classify a piece and place the various stylistic elements


#### Please contact Peter N (boxoforanmore) with any questions about this project ####
#### Reviewed contributions are welcomed ####
