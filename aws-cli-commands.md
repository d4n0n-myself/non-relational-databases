# Prerequisites:
to execute any of the described below scripts add account details (tokens, secret keys) to ~/.aws/credentials

# Show existing EC2 (format: json, result object contains instanceId, subnetId, state): 
aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,Subnet:SubnetId,State:State}" --output json

# Show regions:
aws ec2 describe-regions

# Launch a new EC2 with Amazon AWS CLI:

### Create template to launch from.
1) Add template metadata to file like [this](https://github.com/d4n0n-myself/non-relational-databases/blob/master/launch-template.json)
2) run command: aws ec2 create-launch-template --launch-template-name LaunchTemplate1 --launch-template-data file://launch-template.json

### Launch new EC2 server from a template:
aws ec2 run-instances --launch-template LaunchTemplateId=lt-*** --count 1
