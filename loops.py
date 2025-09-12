# List is a data structure which can hold multiple values of multiple types
# Array is a data structure whoch can ho;d multiple values of same type
List_of_clouds = ["aws", "azure", "GCP", "digital ocean", "utho", "alibaba", "oracle"]
cloud = "gcp"

#print (List_of_clouds)

# add a new cloud
List_of_clouds.append("Salesforce")
List_of_clouds.append("IBM")
#print (List_of_clouds)

List_of_clouds.insert(2,"Heroku")
#print(List_of_clouds)
#print(len(List_of_clouds))

List_of_clouds.insert(0,"Hello Cloud")
#print(List_of_clouds)
List_of_clouds.remove("aws")
#print(List_of_clouds)

for cloud in List_of_clouds:
    print(cloud)

for i in range(1,11):
    print(i)