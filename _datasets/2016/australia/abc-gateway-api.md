---
dataset_url: https://content-api-govhack.abc-prod.net.au/v1/6946348
excerpt_separator: <!--more-->
gid: abc-gateway-api
jurisdiction: australia
name: ABC Gateway API
organisation: abc
title: ABC Gateway API
mentors:
  - sarah-bolt
---

This API provides access to retrieve individual pieces of ABC News Content and some associated metadata.  It provides users with, amongst other things, detailed information about ABC News articles including their body text.  This portal to a substantial body of written News content allows significant opportunity to explore many analysis approaches including natural language processing techniques.  

<!--more-->

It can be also be used in conjunction with the other data extract highlighted by the ABC, 'Views of ABC News Digital Content (May 2016)' provided on data.gov.au.  The latter provides hourly traffic to ABC News content on some of the ABC's digital properties.  In combination these sources provide data on what news Australians are reading about in what quantities, when and on what platforms. 

Details
The Content Gateway API is an API to retrieve content and metadata by content ID.  With each call, it returns a document or collection using that document's numeric id.  There are various different document types, the most common being an article.  For example for article 7647654 (http://www.abc.net.au/news/2016-07-21/most-accurate-map-yet-of-human-brain-released-by-scientists/7647654) the content is retrieved by calling:

https://content-api-govhack.abc-prod.net.au/v1/6946348

Output
Output is JSON.  The following fields are provided for article documents when available:
â¢	id -  numeric content id
â¢	doctype - string document type
â¢	title - title of this document.
â¢	shortTeaserTitle - string
â¢	teaserTitle - string
â¢	shortTeaserTextPlain - string, plain text, links removed
â¢	shortTeaserText - string, HTML 
â¢	teaserTextPlain - string, plain text, links removed
â¢	teaserText - string, HTML  
â¢	location - a list of all location taxonomies, each will have a content ID, name, postcode, latitude and longitude and its parents.
â¢	subject - a list of all subject taxonomies, each will have subject name, content ID and its parents
â¢	contentGenre - string description of the content genre
â¢	thumbnailLink - thumbnail links for this document
â¢	relatedItems - list of id, doctype and short teaser title for related documents
â¢	firstPublishedDate - ISO8601 format (yyyy-MM-dd'T'HH:mm:ssZZ) with zone UTC
â¢	lastPublishedDate - ISO8601 format (yyyy-MM-dd'T'HH:mm:ssZZ) with zone UTC
â¢	validTo - ISO8601 format (yyyy-MM-dd'T'HH:mm:ssZZ) with zone UTC
â¢	canonicalUrl - the absolute url of the document
â¢	importance - numeric value giving editorial importance
â¢	latitude - a string value for latitude of primary location
â¢	longitude - a string value for longitude of primary longitude
â¢	version - a numeric value representing the current version of the document
â¢	keywords - a group of strings separated by comma
â¢	textPlain - string, HTML, main body content

The API does currently have rate limits so you may get an error message "Too many requests".  The API will be available from now through to completion of the competition.