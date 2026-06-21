
output "api_url" {
  value = aws_apigatewayv2_api.visitor_api.api_endpoint
}

output "cloudfront_url" {
  value = aws_cloudfront_distribution.cdn.domain_name
}