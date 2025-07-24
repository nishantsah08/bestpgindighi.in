terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

resource "google_artifact_registry_repository" "bestpg_repo" {
  location      = var.gcp_region
  repository_id = "bestpg-repo"
  description   = "Docker repository for the BestPG application images"
  format        = "DOCKER"
}
