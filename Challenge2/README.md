# Challenge2

We need to write code that will query the meta data of an instance within AWS and provide a json formatted output. The choice of language and implementation is up to you.

Bonus Points

The code allows for a particular data key to be retrieved individually. For solution see ** ec2-metadata **

# ec2-metadata

**Pre-Requisites**

To run this program we need AWS EC2 Instance, where we should run below snippet (python3 by default present in Linux Machines)

```
python3  ec2-metadata.py
```

Will give you metadata of EC2 Instance as below:


<img src="MetadataJSON.jpeg" alt="MetadataJSON" class="inline"/>

As well for Retrieve Data key individually

<img src="MetadataOptions.jpeg" alt="MetadataOptions" class="inline"/>

For Retrieving Data, need to give the index or option from the MetaData List

<img src="MetadataIndex.jpeg" alt="hi" class="inline"/>
