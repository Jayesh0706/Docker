# Docker Volumes
For non-database use cases (like shared logs or static files), it’s generally fine to share the same directory as long as you avoid write conflicts.
For databases or high-risk conflicts, always use separate directories or Docker-managed named volumes.
