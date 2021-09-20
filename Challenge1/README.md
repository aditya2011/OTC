# Challenge1

A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

**Three-Tier Architecture Overview**

The three-tier architecture is the most popular implementation of a multi-tier architecture and consists of a single presentation tier, logic tier, and data tier. This architecture is used in a client-server application such as a web application that has the frontend, the backend, and the database. Each of these layers or tiers does a specific task and can be managed independently of each other.

<img src="3tierarch.png" alt="3tierarch" class="inline"/>


**Pre-Requisites**

. Install Terraform
. Install AWS CLI
. Signup for an AWS Account
. Create IAM Programattic User and configure AWS Access Key and AWS Secret Key

**AWS**

Amazon Web Service (AWS) is a cloud platform that provides different cloud computing services, we are using AWS Services for completing this challenge and build a three tier cloud infrastructure.

**Terraform**

For Fullfilling this challenge, I am taking Terraform as IAC,HashiCorp Terraform is a tool for building, changing, and versioning infrastructure that has an open-source and enterprise version. Terraform is cloud agnostic and can be used to create multi-cloud infrastructure, which uses HCL(HarshiCorp Configuration Language) for IAC.

**Solution**

Below are the parts or steps which we create while creating 3 -tier Architecture in AWS:

1. Virtual Private Cloud (VPC):

2. Setup the Internet Gateway:

3. Create 3 Subnets :

4. Create Two Route Tables with route table Association:

5. Create the NAT Gateway:

6. Create RDS for storage :

We will create below Architecture in 3 tier:

<img src="3-Tier-AWS-Arch.jpeg" alt="3-Tier-AWS-Arch" class="inline"/>

**Overview**

Step 1: Create a VPC with a CIDR Range

Step 2: Set Internet Gateway to connect with VPC

Step 3: Create 3 subnet as one as public and 2 private subnets.

Step 4: Set route table with Table Association

Step 5: Create NAT Gateway for private instance to get Internet path from the public to private.

Step 6: Create RDS Storage to store the data of the application into the database. That database is called RDS.

