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

resource "google_cloud_run_v2_service" "backend" {
  name     = "backend"
  location = var.gcp_region

  template {
    containers {
      image = "${var.gcp_region}-docker.pkg.dev/${var.gcp_project_id}/bestpg-repo/backend:latest"
    }
  }
}

resource "google_cloud_run_v2_service" "frontend" {
  name     = "frontend"
  location = var.gcp_region

  template {
    containers {
      image = "${var.gcp_region}-docker.pkg.dev/${var.gcp_project_id}/bestpg-repo/frontend:latest"
    }
  }
}
