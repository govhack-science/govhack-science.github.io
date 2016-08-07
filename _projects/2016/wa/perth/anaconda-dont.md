---
category: ''
datasets_used:
- agency: Water corporation
  name: Water corporation aerial UAV images
  url: ''
event: perth
hackerspace_url: https://2016.hackerspace.govhack.org/node/3166
jurisdiction: wa
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-exploring-underground
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-machine-learning-hack
- australia-location-data
- wa-geospatial-prize
- wa-most-promising-govhacker
- wa-western-australian-entrepeneurial-prize
- wa-western-australian-solution-prize
- wa-western-australian-sustainability-prize
project_title: Anaconda Don't
project_url: ''
repo:
  name: Govhack 2016 Team Anaconda
  type: google-drive
  url: https://drive.google.com/folderview?id=0B3WXEtmAkqOMclB2ZlhMd1RLSDQ&usp=sharing
team_name: Anaconda Don't
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/Anaconda%20dont%20video.mp4
  type: youtube
  url: https://www.youtube.com/watch?v=8wDEIkRUPCg
---

​​​​​​​The Water Corporation is the principal supplier of drinking water to the Perth metropolitan area as well as the rest of Western Australia. For some of these towns, the water is supplied through a vast network of above ground pipes. These pipes require regular inspections and maintenance to make sure that the precious cargo it is carrying isn’t leaking out and wasted.
 
Currently, the Water Corporation inspects their above ground pipe assets using photos taken by aerial UAVs that are flown along the length of the pipes. This is then sent back to the office where several people have to look through the massive number of images and manually mark out and record the coordinates of features along the pipes, such as repair bands and footings.
 
We are developing a solution where we are able to take the aerial images, apply a number of computer vision algorithms and image manipulation techniques, and automatically mark out the coordinates of notable features such as repair bands and pipe footings which provide information about the network to the Water Corporation. 
 
To further augment this assessment a thematic map that describes the number of defects per linear unit could assist with budget allocation.
 
Depending on other factors, positional accuracy could also be improved for Water Corporations pipe vector layer, allowing for other improvements in analysis.
 
Process
 

Open the image


Resize image for ease of processing and accuracy improvements


Run some processes in the opencv (opensource) library - edge detection and smoothing


Detect the vectors of a pipe using a Hough line transform


Determine the rotation, scale and position of the pipe according to the Hough line


Use these parameters to crop the high resolution image


Against the cropped image use signal processing techniques to determine edges and events along the pipe


Classify the event and record the position of the event in image space


Transform the event to real world coordinates


Classify linear events along the pipe - eg xx events per kilometre, xx events per pipe segment


Review network for highest defect rate as an indicator to direct maintenance effort


Ultimately - A recommendation engine of above ground pipe network maintenance

 
At this stage we would have some certainty of an event along the pipe, however the classification technique would be improved by some deep learning process. The deep learning process could use the event markers in the above process to capture training data sets. These training datasets could then be used to process other images.
 
Considerations

Image variability


Real world coordinate system accuracy


Accuracy of classification 


Employment shifts to higher value work because of innovation - eg. assessment of fund spending, failure prediction, actual maintenance, etc


Open source programming


Leak detection / vegetation growth


Deep / machine learning opportunity