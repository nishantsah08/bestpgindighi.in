variable "supabase_password" {
  description = "The password for the Supabase database."
  type        = string
  sensitive   = true
}

resource "google_secret_manager_secret" "supabase_password" {
  secret_id = "supabase-password"

  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "supabase_password_version" {
  secret      = google_secret_manager_secret.supabase_password.id
  secret_data = var.supabase_password
}
