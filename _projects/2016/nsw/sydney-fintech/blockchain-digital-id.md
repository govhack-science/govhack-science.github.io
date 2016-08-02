---
datasets_used:
- agency: Australian Taxation Office
  name: Taxation statistics - Individual tax return sample files
  url: http://portal.govhack.org/datasets/2016/australia/australian-taxation-office/taxation-statistics-individual-sample-files.html
- agency: Australian Business Register
  name: ABN Lookup Webservices
  url: http://portal.govhack.org/datasets/2016/australia/australian-business-register/abn-lookup-webservices.html
event: sydney-fintech
hackerspace_url: https://2016.hackerspace.govhack.org/node/2706
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/civics-1million-identity-fraud-protection.jpg
jurisdiction: nsw
prizes:
- australia-that-thing-we-all-need
- australia-commerically-viable-hack
- australia-entrepreneurial-hack
- australia-future-australia-hack
- australia-hiding-wally
- australia-innovative-ideas-hack
- australia-smarter-data
- nsw-acceleration-award-govhack-nsw
project_title: Blockchain Digital ID
project_url: http://bron.tech/govhack
repo:
  name: Github Repo- Blockchain Digital ID
  type: github
  url: https://github.com/vojdan/govhack
team_name: Brontech
video:
  type: youtube
  url: https://www.youtube.com/watch?v=6MRANBXQs4Y
---

THE PROBLEM:
Identity is much more complex construct than we usually anticipate it to be. We take identity for granted and we think of it as undistinguishable component of our existence i.e. “I am therefore I have identity”.  Yet, in the current social settings things get tricky as we live in a world where identity is not commonly possessed but its custodian.  In developed countries, identities and its attributes are stored in detached centralized silos owned by third parties. Cross-referencing, cross-examination and simultaneous update are “mission impossible”.  Centralized storages pose huge risks as they represent “honey pots” for hackers and have no internal mechanism that can prohibit data loss and tampering. Structured like this, identities are lost when one crosses the boundaries of a jurisdiction or are meaningless for more complex digital interactions that require larger set of attributes associated with the ID. In the developing world, the identity crisis takes whole other dimension. The United Nations initiative ID2020 estimates that 2B people in the world do not have legal identity which imposes huge barriers for this people to get bank accounts, access the medical system, vote etc. More than 20M refugees that once have been issued legal identity have lost it on the route to a more secure place to live (e.g. current refugee crisis in Europe).
THE SOLUTION:
So to be short, during the GovHack we have developed a proof of concept for one of the biggest issues in the modern society. Our solution combines multiple data sources, proof storage on Ethereum blockchain, trust score algorithm and simple but intuitive interface.  The main idea behind the developed solution is that there is so much data held by governmental institutions and other companies that can certify the veracity of different attributes of ones identity. By combining multiple streams of data, a citizen can compose more complex ID that holds relevant up to date information that he/she can reveal if needed to a third party. By using proofs stored on the Blockchain and data stored in decentralized fashion, we empower the custodians to be in control of their data, we enable interoperability among gov.institutions and other parties surpassing even geographical borders and we dramatically decrease the damages of potential data breaches. The trust score algorithm calculates the strengths of proofs that one has for his/hers ID attributes and in case of more specific trust scores how she/he stands in comparison to the overall network of peers.
Such architecture solves issues regarding privacy, control and duplication of data that are common in countries like Australia, the data access is persistent across jurisdictions for example in case of cross-border interaction or in disadvantage situation if one becomes a refugee. Also this solution can be used for issuing IDs for new immigrants or refugees.
HOW IT WORKS:
The blockchain ID is used in the following way : 
1.     Each citizen creates an account where he/she enters attributes of his/her ID like name, last name, gender, affiliations etc.
2.     Then to improve the trust score the user “requests” cross referenced attestation from governmental sources regarding his attributes. Here we use the ATO individual tax returns to verify personal attributes (e.g. gender, income) and we connect with Australian Business Registry to check the veracity of the user’s affiliations (e.g. if she is a CEO of a company and the attributes of that company).  
3.     The Blockchain Digital ID also enables connection to third party data sources to verify the attributes of an identity (e.g. Social media- we've connected it with Twitter).
4.     The Blockchain Digital ID also enables attestations by third parties like banks or from peers.
5.     The Blockchain Digital ID calculates trust score based on the strengths of proofs from the different data sources and the overall ranking of the individual according to the governmental aggregated statistic.
USAGE
The users can use the Blockchain Digital ID to verify their identity when needed e.g. when looking for a loan or trusted invoicing. Also this ID can be used to create a track for individuals that cannot obtain legal ID. Usually in refugee crisis this kind of solution is helpful due to its agnosticism towards jurisdiction as well as combination of different data streams.