# Variable
variable "aws_accesskey_id" {
}
variable "aws_accesskey_secret" {
}
variable "aws_region" {
}
variable "aws_iam_user_name" {
}


# Provider
provider "aws" {
  access_key = var.aws_accesskey_id
  secret_key = var.aws_accesskey_secret
  region     = var.aws_region
}


# IAM for serverless
resource "aws_iam_user" "user" {
  name = var.aws_iam_user_name
}

resource "aws_iam_access_key" "ak" {
  user = aws_iam_user.user.name
}

resource "aws_iam_user_policy_attachment" "iam_pcy_attach1" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/IAMFullAccess"  # IAM
}
resource "aws_iam_user_policy_attachment" "iam_pcy_attach2" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/AWSCloudFormationFullAccess"  # CloudFormation
}
resource "aws_iam_user_policy_attachment" "iam_pcy_attach3" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"  # S3
}
resource "aws_iam_user_policy_attachment" "iam_pcy_attach4" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/AWSLambdaFullAccess"  # Lambda
}
resource "aws_iam_user_policy_attachment" "iam_pcy_attach5" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator"  # APIGateway
}
resource "aws_iam_user_policy_attachment" "iam_pcy_attach6" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess"  # APIGateway
}
resource "aws_iam_user_policy_attachment" "iam_pcy_attach7" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/AWSCertificateManagerReadOnly"  # ACM
}
resource "aws_iam_user_policy_attachment" "iam_pcy_attach8" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/CloudFrontFullAccess"  # CloudFront
}
resource "aws_iam_user_policy_attachment" "iam_pcy_attach9" {
  user       = aws_iam_user.user.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess"  # Route53
}


# Output
output "iam_user" {
  value = "https://console.aws.amazon.com/iam/home#/users/${aws_iam_user.user.name}?section=security_credentials"
}
output "iam_user_secret" {
  value = "${aws_iam_access_key.ak.secret}"
}
