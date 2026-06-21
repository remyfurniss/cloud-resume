locals {
  website_files = {
    "index.html" = {
      source = "../website/index.html"
      type   = "text/html"
    }

    "script.js" = {
      source = "../website/script.js"
      type   = "application/javascript"
    }

    "style.css" = {
      source = "../website/style.css"
      type   = "text/css"
    }
  }
}