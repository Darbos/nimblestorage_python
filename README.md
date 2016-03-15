### Sample Python class for working with the Nimble Storage REST API  
  
At Capella University we recently introduced 6 individual CS700s (no grouping) connected by fiber channel. We use a much more robust Python class like this in our automated processes alongside UCS SDK and Custom Fabric MDS wrapper. This is a stripped down version I have been re-writing in my spare time to give other people a basic framework to start automating their Nimble Storage environments.  
  
I will try to add what I can, but would appreciate any contributions/fixes/logging.  
  
The more people that rely and make operational demands of the Nimble Storage REST API, the more resources they will apply to the API development team(s).  


### Nimble RFE(s)  
"Update initiator alias with API." - Allow Initiator's aliases to be renamed through the API (there is a workaround in the GUI). This would only be an issue for you if you are constantly recycling WWPNs (Cisco UCS blades).  

"ALL/DETAIL endpoint for snapshots" - Get limited amounts of information about every snapshot on the array (instead of having to loop through every volume and running a query for each volume)  

