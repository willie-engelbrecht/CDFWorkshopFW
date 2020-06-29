# CDFWorkshopFW

Opens up the AWS firewall rules for a CDF workshop. 


# Usage
```
sudo bash -c "$(curl -s https://raw.githubusercontent.com/willie-engelbrecht/CDFWorkshopFW/master/setup.sh)"
```

You will be asked 5 Questions:
```
AWS Access Key: <abc>
AWS Secret Key: <xyz>
Security Group 1: sg-0b0<digits>     # Look in the AWS Console for the default-cluster instance Security Group info
Security Group 2: sg-09b<digits>     # Look in the AWS Console for the default-web instance Security Group info
Workshop Keyword: secretcode
```

### Additional steps
* Please go to your AWS console and open up port 8080 for your CDF "default-web" instance to 0.0.0.0/0
