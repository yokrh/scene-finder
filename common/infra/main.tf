# Variable
variable "aws_accesskey_id" {
}
variable "aws_accesskey_secret" {
}
variable "aws_region" {
}
variable "aws_s3_bucket_name" {
}

# Provider
provider "aws" {
  access_key = var.aws_accesskey_id
  secret_key = var.aws_accesskey_secret
  region     = var.aws_region
}

# S3
resource "aws_s3_bucket" "bucket" {
  bucket = var.aws_s3_bucket_name
}

# Output
output "s3_bucket_id" {
  value = "${aws_s3_bucket.bucket.id}"
}
