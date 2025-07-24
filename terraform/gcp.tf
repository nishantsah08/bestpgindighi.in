terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.34"
    }
  }
}

provider "google" {
  region  = "asia-south1"
}

variable "gcp_project_id" {
  description = "The GCP project ID."
  type        = string
}

resource "google_cloud_run_v2_service" "backend" {
  project  = var.gcp_project_id
  name     = "backend"
  location = "asia-south1"

  template {
    containers {
      image = "asia-south1-docker.pkg.dev/${var.gcp_project_id}/bestpg-repo/backend:latest"
      ports {
        container_port = 8080
      }
      env {
        name  = "DATABASE_URL"
        value = "postgresql://postgres.jagtvsfsraqpznftvpkx:${google_secret_manager_secret_version.supabase_password_version.secret_data}@aws-0-ap-south-1.pooler.supabase.com:6543/postgres"
      }
    }
  }
}

resource "google_cloud_run_v2_service" "frontend" {
  project  = var.gcp_project_id
  name     = "frontend"
  location = "asia-south1"

  template {
    containers {
      image = "asia-south1-docker.pkg.dev/${var.gcp_project_id}/bestpg-repo/frontend:latest"
      ports {
        container_port = 80
      }
    }
  }
}
