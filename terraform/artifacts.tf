resource "google_artifact_registry_repository" "bestpg_repo" {
  location      = "asia-south1"
  repository_id = "bestpg-repo"
  description   = "Docker repository for the BestPG application images"
  format        = "DOCKER"
}
