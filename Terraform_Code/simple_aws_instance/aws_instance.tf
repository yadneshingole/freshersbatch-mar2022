provider "aws"{
	
	region = "us-east-1"
	access_key = "AKIA2JIL7S5ZPAT7Z2CT"
	secret_key = "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"
	version = "~> 2.0"
}
resource "aws_instance" "web1" {
	ami = "ami-0022f774911c1d690"
	instance_type = "t2.micro"

	tags = {
    Name = "terraform-example"
  }
}