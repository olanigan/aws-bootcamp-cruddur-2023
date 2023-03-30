terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.59.0"
    }
  }
}

provider "aws" {
  data "aws_db_instance" "database" {
    db_instance_identifier = "my-test-database"
    }
}