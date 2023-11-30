provider "github" {
  token = "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"
}

resource "github_repository" "day2" {
  name        = var.day2
  description = "Created with Terraform"
  private     = true
}

variable "day2" {
  description = "day2"
  type        = string
}